<template>
  <div
    class="scene"
    :style="{
      width: width + 'px',
      height: height + 'px',
    }"
    @mouseenter="flip"
    @mouseleave="flip"
  >
    <div class="card" :class="isFlipped && 'is-flipped'">
      <div class="card-face"><slot name="front" /></div>
      <div class="card-face back"><slot name="back" /></div>
    </div>
  </div>
</template>

<script setup>
import { ref, toRefs, computed, readonly } from 'vue'

const props = defineProps({
  width: Number,
  height: Number,
})
const emit = defineEmits(['flip', 'show:front', 'show:back'])

const { width, height } = toRefs(props)
const isFlipped = ref(false)

function flip() {
  isFlipped.value = !isFlipped.value
  emit('flip')
  isFlipped.value ? emit('show:front') : emit('show:back')
}

defineExpose({
  flip,
  isFlipped: readonly(isFlipped),
})
</script>

<style scoped>
.scene {
  perspective: 600px;
  cursor: pointer;
}

.card {
  width: 100%;
  height: 100%;
  position: relative;
  transition: transform 1s;
  transform-style: preserve-3d;
}

.card-face {
  position: absolute;
  height: 100%;
  width: 100%;
  backface-visibility: hidden;
  display: flex;
  justify-content: center;
  align-items: center;
}

.back {
  transform: rotateY(180deg);
}

.is-flipped {
  transform: rotateY(180deg);
}
</style>
