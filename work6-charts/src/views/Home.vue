<template>
  <div class="main">
    <dir class="top">
      <div class="no1 view" >
        <CityBar></CityBar>
        <div class="check" @click="change('citybar')">跳转</div>
      </div>
      <div class="no2 view" >
        <div class="title">三大城市群内涝图表分析</div>
        <div class="map">
          <Map @getCityName="getCityName"></Map>
          <div class="check" @click="change('map')">跳转</div>
        </div>
      </div>
      <div class="no3 view" >
        <MonthBar :cityName="cityName"></MonthBar>
        <div class="check" @click="change('monthbar')">跳转</div>
      </div>
    </dir>
    <div class="bottom">
      <div class="no4 view">
        <YearLine></YearLine>
        <div class="check" @click="change('yearline')">跳转</div>
      </div>
      <div class="no5 view" >
        <ScorePie></ScorePie>
        <div class="check" @click="change('scorepie')">跳转</div>
      </div>
    </div>
  </div>
</template>

<script setup>
import {ref, reactive} from "vue"
import {useRouter } from 'vue-router' 
import CityBar from '@/components/CityBar'
import Map from '@/components/Map'
import MonthBar from '@/components/MonthBar'
import YearLine from '@/components/YearLine'
import ScorePie from '@/components/ScorePie'

const router = useRouter()
const cityName = ref('南京')

const change =(name)=>{
  router.push(`${name}`)
}
const getCityName = (name)=>{
  cityName.value = name
}

</script>
<style lang='less' scoped>
.main{
  height: 100%;
  max-width: 100vw;
}
.top{
  height: 60%;
  display: flex;
  justify-content: space-around;
}
.bottom{
  height: 40%;
  display: flex;
  justify-content: space-around;
}
.view{
  flex:1;
  height:100%;
  position: relative;
}
.no2{
  display: flex;
  flex-direction: column;
  justify-content: space-around;
  .title{
    line-height: 200%;
    font-weight: bold;
    flex-basis: 30px;
    background: #fff;
	  border-radius: 10px;
    box-shadow: 3px 3px 3px rgb(231, 231, 231);
  }
  .map{
    flex: 1;
    position: relative;
  }
}
.check{
  position: absolute;
  right: 20px;
  top: 20px;
}
</style>
