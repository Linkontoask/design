<template>
  <div class="landlord">
    <div class="user-info">
      <div class="user-info-text">
        <h3>{{ user.user_name }}</h3>
        <p>{{ user.register_time }}</p>
      </div>
      <img class="user-info-avatar" v-if="user.avatar" :src="require('../../../assets/'+user.avatar)" alt="">
    </div>
    <div class="text">
      <h1>心灵的旅行</h1>
      <div>
        这个城市
        或许陌生
        又或者熟悉

        可总有那么一个地方...</div>
    </div>
    <div class="other">
      <h3>房东的其它房源</h3>
      <house :data="houseList"></house>
    </div>
  </div>
</template>

<script>
  import house from '../../base/house'
  import axios from '../../../utils/axios'
  export default {
    name: "landlord",
    components: {
      house
    },
    data() {
      return {
        user: {},
        houseList: []
      }
    },
    methods: {
      async getData() {
        const data = await axios.get.call(this, '/hotel/user_info/', {
          user_id: this.$route.query.uuid
        });
        this.user = data.data;
        const house = await axios.get('/hotel/get_hotel/', {
          is_all: 'no',
          user_id: this.$route.query.uuid
        });
        this.houseList = house.data;
      }
    },
    async activated() {
      this.getData()
    },
    beforeMount() {

    }
  }
</script>

<style scoped lang="less">
  @import "../../../style/global";
.landlord {
  .user-info {
    display: flex;
    align-items: center;
    justify-content: space-between;
    padding-bottom: 24px;
    width: calc(100% - 72px);
    margin: 108px auto 0;
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
    }
  }
  .text {
    margin-top: 48px;
    text-align: center;
    h1 {
      font-size: 16px;
      margin-bottom: 24px;
    }
    div {
      text-align: left;
      line-height: 2;
      white-space: pre-wrap;
      padding: 0 36px;
      font-size: 14px;
    }
  }
  .other {
    padding: 48px 36px;
    h3 {
      font-size: 16px;
    }
  }
}
</style>
