<template>
  <div class='location-list' v-if="locations.length" >
    <b-list-group v-if="locations.length">
      <b-list-group-item v-for="(location, index) in locations" v-bind:key="index">
        <p><b>{{index+1}}.</b></p>
        <icon-close @click="deleteHandler(index)"/>
        Широта: {{location.lat}}
        Долгота: {{location.lng}}
        </b-list-group-item>
    </b-list-group>
    <b-button variant="outline-primary" @click="saveHandler">Сохранить</b-button>
  </div>
</template>

<script>
export default {
  props: {
    locations: {
      type: Array,
      default () {
        return []
      }
    }
  },
  

  methods: {
    saveHandler () {
      this.$emit('save')
    },
    deleteHandler (index) {
      this.$emit('delete', index)
    }
  }
 }
</script>

<style scoped lang="less">
@import "../style.less";

  .location-list {
    background: @color-grey-nav;
    position: fixed;
    top: 120px;
    left: 5px;
    max-width: 240px;
    max-height: 400px;
    text-align: left;
    z-index: 100;
    overflow: scroll;
    font-size: 13px;
    text-align: left;
    color: @color-light;
      
      .list-group-item {
        background: none;
        p {
          margin: 1px;
        }
        .icon-close {
          position: absolute;
          right: 7px;
          top: 7px;
        }
      }
      button {
        margin: 20px;
      }
    }
</style>