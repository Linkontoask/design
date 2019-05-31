<template>
  <div class="user">
    <div class="user-info" @click="handleViewUserInformation">
      <div class="user-info-text">
        <h3>{{ user.user_name }}</h3>
        <p>{{ user.signature }}</p>
      </div>
      <div class="user-info-avatar" v-if="user.avatar" :style="{backgroundImage: `url(${require('../assets/' + user.avatar)})`}"></div>
    </div>
    <div class="user-amount">
      <div>
        <p>红包</p>
        <h4>3个</h4>
      </div>
      <div>
        <p>账户余额</p>
        <h4>￥{{ user.property }}</h4>
      </div>
      <div>
        <p>积分</p>
        <h4>{{ user.score }}分</h4>
      </div>
    </div>
    <div class="user-control">
      <ul>
        <li v-for="(item, index) in control" :key="index" @click="handleClick(item.path)">
          <p>{{ item.name }}</p>
          <img :src="require('../assets/' + item.icon)" alt="not find img">
        </li>
      </ul>
    </div>
    <Chat :showChat="showChat" name="客服" @close="close"></Chat>
  </div>
</template>

<script>
  import cookie from 'utils/cookie';
  import axios from 'utils/axios';
  import Storage from '../utils/localStorage'
  import Chat from '../components/base/chat'
  import { mapMutations} from 'vuex'

  import USER from '../static/data/user'

  const control = [{
    name: '全部订单',
    path: 'userOrderList',
    icon: 'orders.png'
  },{
    name: '支付方式',
    path: 'userPay',
    icon: 'pay.png'
  },{
    name: '发布房源',
    path: 'popNewHouse',
    icon: 'release-333.png'
  },{
    name: '我的房源',
    path: 'userInformation',
    icon: 'house-333.png'
  },{
    name: '联系客服',
    path: 'chat',
    icon: 'CustomerService.png'
  },{
    name: '设置',
    path: 'userSetting',
    icon: 'setting.png'
  },{
    name: '反馈',
    path: 'userFeedBack',
    icon: 'feedback.png'
  }];
  export default {
    name: "user",
    data() {
      return {
        showChat: false,
        user: {
          signature: '我的个性签名',
        },
        control: control
      }
    },
    components: {
      Chat
    },
    methods: {
      ...mapMutations([
        'IS_SHOW_NATION',
      ]),
      close() {
        this.showChat = false;
        this.IS_SHOW_NATION(true);
      },
      handleClick(name) {
        if (name === 'chat') {
          this.IS_SHOW_NATION(false);
          this.showChat = true;
        } else {
          this.$router.push({
            name,
            query: {
              back: this.$route.name,
              control: 'close',
              direction: 'pop-bottom'
            }
          })
        }
      },
      handleViewUserInformation() {
        this.$router.push({
          name: 'userInformation'
        })
      }
    },
    async mounted() {

    },
    async activated() {
      // const data = await axios.get.call(this, '/hotel/user_info/', {});
      Storage.set('user_info_', USER.data);
      this.user = USER.data;
      // console.log('user', 'keep-alive');
    }
  }
</script>

<style scoped lang="less">
  @import "../style/global";
.user {
  padding: 0 24px;
  .user-info {
    margin-top: 98px - @topIndicator;
    display: flex;
    align-items: center;
    justify-content: space-between;
    .user-info-text {
      h3 {
        font-weight: 500;
      }
      p {
        color: #909399;
        margin-top: 8px;
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
  .user-amount {
    margin-top: 36px;
    background-color: #25A3A8;
    height: 66px;
    padding: 24px 30px;
    border-radius: 8px;
    display: flex;
    align-items: center;
    justify-content: space-between;
    color: white;
    h4 {
      margin-top: 16px;
    }
  }
  .user-control {
    margin-top: 56px;
    ul {
      li {
        display: flex;
        justify-content: space-between;
        align-items: center;
        padding-bottom: 16px;
        border-bottom: 1px solid #E4ECE8;
        p {
          color: #606266;
        }
      }
      li ~ li {
        margin-top: 24px;
      }
    }
    img {
      width: 22px;
    }
  }
  .primary {
    margin-top: 36px;
    width: 100%;
  }
}
</style>
