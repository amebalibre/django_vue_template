import Vue from 'vue'
import App from '@/App.vue'
import router from '@/router'
import '@/registerServiceWorker'

import 'bootstrap'
import 'bootstrap/dist/css/bootstrap.min.css'

// require([
//   '@/assets/style/bootstrap-4.1.3/scss/bootstrap.scss'
//
// ])
Vue.config.productionTip = false

new Vue({
  router,
  render: h => h(App)
}).$mount('#app')
