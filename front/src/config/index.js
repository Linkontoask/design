import Vue from 'vue'
import VEasy from 'v-easy-message'
import VueAwesomeSwiper from 'vue-awesome-swiper'
import 'swiper/dist/css/swiper.css'
import LyTab from 'ly-tab'
import '../style/cover.less'
import '../style/release.less'
import { VueHammer } from 'vue2-hammer'

Vue.use(VueHammer);
Vue.use(LyTab);
Vue.use(VueAwesomeSwiper);
Vue.use(VEasy);
