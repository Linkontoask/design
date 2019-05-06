import Vue from 'vue'
import Homestay from './Homestay.vue'
import router from './router/index'
import store from './store/index'
import './registerServiceWorker'
import VEasy from 'v-easy-message'
import VueAwesomeSwiper from 'vue-awesome-swiper'
import 'swiper/dist/css/swiper.css'
import './style/cover.less'
Vue.use(VueAwesomeSwiper);
Vue.use(VEasy);
Vue.config.productionTip = false;

new Vue({
  router,
  store,
  render: h => h(Homestay)
}).$mount('#homeStay')
