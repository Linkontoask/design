<template>
  <div class="setting">
    <h1>设置</h1>
    <div>
      <ul>
        <li v-for="(item, index) in list" :key="index" @touchend="handleViewList(index)">
          <p>{{ item.name }}</p>
          <span>{{ item.result }}</span>
        </li>
      </ul>
    </div>
    <ve-button class="primary" @click="handleOut">退出登录</ve-button>
    <List :data="listView.lists" v-if="listView.showList" @change="handleChange"></List>
  </div>
</template>

<script>
  import axios from '../../../utils/axios'
  import cookie from '../../../utils/cookie'
  import Storage from '../../../utils/localStorage'
  import List from '../../base/list'
  export default {
    name: 'setting',
    components: {
      List
    },
    data() {
      return {
        list: [{name: '通知', result: '关', id: 0},{name: '语言', result: '中文', id: 1},],
        notice: [{name: '开'},{name: '关'},],
        language: [{name: '中文'},{name: '英语'},{name: '法语'},{name: '西班牙语'},],
        check: 0,
        listView: {
          lists: [],
          showList: false
        }
      }
    },
    methods: {
      handleViewList(index) {
        this.check = index;
        if (index === 0) {
          this.listView.lists = this.notice
        } else {
          this.listView.lists = this.language
        }
        this.listView.showList = true
      },
      handleChange(value) {
        this.listView.showList = false;
        this.list[this.check].result = value.name
      },
      async handleOut() {
        cookie.remove('hotel_');
        Storage.remove('houseData');
        Storage.remove('now_checked_house');
        Storage.remove('before_url_house_');
        Storage.remove('popHouse_before');
        Storage.remove('user_info_');
        this.$router.push({name: 'login'});
        const data = await axios.get.call(this, '/hotel/login_out/', {});
        this.$msg({
          type: 'success',
          message: data.e
        });
      }
    },
    mounted() {

    },
    beforeMount() {

    }
  }
</script>

<style scoped lang="less">
.setting {
  position: relative;
  padding: 24px 36px;
  h1 {
    font-size: 20px;
    color: #2E312F;
    margin-bottom: 55px;
  }
  .primary {
    float: none;
    width: 100%;
  }
  ul {
    padding-bottom: 36px;
    li {
      display: flex;
      align-items: center;
      justify-content: space-between;
      padding-bottom: 12px;
      border-bottom: 1px solid #E4ECE8;
      span {
        color: #A0ABA9;
        font-weight: lighter;
      }
      & + li {
        margin-top: 24px;
      }
    }
  }
}
</style>
