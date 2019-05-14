import {
  IS_SHOW_NATION,
  BEFORE_URL,
  SEARCH
} from './mutation-types.js'

export default {
  [IS_SHOW_NATION](state, status) {
    state.showActionBar = status;
  },
  [BEFORE_URL](state, url) {
    state.beforeUrl.push(url);
    // console.log(state.beforeUrl)
  },
  [SEARCH](state, str) {
    state.searchString = str;
  }
}
