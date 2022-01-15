import { createApp } from 'vue'
import App from './App.vue'
import { createRouter, createWebHistory } from 'vue-router'
import Layout from './components/Layout.vue'
import HelloAuthor from './components/HelloAuthor.vue'
import View from './components/View.vue'

const router = createRouter({
  history: createWebHistory(),
  routes: [
    {
      path: '/',
      component: HelloAuthor,
    },
    {
      path: '/layout',
      component: Layout,
    },
    {
      path: '/layout/view',
      component: View,
    },
  ],
})

createApp(App).use(router).mount('#app')
