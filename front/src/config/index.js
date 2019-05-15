import Vue from 'vue'
import VEasy from 'v-easy-message'
import VueAwesomeSwiper from 'vue-awesome-swiper'
import 'swiper/dist/css/swiper.css'
import LyTab from 'ly-tab'
import { VueHammer } from 'vue2-hammer'
import {
  Upload,
  Dialog,
  Dropdown,
  DropdownMenu,
  DropdownItem,
} from 'element-ui'
import '../style/cover.less'
import '../style/release.less'
import '../style/animation.less'

Vue.use(VueHammer);
Vue.use(LyTab);
Vue.use(VueAwesomeSwiper);
Vue.use(VEasy);
Vue.use(Dialog);
Vue.use(Upload);
Vue.use(Dropdown);
Vue.use(DropdownMenu);
Vue.use(DropdownItem);
