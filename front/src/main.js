import Vue from 'vue'
import Homestay from './Homestay.vue'
import router from './router/'
import store from './store/'
import './registerServiceWorker'
import './config/'
import './router/beforEach'
import i18n from './local/lang/index';

Vue.config.productionTip = false;

new Vue({
  i18n,
  router,
  store,
  render: h => h(Homestay)
}).$mount('#homeStay')
