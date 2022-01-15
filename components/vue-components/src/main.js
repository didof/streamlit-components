import { createApp } from 'vue'
import App from './App.vue'
import { createRouter, createWebHistory } from 'vue-router'
import Header from './components/Header.vue'
import HelloAuthor from './components/HelloAuthor.vue'

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
  ],
})

createApp(App).use(router).mount('#app')
