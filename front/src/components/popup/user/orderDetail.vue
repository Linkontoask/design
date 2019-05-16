<template>
  <div class="order-detail">
    <div class="top">
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
        <div class="btn">立即评价</div>
        <div class="btn">再次预定</div>
      </div>
    </div>
    <div class="order-information">
      <h3>订单信息</h3>
      <div class="order-tenant" v-for="(item, index) in order.tenant" :key="index">
        <p>入住人姓名：<span>{{ item.name }}</span></p>
        <p>入住人身份证号：<span>{{ item.id }}</span></p>
      </div>
    </div>
    <div class="order-information" style="padding-top: 0">
      <h3>房源信息</h3>
      <div class="order-house">
        <img src="" alt="">
        <div class="house-base">
          <div class="clamp2">{{ order.hotel.name }}</div>
          <span>{{ order.hotel.position }}</span>
        </div>
        <div class="right">
          <p></p>
          <p></p>
        </div>
      </div>
    </div>
    <div style="margin-top: -36px">
      <Time :time="bTime" :day="p"></Time>
      <p class="price">在线支付：<strong>￥{{ order.price }}</strong></p>
    </div>
  </div>
</template>

<script>
  import axios from '../../../utils/axios'
  import Time from '../../base/time'
  const date = new Date();
  export default {
    name: 'orderDetail',
    components: {
      Time
    },
    data() {
      return {
        p: 1,
        top: ['提交订单', '房东确认', '房客入住', '房客离开'],
        order: {price: '138',hotel: {name: '房源的名字，宽窄巷子、春熙路、太鼓励文殊院', position: '房源的地理位置'}, tenant: [{name: 'Link', id: '430723199708145612'}, {name: 'Link', id: '430723199708145612'}]},
        time: {
          m: date.getMonth() + 1,
          d: date.getDate()
        },
      }
    },
    computed: {
      bTime() {
        return [this.time.m + '月' + this.time.d + '日', this.time.m + '月' + (this.time.d + this.p) + '日']
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
.order-detail {
  position: relative;
  margin-top: -56px;
  .top {
    width: 100%;
    height: 266px;
    background: url("../../../assets/order.png") no-repeat;
    background-size: 100%;
    color: white;
    ul {
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
      padding: 36px;
      display: flex;
      align-items: center;
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
    padding: 36px;
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
    .right {
      p {
        width: 24px;
        height: 2px;
        background-color: #8F9895;
        transform: rotate(135deg);
        margin-top: 14px;
      }
      p:last-child {
        margin-top: -18px;
        transform: rotate(-135deg);
      }
    }
    .house-base {
      width: 80%;
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
    padding: 24px 36px;
    strong {
      color: #EB0C0C;
    }
  }
}
</style>
