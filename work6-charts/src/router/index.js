import { createRouter, createWebHashHistory } from 'vue-router'
import Home from '../views/Home.vue'
import CityBar from '../views/CityBarView'
import Map from '../views/MapView'

const routes = [
  {
    path: '/',
    name: 'Home',
    component: Home
  },
  {path: '/cityBar', component: CityBar},
  {path: '/map', component: Map},
]

const router = createRouter({
  history: createWebHashHistory(),
  routes
})

export default router
