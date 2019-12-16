<template>
  <div class="pop-up-marker">
   
    <b-card 
    tag="article"
    style="max-width: 20rem;"
    class="mb-2"
  >
    <icon-close @click="close"/>
    <b-card-text>
      <p>Широта: {{lat}} </p>
      <p>Долгота: {{lng}} </p>
    </b-card-text>

    <b-button href="#" variant="primary" @click="add">Добавить локацию</b-button>
  </b-card>
  </div>
</template>

<script>
export default {
  
  props: {
    lat: {
      type: Number,
      default: 0
    },

    lng: {
      type: Number,
      default: 0
    },

    close: {
      type: Function,
      default: (ch) => {
        return ch
      }
    },

    add: {
      type: Function,
      default: (ch) => {
        return ch
      }
    }
  }
}
</script>

<style scoped lang="less">
@import "../style.less";

.pop-up-marker {
  position: absolute;
  width: 300px;
  height: 200px;
  top: 50%;
  left: 50%;
  margin: -100px 0 0 -150px;
  z-index: 100;
  background: #ffffff;
}
.icon-close {
  position: absolute;
  right: 7px;
  top: 7px;
}
</style>