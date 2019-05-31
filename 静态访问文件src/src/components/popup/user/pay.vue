<template>
  <div class="user-pay">
    <h1>支付顺序</h1>
    <ul>
      <draggable v-model="pay">
        <transition-group name="fade">
          <li v-for="(item, index) in pay" :key="item.icon">
            <img :src="require('../../../assets/' + item.icon)" alt="">
            <p>{{ item.name }}</p>
            <div class="control">
              <span></span>
              <span></span>
              <span></span>
            </div>
          </li>
        </transition-group>
      </draggable>
    </ul>
  </div>
</template>

<script>
  import axios from '../../../utils/axios'
  import draggable from 'vuedraggable'
  export default {
    name: 'userPay',
    components: {
      draggable
    },
    data() {
      return {
        pay: [{name: '支付宝', icon: 'aliPay.png'},{name: '微信', icon: 'wechatPay.png'},{name: '银联', icon: 'unionpay.png'},]
      }
    },
    methods: {

    },
    mounted() {

    },
    beforeMount() {

    }
  }
</script>

<style scoped lang="less">
  .fade-move {
    transition: transform .3s;
  }
.user-pay {
  position: relative;
  padding: 86px 24px 24px;
  ul {
    li {
      display: flex;
      align-items: center;
      padding-bottom: 12px;
      border-bottom: 1px solid #E4ECE8;
      background-color: white;
      img {
        width: 32px;
      }
      p {
        margin-left: 20px;
        color: #2E312F;
      }
      div {
        margin-left: auto;
        width: 16px;
      }
      span {
        display: block;
        width: 100%;
        height: 1px;
        background-color: #5F6564;
      }
      span + span {
        margin-top: 4px;
      }
      & + li {
        margin-top: 24px;
      }
    }
  }
  h1 {
    font-size: 20px;
    color: #2E312F;
    margin-bottom: 55px;
  }
}
</style>
