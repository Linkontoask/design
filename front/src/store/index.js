import Vue from 'vue'
import Vuex from 'vuex'
import mutations from './mutations'
import actions from './action'

Vue.use(Vuex);

const state = {
  showActionBar: true,
  beforeUrl: [],
  releaseHouse: {}, // 后期优化发布房源数据管理
};

export default new Vuex.Store({
  state,
  actions,
  mutations,
})
