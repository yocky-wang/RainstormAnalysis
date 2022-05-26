<template>
  <div ref="cityBarRef" class="chart"></div>
</template>

<script setup>
import {ref,reactive, onMounted, defineExpose} from 'vue'
import * as echarts from 'echarts'

const cityBarRef = ref(null)
const chart = ref(null)
// const {chart} = useChartInit(cityBarRef)
const baseOption = {
  title: {
    text: "各城市内涝次数",
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
    data: ["内涝次数"],
  },
  grid: {
    left: "3%",
    right: "4%",
    bottom: "5%",
    containLabel: true,
  },
  xAxis: [{ type: "value", name: "内涝次数", nameLocation: 'center' }],
  yAxis: [{ type: "category", scale: true }],
  series: [
    {
      name: "内涝次数",
      type: "bar",
      label:{
              // color: '#000000',
              show: true,
              // formatter: (params)=>{return 1}
            },
      itemStyle: {
        borderRadius: [0, 5, 5, 0],
      },
      encode: {
        x: "count",
        y: "cityName",
      }
    },
  ],
};
const dataset = {
  dimensions: ["cityName", "count"],
  source: [
    { cityName: "name1", count: 150 },
    { cityName: "name2", count: 120 },
    { cityName: "name3", count: 100 },
    { cityName: "name4", count: 80 },
    { cityName: "name5", count: 20 },
    { cityName: "name6", count: 20 },
  ],
}
const data = ref(null)
onMounted(async()=>{
  const obj = await fetch('/data/json/walden.json').then(res=>{console.log(res);return res.json()}).then(obj=>obj)
  echarts.registerTheme('walden', obj)
  chart.value = echarts.init(cityBarRef.value, 'walden')
  chart.value.setOption(baseOption)
  chart.value.setOption({dataset})
  window.addEventListener('resize',()=>{chart.value.resize()})
})
const resize = ()=>{
    chart.value.setOption(baseOption)
    chart.value.setOption({dataset})
    chart.value.resize()
  }

defineExpose({
  resize
})
</script>

<style lang='less' scoped>

</style>
