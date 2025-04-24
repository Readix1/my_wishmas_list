import { createRouter, createWebHistory } from 'vue-router'
import MesListes from '@/views/MesListes.vue'
import Login from '@/views/Login.vue'
import ListeDetail from '@/views/ListeDetail.vue'

const routes = [
  { path: '/', redirect: '/listes' },
  { path: '/listes', component: MesListes },
  { path: '/listes/:id', component: ListeDetail, props: true },
  { path: '/login', component: Login }
]

const router = createRouter({
  history: createWebHistory(),
  routes
})

export default router
