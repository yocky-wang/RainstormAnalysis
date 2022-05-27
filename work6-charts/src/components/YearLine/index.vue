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
    data: ['京津冀城市群', '粤港澳大湾区城市', '长三角城市群']
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
  dimensions: ["year", "京津冀城市群", "粤港澳大湾区城市", "长三角城市群"],
  source: [
    { year: 2010, '京津冀城市群': 20, '粤港澳大湾区城市': 25, '长三角城市群': 30 },
    { year: 2011, '京津冀城市群': 20, '粤港澳大湾区城市': 35, '长三角城市群': 30 },
    { year: 2012, '京津冀城市群': 20, '粤港澳大湾区城市': 25, '长三角城市群': 30 },
    { year: 2013, '京津冀城市群': 20, '粤港澳大湾区城市': 25, '长三角城市群': 32 },
    { year: 2014, '京津冀城市群': 20, '粤港澳大湾区城市': 25, '长三角城市群': 32 },
    { year: 2015, '京津冀城市群': 10, '粤港澳大湾区城市': 15, '长三角城市群': 32 },
  ],
}
onMounted(async()=>{
  const chart = echarts.init(yearLineRef.value)
  chart.setOption(baseOption)
  chart.setOption({dataset})
  window.addEventListener('resize',()=>{chart.resize()})
})
</script>

<style lang='less' scoped>

</style>