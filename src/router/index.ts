import { createRouter, createWebHistory } from 'vue-router'
import ResultsViewVue from '../views/ResultsView.vue'
const router = createRouter({
  history: createWebHistory(import.meta.env.BASE_URL),
  routes: [
    { path: '/', name: 'results', component: ResultsViewVue },
    {
      path: '/:catchAll(.*)',
      redirect: '/'
    }
  ]
})

export default router
