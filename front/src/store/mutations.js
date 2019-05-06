import {
  IS_SHOW_NATION
} from './mutation-types.js'

export default {
  [IS_SHOW_NATION](state, status) {
    state.showActionBar = status;
  }
}
