import Vue from 'vue'
import VueRouter from 'vue-router'
import Home from '../views/Home.vue'
import Login from '../views/Login.vue'

Vue.use(VueRouter)

const routes = [
  {
    path: '/',
    name: 'home',
    component: Home
  },
  {
    path: '/login',
    name: 'login',
    component: Login,
    // 장고랑 다르게 뒤를 닫진 않는다.
  }
]

const router = new VueRouter({
  // 거기있는 파일을 모두 읽어들여서.
  mode: "history",
  base: process.env.BASE_URL,
  routes
})

export default router
