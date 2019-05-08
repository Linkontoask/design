import Vue from 'vue'
import Homestay from './Homestay.vue'
import router from './router/index'
import store from './store/index'
import './registerServiceWorker'
import VEasy from 'v-easy-message'
import VueAwesomeSwiper from 'vue-awesome-swiper'
import 'swiper/dist/css/swiper.css'
import LyTab from 'ly-tab'
import './style/cover.less'
import { VueHammer } from 'vue2-hammer'
VueHammer.config.swipe = {
};
Vue.use(VueHammer, {
  config: {
    swipe: {
      direction: ['DIRECTION_LEFT', 'DIRECTION_RIGHT'],
    }
  }
})

Vue.use(LyTab);
Vue.use(VueAwesomeSwiper);
Vue.use(VEasy);
Vue.config.productionTip = false;

new Vue({
  router,
  store,
  render: h => h(Homestay)
}).$mount('#homeStay')
