import Vue from 'vue'
import Vuex from 'vuex'
import mutations from './mutations'
import actions from './action'

Vue.use(Vuex);

const state = {
  showActionBar: true,
  beforeUrl: [],
  releaseHouse: {}, // 后期优化发布房源数据管理
  searchString: '', // 搜索字符串
  bookHouse: {}, // 预定房源信息
};

export default new Vuex.Store({
  state,
  actions,
  mutations,
})
