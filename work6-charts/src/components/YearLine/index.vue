<template>
  <div ref="yearLineRef" class="chart"></div>
</template>

<script setup>
import {ref,reactive, onMounted} from 'vue'
import * as echarts from 'echarts'

const yearLineRef = ref(null)

const baseOption = {
  title: {
    text: "城市群内涝次数年份图",
  },
  tooltip: {
    trigger: "axis",
    axisPointer: {
      label: {
        backgroundColor: "#E9EEF3",
      },
    },
  },
  legend: {
    data: ['京津冀城市群', '粤港澳城市群', '长三角城市群']
  },
  grid: {
    left: "3%",
    right: "4%",
    bottom: "5%",
    containLabel: true,
  },
  yAxis: [{ type: "value", name: "内涝次数", nameLocation: 'center' }],
  xAxis: [{ type: "category", scale: true }],
  series: [
    {
      type: "line",
      stack: 'Total',
      areaStyle: {},
      emphasis: {
        focus: 'series'
      },
    },
    {
      type: "line",
      stack: 'Total',
      areaStyle: {},
      emphasis: {
        focus: 'series'
      },
    },
    {
      type: "line",
      stack: 'Total',
      areaStyle: {},
      emphasis: {
        focus: 'series'
      },
    },
  ],
};
const dataset = {
  dimensions: ["year", "京津冀城市群", "粤港澳城市群", "长三角城市群"],
}
// data
const getYear = async ()=>{
  const data = await fetch('/data/json/yearLine.json').then(res=>res.json())
  return new Array(13).fill(0).map((item,index)=>{
    return {
      year:`${2010+index}`,
      '京津冀城市群': data['京津冀城市群'][index],
      '粤港澳城市群': data['粤港澳城市群'][index],
      '长三角城市群': data['长三角城市群'][index]
    }
  })
}
onMounted(async()=>{
  const chart = echarts.init(yearLineRef.value)
  chart.setOption(baseOption)
  dataset.source = await getYear()
  chart.setOption({dataset})
  window.addEventListener('resize',()=>{chart.resize()})
})
</script>

<style lang='less' scoped>

</style>