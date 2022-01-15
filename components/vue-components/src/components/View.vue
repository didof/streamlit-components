<template>
  <div :id="id">
    <h1>View: {{ name }}</h1>
  </div>
</template>

<script setup>
import { ref, unref, computed, onMounted } from 'vue'
import { Streamlit } from 'streamlit-component-lib'

const name = ref(null)

const id = computed(() => {
  const id = `__layout-view-${name.value}`

  if (name.value) {
    Streamlit.setComponentValue(unref(name))
  }

  return id
})

const onRender = event => {
  const data = event.detail
  name.value = data.args['name']

  Streamlit.setFrameHeight()
}

onMounted(() => {
  Streamlit.events.addEventListener(Streamlit.RENDER_EVENT, onRender)
  Streamlit.setComponentReady()
  Streamlit.setFrameHeight()
})
</script>
