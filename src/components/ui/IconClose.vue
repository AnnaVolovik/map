<template>
  <svg
    class="icon-close"
    @click="$emit('click')"
    :width="size"
    :height="size"
    :viewBox="viewBox">
    <path d="M 19,6.41L 17.59,5L 12,10.59L 6.41,5L 5,6.41L 10.59,12L 5,17.59L 6.41,19L 12,13.41L 17.59,19L 19,17.59L 13.41,12L 19,6.41 Z "/>
  </svg>
</template>

<script>
export default {
  props: {
    size: {
      type: Number,
      default: 24
    },
    viewBox: {
      type: String,
      default: '0 0 24 24'
    }
  }
}
</script>
