import Vue from 'vue'
import VueRouter from 'vue-router'
import Main from '../views/Main.vue'

import axios from 'axios'

Vue.use(VueRouter, axios)

  const routes = [
  {
    path: '/',
    name: 'Main',
    component: Main
  },
  {
    path: '/regression',
    name: 'Regression',
    component: () => import('@/views/Regression')
  },
  {
    path: '/sound',
    name: 'Sound',
    component: () => import('@/views/Sound')
  },
  {
    path: '/tabular',
    name: 'Tabular',
    component: () => import('@/views/Tabular')
  },
  {
    path: '/image',
    name: 'Image',
    component: () => import('@/views/Image')
  }
]

const router = new VueRouter({
  mode: 'history',
  base: process.env.BASE_URL,
  routes
})

export default router
