<template>  
  <div class="page-container">
    <pop-up-marker  
      v-if="popUpMarker"  
      :lat="popUpMarker.lat"  
      :lng="popUpMarker.lng" 
      :close="close" 
      :add="add"  />
    <div class="gmap" ref="gmap" :style="{height: windowHeight}" />    
  </div>
</template>

<script>
import gmapsInit from '../utils/gmaps';

export default {

  name: 'GoogleMap',

  data () {
    return {
      popUpMarker: null,
      windowHeight: window.innerHeight - 36 + 'px',
      mapStyle: {
        styles: [
            {elementType: 'geometry', stylers: [{color: '#242f3e'}]},
            {elementType: 'labels.text.stroke', stylers: [{color: '#242f3e'}]},
            {elementType: 'labels.text.fill', stylers: [{color: '#746855'}]},
            {
              featureType: 'administrative.locality',
              elementType: 'labels.text.fill',
              stylers: [{color: '#d59563'}]
            },
            {
              featureType: 'poi',
              elementType: 'labels.text.fill',
              stylers: [{color: '#d59563'}]
            },
            {
              featureType: 'poi.park',
              elementType: 'geometry',
              stylers: [{color: '#263c3f'}]
            },
            {
              featureType: 'poi.park',
              elementType: 'labels.text.fill',
              stylers: [{color: '#6b9a76'}]
            },
            {
              featureType: 'road',
              elementType: 'geometry',
              stylers: [{color: '#38414e'}]
            },
            {
              featureType: 'road',
              elementType: 'geometry.stroke',
              stylers: [{color: '#212a37'}]
            },
            {
              featureType: 'road',
              elementType: 'labels.text.fill',
              stylers: [{color: '#9ca5b3'}]
            },
            {
              featureType: 'road.highway',
              elementType: 'geometry',
              stylers: [{color: '#746855'}]
            },
            {
              featureType: 'road.highway',
              elementType: 'geometry.stroke',
              stylers: [{color: '#1f2835'}]
            },
            {
              featureType: 'road.highway',
              elementType: 'labels.text.fill',
              stylers: [{color: '#f3d19c'}]
            },
            {
              featureType: 'transit',
              elementType: 'geometry',
              stylers: [{color: '#2f3948'}]
            },
            {
              featureType: 'transit.station',
              elementType: 'labels.text.fill',
              stylers: [{color: '#d59563'}]
            },
            {
              featureType: 'water',
              elementType: 'geometry',
              stylers: [{color: '#17263c'}]
            },
            {
              featureType: 'water',
              elementType: 'labels.text.fill',
              stylers: [{color: '#515c6d'}]
            },
            {
              featureType: 'water',
              elementType: 'labels.text.stroke',
              stylers: [{color: '#17263c'}]
            }
          ]
      },
    }
  },

  props : {
    center: {
      type: String,
      default: 'Riga'
    }
  },

  async mounted() {
    // высота карты = высоте экрана
    window.onresize = () => {
      this.windowHeight = window.innerHeight + 'px'
    };
    
    try {
      const google = await gmapsInit();
      const geocoder = new google.maps.Geocoder();
      const map = new google.maps.Map(this.$refs.gmap, this.mapStyle );

      // расположить карту по центру необходимой области
      geocoder.geocode({ address: this.center }, (results, status) => {
        if (status !== 'OK' || !results[0]) {
          throw new Error(status);
        }
        map.setCenter(results[0].geometry.location);
        map.fitBounds(results[0].geometry.viewport);
      });

      // pop-up на клик
      map.addListener('click', ( e ) => {
        this.popUpMarker = {
          lat: e.latLng.lat(),
          lng: e.latLng.lng()
        }
      });
      } catch (error) {
        // eslint-disable-next-line no-console
        console.error(error);
      }
  },

  methods: {
    close () {
      this.popUpMarker = null
    },

    add () {
      this.$emit('add', this.popUpMarker);
      this.popUpMarker = null
    }
  }
};
</script>

<style scoped>

  .page-container {
    width: 100%;
    height: 100%;
  }

  .gmap {
    width: 100%;
    
  }
</style>
