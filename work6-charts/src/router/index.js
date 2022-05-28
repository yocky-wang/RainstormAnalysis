import { createRouter, createWebHashHistory } from 'vue-router'
import Home from '../views/Home.vue'
import CityBar from '../views/CityBarView'
import Map from '../views/MapView'
import YearLine from '../views/YearLineView'
import ScorePie from '../views/ScorePieView'
import MonthBar from '../views/MonthBarView'

const routes = [
  {
    path: '/',
    name: 'Home',
    component: Home
  },
  {path: '/cityBar', component: CityBar},
  {path: '/map', component: Map},
  {path: '/yearline', component: YearLine},
  {path: '/scorepie', component: ScorePie},
  {path: '/monthbar', component: MonthBar},
]

const router = createRouter({
  history: createWebHashHistory(),
  routes
})

export default router
