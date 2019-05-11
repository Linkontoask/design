<template>
  <div class="user">
    <div class="user-info">
      <div class="user-info-text">
        <h3>{{ name }}</h3>
        <p>{{ user.signature }}</p>
      </div>
      <div class="user-info-avatar" :style="{backgroundImage: `url(${require('../static/img/' + user.avatar)})`}"></div>
    </div>
    <div class="user-amount">
      <div>
        <p>红包</p>
        <h4>3个</h4>
      </div>
      <div>
        <p>账户余额</p>
        <h4>￥138.6</h4>
      </div>
      <div>
        <p>积分</p>
        <h4>12分</h4>
      </div>
    </div>
    <div class="user-control">
      <ul>
        <li v-for="(item, index) in control" :key="index">
          <p>{{ item.name }}</p>
          <img :src="require('../assets/' + item.icon)" alt="not find img">
        </li>
      </ul>
    </div>
    <ve-button class="primary">退出登录</ve-button>
  </div>
</template>

<script>
  import cookie from 'utils/cookie';
  const control = [{
    name: '全部订单',
    icon: 'orders.png'
  },{
    name: '支付方式',
    icon: 'pay.png'
  },{
    name: '发布房源',
    icon: 'release-333.png'
  },{
    name: '联系客服',
    icon: 'CustomerService.png'
  },{
    name: '设置',
    icon: 'setting.png'
  },{
    name: '反馈',
    icon: 'feedback.png'
  }];
  export default {
    name: "user",
    data() {
      return {
        name: '',
        user: {
          signature: '我的个性签名',
          avatar: 'infomation.png'
        },
        control: control
      }
    },
    methods: {

    },
    mounted() {
      this.name = cookie.get('hotel_');
    },
    activated() {
      console.log('user', 'keep-alive');
    }
  }
</script>

<style scoped lang="less">
  @import "../style/global";
.user {
  padding: 0 36px;
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
