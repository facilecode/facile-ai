import Vue from 'vue'
import VueRouter from 'vue-router'
import Home from '../views/Home.vue'
import Regression from '../views/Regression.vue'
import Sound from '../views/Sound.vue'
import Image from '../views/Image.vue'
import Classification from '../views/Classification.vue'

import axios from 'axios'

Vue.use(VueRouter, axios)

  const routes = [
  {
    path: '/',
    name: 'Home',
    component: Home
  },
  {
    path: '/Regression',
    name: 'Regression',
    view: Regression.Vue
  },
  {
    path: '/Sound',
    name: 'Sound',
    view: Sound.Vue
  },
  {
    path: '/Image',
    name: 'Image',
    view: Image.Vue
  },
  {
    path: '/Classification',
    name: 'Classification',
    view: Classification.Vue
  }
]

const router = new VueRouter({
  mode: 'history',
  base: process.env.BASE_URL,
  routes
})

export default router
