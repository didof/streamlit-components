import { createApp } from 'vue'
import App from './App.vue'
import { createRouter, createWebHistory } from 'vue-router'
import Header from './components/Header.vue'
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
      path: '/header',
      component: Header,
    },
    {
      path: '/header/view',
      component: View,
    },
  ],
})

createApp(App).use(router).mount('#app')
