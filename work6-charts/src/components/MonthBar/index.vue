<template>
  <div ref="monthBarRef" class="chart"></div>
</template>

<script setup>
import {ref,reactive, onMounted, defineProps, toRefs, watch } from 'vue'
import * as echarts from 'echarts'

const props = defineProps({
  cityName: {
    type: String,
    default: '南京'
  }
})
const monthBarRef = ref(null)
const chart = ref(null)
const {cityName} = toRefs(props)
const cityData = ref([])
const baseOption = {
  title: {
    text: `${cityName.value}城市内涝-月份图`,
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
  xAxis: [{ type: "category", nameLocation: 'center' }],
  yAxis: [{ type: "value", name: "内涝次数"}],
  series: [
    {
      name: "内涝次数",
      type: "bar",
      itemStyle: {
        borderRadius: [5, 5, 0, 0],
        color: '#3fb1e3'
      },
    },
  ],
};
const dataset = {
  dimensions: ["month", "count"],
}
const getData = async ()=>{
  const {data} = await fetch('/data/json/cityRain.json').then(res=>res.json())
  return data
}
const getCityMonth = (name)=>{
  const {month} = cityData.value.find((item)=>item.cityName==name)
  return month.map((item,index)=>{return {month: `${index+1}月`, count: item}})
}
watch(cityName,(newValue)=>{
  baseOption.title.text = `${newValue}城市内涝-月份图`
  dataset.source = getCityMonth(newValue)
  chart.value.setOption(baseOption)
  chart.value.setOption({dataset})
})
onMounted(async()=>{
  chart.value = echarts.init(monthBarRef.value)
  cityData.value = await getData()
  chart.value.setOption(baseOption)
  dataset.source = getCityMonth(cityName.value)
  chart.value.setOption({dataset})
  window.addEventListener('resize',()=>{chart.value.resize()})
})

</script>