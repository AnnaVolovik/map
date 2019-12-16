<template>
  <div id="app">
    <Header />
    <LocationList 
      :locations="markers" 
      v-on:save="saveMarkers"
      v-on:delete="deleteMarker($event)" />
    <GoogleMap v-on:add="addMarker"/>
  </div>
</template>

<script>

import Header from './components/Header.vue'
import LocationList from './components/LocationList.vue'
import GoogleMap from './components/GoogleMap.vue'

export default {
  name: 'app',
  components: {
    Header,
    LocationList,
    GoogleMap
  },

  data () {
    return {
      markers: [],
    }
  },

  mounted() {
    this.getLocations()
  },

  methods : {
    getLocations() {
      this.$axios.get('/')
        .then(response => {
          this.markers = response.data.data
        })
        .catch(err => {
          console.log(err)
        })
    },

    addMarker (item) {
      this.markers.push(item)
    },

    deleteMarker (index) {
      this.markers.splice(index, 1)
    },

    saveMarkers() {
      this.$axios.post('/update', this.markers)
        .then(response => {
          this.markers = response.data.data
        })
        .catch(err => {
          console.log(err)
        })
    }
  }
}
</script>

<style lang="less">
@import "./style.less";

#app {
  display: flex;
  flex-direction: column;
  font-family:"Helvetica Neue", Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;  
}

</style>
