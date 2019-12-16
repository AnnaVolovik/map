import Vue from 'vue'
import BootstrapVue from 'bootstrap-vue'

import 'bootstrap/dist/css/bootstrap.css'
import 'bootstrap-vue/dist/bootstrap-vue.css'

import axios from 'axios'

import App from './App.vue'

Vue.use(BootstrapVue)

import PopUpMarker from './components/PopUpMarker.vue'
import IconClose from './components/ui/IconClose.vue'

Vue.component('pop-up-marker', PopUpMarker)
Vue.component('icon-close', IconClose)


const axiosConfig = {
  baseURL: 'http://localhost:5000',
  // json: true,
  timeout: 30000
}
const $axios = axios.create(axiosConfig)
Vue.prototype.$axios = $axios

new Vue({
  render: h => h(App),
}).$mount('#app')
