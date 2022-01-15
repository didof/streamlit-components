<template>
  <nav v-if="isReady">
    <ul>
      <li v-for="(tab, index) in tabs" @click="changeTab(index)">
        {{ tab }}
      </li>
    </ul>
  </nav>
  <nav v-else>Loading...</nav>
</template>

<script setup>
import { Streamlit } from 'streamlit-component-lib'
import { ref, computed, onMounted } from 'vue'

const tabs = ref([])
const isReady = ref(false)
const selectedIndex = ref(0)
const views = ref([])

const changeTab = index => {
  selectedIndex.value = index
  Streamlit.setComponentValue(tabs.value[selectedIndex.value])
}

const onRender = event => {
  const data = event.detail
  const _tabs = data.args['views']

  if (_tabs[_tabs.length - 1] != null) {
    tabs.value = _tabs
    isReady.value = true
  }

  Streamlit.setFrameHeight()
}

onMounted(() => {
  Streamlit.events.addEventListener(Streamlit.RENDER_EVENT, onRender)
  Streamlit.setComponentReady()
  Streamlit.setFrameHeight()
})
</script>

<style>
* {
  margin: 0;
  padding: 0;
}
</style>

<style scoped>
nav {
  width: 100%;
  height: 3rem;
}

ul {
  height: 100%;
  display: flex;
  justify-content: space-between;
  align-items: center;
  list-style: none;
  background-size: cover;
  background-repeat: no-repeat;
  background-image: linear-gradient(
    -45deg,
    #ff5959,
    #ff4040,
    #ff0d6e,
    #ff8033,
    #d74177
  );
  background-size: 400% 400%;
  animation: 12s myGradient infinite;
  box-shadow: 3px 3px 20px #ff3352;
}

@keyframes myGradient {
  0% {
    background-position: 0% 50%;
  }

  50% {
    background-position: 100% 50%;
  }

  100% {
    background-position: 0% 50%;
  }
}

li {
  width: 100%;
  height: 100%;
  display: flex;
  justify-content: center;
  align-items: center;
  cursor: pointer;
  color: #fff;
  text-decoration: none;
  font-family: verdana;
  font-weight: lighter;
  font-size: 24px;
}
</style>
