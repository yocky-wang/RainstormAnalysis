import { createRouter, createWebHashHistory } from 'vue-router'
import Home from '../views/Home.vue'
import CityBar from '../views/CityBarView'

const routes = [
  {
    path: '/',
    name: 'Home',
    component: Home
  },
  {path: '/cityBar', component: CityBar}
]

const router = createRouter({
  history: createWebHashHistory(),
  routes
})

export default router
