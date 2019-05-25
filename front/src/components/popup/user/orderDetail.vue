<template>
  <div class="order-detail">
    <div class="top" :style="{backgroundImage: `url(${order.hotel_info[0].imgs[0]})`}">
      <ul style="padding-top: 98px">
        <li v-for="item in top" :key="item">
          <span></span>
        </li>
      </ul>
      <ul>
        <li v-for="item in top" :key="item">
          <p>{{ item }}</p>
        </li>
      </ul>
      <div class="btn-group">
        <div class="btn fill" v-if="order.order_status === 1" @click="handlePay">立即支付</div>
        <div class="btn" v-if="order.order_status === 2" @click="handleEvaluation">立即评价</div>
        <div class="btn plain" v-if="order.order_status === 1" @click="handleChat">联系房东</div>
        <div class="btn" v-else @click="handleAgain">再次预定</div>
      </div>
    </div>
    <div class="order-information">
      <h3>订单信息</h3>
      <div class="order-tenant" v-if="order.order_info" v-for="(item, index) in order.order_info.tenant" :key="index">
        <p>入住人姓名：<span>{{ item.name }}</span></p>
        <p>入住人身份证号：<span>{{ item.id }}</span></p>
      </div>
    </div>
    <div class="order-information" style="padding-top: 0">
      <h3>房源信息</h3>
      <div class="order-house">
        <img :src="order.hotel_info[0].imgs[0]" alt="">
        <div class="house-base">
          <div class="clamp2">{{ order.hotel_info[0].name }}</div>
          <span>{{ order.hotel_info[0].position }}</span>
        </div>
      </div>
    </div>
    <div style="margin-top: -36px">
      <Time :time="order.order_info.time" :day="p"></Time>
      <p class="price">在线支付：<strong>￥{{ order.order_info.price }}</strong><span style="font-size: 14px;margin-left: 10px">({{ order.order_status === 1 ? '未支付' : '已支付' }})</span></p>
    </div>
    <confirm :vis="confirmShow" @status="value => confirmShow = value">
      <span>{{ content }}</span>
    </confirm>
  </div>
</template>

<script>
  import axios from '../../../utils/axios'
  import Storage from '../../../utils/localStorage'
  import Time from '../../base/time'
  import confirm from '../../base/confirm'
  const date = new Date();
  export default {
    name: 'orderDetail',
    components: {
      Time,
      confirm
    },
    data() {
      return {
        p: 1,
        top: ['提交订单', '房东确认', '房客入住', '房客离开'],
        order: {
          order_info: {},
          hotel_info: [{position: '', name: '', imgs: []}]
        },
        confirmShow: false,
        content: ''
      }
    },
    computed: {
      bTime() {
        return [this.time.m + '月' + this.time.d + '日', this.time.m + '月' + (this.time.d + this.p) + '日']
      }
    },
    methods: {
      async handlePay() {
        const data = await axios.post.call(this, '/hotel/pay_order/', {
          order_id: this.order.order_id,
          price: Number(this.order.order_info.price)
        });
        this.confirmShow = true;
        if (data.r === 0) {
          this.content = '支付成功';
          this.getData()
        } else {
          this.content = data.e;
        }
      },
      handleEvaluation() {
        this.$router.push({
          name: 'houseEvaluation',
          query: {
            uuid: this.order.hotel_info[0].hotel_id,
            order_id: this.order.order_id,
            obj_class: this.order.hotel_info[0].obj_class
          }
        })
      },
      handleChat() {
        this.$router.push({
          name: 'chat'
        })
      },
      handleAgain() {
        Storage.set('now_checked_house', this.order.hotel_info[0]);
        this.$router.push({
          path: '/PopHouse/houseBook/firstBook',
          query: {
            control: 'close',
            direction: 'pop-bottom',
            price: this.order.hotel_info[0].price
          }
        })
      },
      async getData() {
        const data = await axios.get.call(this, '/hotel/get_order_form/', this.$route.query);
        this.order = data.data[0];
        console.log(this.order)
      }
    },
    mounted() {

    },
    async activated() {
      this.getData()
    },
    async beforeMount() {
      // this.getData()
    }
  }
</script>

<style scoped lang="less">
.order-detail {
  position: relative;
  .top {
    position: relative;
    width: 100%;
    height: 266px;
    background-size: 100%;
    color: white;
    &::after {
      content: "";
      width: 100%;
      height: 100%;
      position: absolute;
      left: 0;
      top: 0;
      background: inherit;
      filter: blur(2px);
      z-index: 1;
    }
    &::before {
      content: '';
      width: 100%;
      height: 100%;
      position: absolute;
      left: 0;
      top: 0;
      background-color: #484e4d;
      opacity: .4;
      z-index: 2;
    }
    ul {
      position: relative;
      z-index: 2;
      padding: 0 36px 0;
      display: flex;
      align-items: center;
      justify-content: space-between;
      li.complete {
        color: #25A3A8;
      }
      li:nth-child(-n + 3) {
        color: #FEAA56;
        span {
          background-color: #FEAA56;
        }
      }
      li:nth-child(-n + 2) {
        color: #25A3A8;
        span {
          background-color: #25A3A8;
        }
        span:after {
          background-color: #25A3A8;
        }
      }
      li:nth-child(-n + 1) {

      }
      li {
        font-size: 14px;
        display: flex;
        flex-wrap: wrap;
        justify-content: flex-start;
        p {
          width: 100%;
          text-align: center;
          margin-top: 10px;
        }
        span:after {
          content: '';
          position: absolute;
          left: 28px;
          top: 8px;
          width: 14vw;
          height: 1px;
          background-color: white;
        }
        span {
          position: relative;
          display: block;
          width: 16px;
          height: 16px;
          border-radius: 50%;
          background-color: white;
        }
      }
      li:last-child {
        span:after {
          display: none;
        }
      }
    }
    .btn-group {
      position: relative;
      padding: 36px;
      display: flex;
      align-items: center;
      z-index: 2;
      .btn {
        padding: 8px 20px;
        background-color: #4E9EDB;
        border-radius: 4px;
      }
      .btn + .btn {
        margin-left: 20px;
      }
    }
  }
  .order-information {
    padding: 24px;
    font-size: 14px;
    h3 {
      color: #2E3130;
      font-size: 18px;
      margin-bottom: 24px;
    }
    .order-tenant {
      padding-bottom: 12px;
      border-bottom: 1px solid #E3E9E6;
      p {
        color: #8F9895;
        span {
          color: #2E3130;
        }
      }
      p:first-child {
        span {
          margin-left: 30px;
        }
      }
      p + p {
        margin-top: 12px;
      }
      & + .order-tenant {
        margin-top: 24px;
      }
    }
  }
  .order-house {
    display: flex;
    align-items: center;
    justify-content: space-between;
    padding-bottom: 24px;
    border-bottom: 1px solid #E3E9E6;
    img {
      border-radius: 4px;
      width: 100px;
    }
    .house-base {
      width: 80%;
      margin-left: 20px;
    }
    .clamp2 {
      font-size: 16px;
      color: #2E3130;
    }
    span {
      display: block;
      font-size: 12px;
      color: #8F9895;
      margin-top: 12px;
    }
  }
  .price {
    padding: 24px 24px;
    strong {
      color: #EB0C0C;
    }
  }
}
</style>
