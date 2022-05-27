<template>
  <div @dblclick="getChina" ref="mapRef" class="chart"></div>
</template>

<script setup>
import { ref, onMounted, defineEmits } from "vue"
import * as echarts from "echarts"
import {toPingyin} from "@/utils/map.js"

const mapRef = ref(null)
let chart = null
const emits = defineEmits(['getCityName'])

const baseOption = {
  title: {
    text: "三大城市群内涝事件",
    left: 20,
    top: 20,
  },
  geo: {
    type: "map",
    map: "china",
    top: "5%",
    bottom: "5%",
    //允许拖动及缩放
    roam: true,
    itemStyle: {
      // 地图的填充色
      areaColor: "#fafafa",
      borderColor: "#333",
    },
  },
  visualMap: {
    min: 0, 
    max: 40, 
    calculable: true, //显示拖拽
    inRange: {
      color: ["#c7f4ff", "#07ceff", "#1f0099"], //颜色
    },
    textStyle: {
      color: "#000",
    },
    text: ['内涝总次数']
  },
}
const dataSeries = [
  {
    type: "effectScatter",
    data: [
      //数据
      { name: "安庆", value: [117.053571, 30.524816, 13] },
      { name: "珠海", value: [113.552724, 22.255899, 10] },
      { name: "温州", value: [120.672111, 28.000575, 15] },
      { name: "舟山", value: [122.106863, 30.016028, 1] },
      { name: "佛山", value: [113.122717, 23.028762, 2] },
      { name: "香港", value: [114.177314, 22.266416, 1] },
      { name: "东莞", value: [113.760234, 23.048884, 17] },
      { name: "上海", value: [121.5447, 31.22249, 9] },
      { name: "苏州", value: [120.619585, 31.299379, 1] },
      { name: "宁波", value: [121.549792, 29.868388, 19] },
      { name: "深圳", value: [114.085947, 22.547, 20] },
      { name: "南京", value: [118.767413, 32.041544, 36] },
      { name: "广州", value: [113.280637, 23.425178, 34] },
      { name: "唐山", value: [118.175393, 39.635113, 9] },
      { name: "石家庄", value: [114.502461, 38.045474, 6] },
      { name: "天津", value: [117.190182, 39.125596, 8] },
      { name: "合肥", value: [117.283042, 31.86119, 9] },
      { name: "北京", value: [116.405285, 39.904989, 5] },
    ],
    coordinateSystem: "geo",
    label: {
      normal: {
        formatter: "{b}",
        position: "right",
        show: true,
      },
    },
  },
]
const changeMap = (chart)=>{
  chart.on("click", async (e) => {
    const provinceMapData = await fetch(`/data/map/${toPingyin(e.name)}.json`).then((res) =>
      res.json()
    )
    echarts.registerMap(`${e.name}`, provinceMapData)
    //防止错位
    chart.setOption(baseOption,true)
    chart.setOption({ series: dataSeries })
    chart.setOption({ geo: {map: `${e.name}`} })
    emits('getCityName',e.name)
  })
}
onMounted(async () => {
  const chinaMapData = await fetch("/data/map/china.json").then((res) =>
    res.json()
  )
  echarts.registerMap("china", chinaMapData)
  chart = echarts.init(mapRef.value)
  chart.setOption(baseOption)
  chart.setOption({ series: dataSeries })
  window.addEventListener('resize',()=>{chart.resize()})
  changeMap(chart)
})
//双击返回
const getChina = ()=>{
  chart.setOption({ geo: {map: `china`} })
}
</script>

<style lang='less' scoped>
</style>
