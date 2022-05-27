<template>
  <div ref="cityBarRef" class="chart"></div>
</template>

<script setup>
import {ref,reactive, onMounted, onUnmounted} from 'vue'
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
  xAxis: [{ type: "value", name: "内涝次数", nameLocation: 'start' }],
  yAxis: [{ type: "category", scale: true }],
  series: [
    {
      name: "内涝次数",
      type: "bar",
      label:{
              show: true,
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
}
// data
let cityData = []
const getCity = async ()=>{
  const res = await fetch('/data/json/cityRain.json').then(res=>res.json())
  cityData = res.data.map((item)=>{
    return {cityName: item.cityName, count: item.count}
  })
  .sort((a,b)=>b.count-a.count)
  return cityData.slice(0,6)
}
// loop
let timeID
const change = (chart)=>{
  const len = 6
  let i = 0
  timeID = setInterval(()=>{
    console.log(i)
    dataset.source = cityData.slice(i,i+6)
    chart.value.setOption({dataset})
    i +=6
    if(i+6>cityData.length){
      i = 0
    }  
  },2000)
}
onMounted(async()=>{
  const obj = await fetch('/data/json/walden.json').then(res=>{console.log(res);return res.json()}).then(obj=>obj)
  echarts.registerTheme('walden', obj)
  chart.value = echarts.init(cityBarRef.value, 'walden')
  chart.value.setOption(baseOption)
  dataset.source = await getCity()
  chart.value.setOption({dataset})
  change(chart)
  window.addEventListener('resize',()=>{chart.value.resize()})
})
onUnmounted(()=>{
  clearInterval(timeID)
})
</script>

<style lang='less' scoped>

</style>
