<template>
  <div ref="scorePieRef" class="chart"></div>
</template>

<script setup>
import {ref, onMounted} from 'vue'
import * as echarts from "echarts"

const scorePieRef = ref(null)
const baseOption = {
  title: {
    text: '暴雨内涝危害评价',
    left: 'center'
  },
  tooltip: {
    trigger: 'item'
  },
  series: [
    {
      name: 'Access From',
      type: 'pie',
      radius: ['40%', '70%'],
      emphasis: {
        itemStyle: {
          shadowBlur: 10,
          shadowOffsetX: 0,
          shadowColor: 'rgba(0, 0, 0, 0.5)'
        }
      }
    }
  ]
}
const dataset = {
  dimensions: ["name", "value"]
}
onMounted(async()=>{
  const chart = echarts.init(scorePieRef.value)
  const {data:res} = await fetch('/data/json/score.json').then(res=>res.json())
  chart.setOption(baseOption)
  dataset.source = res
  chart.setOption({dataset})
  window.addEventListener('resize',()=>{chart.resize()})
})
</script>

<style lang='less' scoped>

</style>
