import {
  IS_SHOW_NATION,
  BEFORE_URL,
  SEARCH,
  BOOK_HOUSE
} from './mutation-types.js'
import Storage from '../utils/localStorage'


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
  },
  [BOOK_HOUSE](state, houseInfor) {
    let json = Storage.get('book_house_') || {};
    Object.assign(json, houseInfor);
    for (const [key,value] of Object.entries(json)) {
      state.bookHouse[key] = value
    }
    Storage.set('book_house_', state.bookHouse)
  }
}
