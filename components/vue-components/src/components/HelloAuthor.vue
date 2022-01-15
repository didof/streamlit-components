<template>
  <flippable-card :width="200" :height="150" mode="slide">
    <template #front>
      <div class="card front">Didof</div>
    </template>

    <template #back>
      <div class="card back">Francesco Di Donato</div>
    </template>
  </flippable-card>
</template>

<script setup>
import { Streamlit } from 'streamlit-component-lib'
import { ref, onMounted } from 'vue'
import FlippableCard from './FlippableCard.vue'

onMounted(() => {
  Streamlit.events.addEventListener(Streamlit.RENDER_EVENT, () => {})
  Streamlit.setComponentReady()
  Streamlit.setFrameHeight()
})
</script>

<style scoped>
.card {
  width: 100%;
  height: 100%;
  display: flex;
  justify-content: center;
  align-items: center;
}

.front {
  background: purple;
  color: whitesmoke;
}

.back {
  background: whitesmoke;
  color: purple;
}
</style>
