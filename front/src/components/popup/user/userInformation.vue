<template>
  <div class="user-information">
    <div class="edit" @touchend="handleEdit">编辑</div>
    <div class="user-info">
      <div class="user-info-text">
        <h3>{{ user.user_name }}</h3>
        <p>加入逸宿时间：{{ user.register_time }}</p>
      </div>
      <div class="user-info-avatar" v-if="user.avatar" :style="{backgroundImage: `url(${require('../../../assets/'+user.avatar)})`}"></div>
    </div>
    <div class="box">
      <h4>我发布的故事</h4>
      <story :data="storyList"></story>
    </div>
    <div class="box">
      <h4>我发布的房源</h4>
      <House :data="houseList"></House>
    </div>
  </div>
</template>

<script>
  import Storage from '../../../utils/localStorage'
  import story from '../../base/story'
  import House from '../../base/house'
  import axios from "../../../utils/axios";
  export default {
    name: 'userInformation',
    data() {
      return {
        user: {},
        storyList: [],
        houseList: []
      }
    },
    components: {
      story,
      House
    },
    methods: {
      handleEdit() {
        this.$router.push({
          name: 'userEditInformation',
          query: {
            direction: 'pop-right'
          }
        })
      },
      async getDate() {
        const store = await axios.get.call(this, '/hotel/get_story/', {is_all: 'no'});
        const house = await axios.get.call(this, '/hotel/get_hotel/', {is_all: 'no'});
        this.storyList = store.data;
        this.houseList = house.data;
      }
    },
    mounted() {

    },
    async activated() {
      this.user = Storage.get('user_info_');
      this.getDate()
    },
    beforeMount() {

    }
  }
</script>

<style scoped lang="less">
  @import "../../../style/global";
.user-information {
  position: relative;
  padding-bottom: 36px;
  .edit {
    position: fixed;
    top: 23px;
    right: 36px;
    font-size: 14px;
    color: #2E312F;
  }
  .user-info {
    display: flex;
    align-items: center;
    justify-content: space-between;
    padding-bottom: 24px;
    width: calc(100% - 72px);
    margin: 108px - @topIndicator auto 0;
    border-bottom: 1px solid #E3E9E6;
    .user-info-text {
      h3 {
        color: #2E3130;
      }
      p {
        color: #909399;
        margin-top: 8px;
        font-size: 14px;
      }
    }
    .user-info-avatar {
      width: 64px;
      height: 64px;
      background: no-repeat center;
      border-radius: 50%;
      background-size: 110%;
    }
  }
  .box {
    padding: 0 36px;
    margin-top: 32px;
    h4 {
      font-weight: 500;
    }
  }
}
</style>
