<template>
  <div class="order-list">
    <h1>订单中心</h1>
    <el-dropdown class="fixed" trigger="click" @command="handleCommand">
      <span class="el-dropdown-link">
        全部订单<i class="el-icon-arrow-down el-icon--right"></i>
      </span>
      <el-dropdown-menu slot="dropdown">
        <el-dropdown-item command="all">全部订单</el-dropdown-item>
        <el-dropdown-item command="complete">已完成订单</el-dropdown-item>
        <el-dropdown-item command="undone">未完成订单</el-dropdown-item>
      </el-dropdown-menu>
    </el-dropdown>
    <div class="order-content">
      <ul>
        <li v-for="(item, index) in orderList" :key="index">
          <h2>
            <p>{{ item.hotel_info[0].name }}</p>
            <span>{{ item.order_status === 1 ? '未支付' : '完成' }}</span>
          </h2>
          <div class="order-img" @click.stop="handleViewDetail(item.order_id)">
            <img :src="item.hotel_info[0].imgs[0]" alt="服务器错误">
            <div class="mask">
              <div class="time">
                <div>
                  <h4>{{ item.order_info.time[0] }}</h4>
                  <p>周四 10:00</p>
                </div>
                <span></span>
                <div>
                  <h4>{{ item.order_info.time[1] }}</h4>
                  <p>周五 12:00</p>
                </div>
              </div>
              <div class="price">
                <p>支付总价</p>
                <h3>￥{{ item.order_info.price }}</h3>
              </div>
            </div>
          </div>
          <div class="order-status">
            <span class="time-out" v-if="item.order_status === 1">
              <img src="../../../assets/time.png" alt="">
              <span>28分</span>后自动取消订单
            </span>
            <div class="btn plain" v-if="item.order_status === 1">联系房东</div>
            <div class="btn plain right" v-else>再次预定</div>
            <div class="btn fill" v-if="item.order_status === 1" @click="handlePay(item)">立即支付</div>
            <div class="btn plain right" v-else @click="handleEvaluation(item)">立即评价</div>
          </div>
        </li>
      </ul>
    </div>
    <confirm :vis.sync="confirmShow">
      <span>{{ content }}</span>
    </confirm>
  </div>
</template>

<script>
  import axios from '../../../utils/axios'
  import confirm from '../../base/confirm'
  export default {
    name: 'orderList',
    data() {
      return {
        orderList: [],
        confirmShow: false,
        content: ''
      }
    },
    components: {
      confirm
    },
    methods: {
      async handlePay(item) {
        const data = await axios.post.call(this, '/hotel/pay_order/', {
          order_id: item.order_id,
          price: Number(item.order_info.price)
        });
        this.confirmShow = true;
        if (data.r === 0) {
          this.content = '支付成功';
        } else {
          this.content = data.e;
        }
      },
      handleViewDetail(id) {
        this.$router.push({
          name: 'userOrderDetail',
          query: {
            order_id: id,
            bgColor: '#fff'
          }
        })
      },
      handleEvaluation(item) {
        this.$router.push({
          name: 'houseEvaluation',
          query: {
            uuid: item.order_id,
            obj_class: item.hotel_info[0].obj_class
          }
        })
      },
      handleCommand(command) {
        console.log(command)
      },
      async getData() {
        const data = await axios.get.call(this, '/hotel/get_order_form/', {});
        this.orderList = data.data;
        console.log(data)
      }
    },
    async activated() {
      this.getData()
    },
    mounted() {

    },
    async beforeMount() {
      this.getData()
    }
  }
</script>

<style scoped lang="less">
.order-list {
  position: relative;
  padding: 86px 36px 0;
  .order-content {
    ul {
      li {
        padding-bottom: 20px;
        border-bottom: 1px solid #E4ECE8;
        .order-status {
          display: flex;
          align-items: center;
          margin-top: 12px;
          .time-out {
            display: flex;
            align-items: center;
            font-size: 12px;
            img {
              width: 24px;
              margin-top: 0;
            }
          }
          .btn {
            padding: 6px 10px;
            border-radius: 4px;
            font-size: 14px;
            margin-left: auto;
          }
          .right {

          }
          .btn + .btn {
            margin-left: 10px;
          }
          .plain {
            border: 1px solid #E3E9E6;
          }
          .fill {
            background-color: #F3A825;
            color: white;
          }
        }
        .order-img {
          position: relative;
          .mask {
            position: absolute;
            bottom: 0;
            width: calc(100% - 40px);
            padding: 10px 20px;
            left: 0;
            height: 44px;
            color: white;
            border-bottom-left-radius: 4px;
            border-bottom-right-radius: 4px;
            background-color: #464646cc;
            display: flex;
            align-items: center;
            justify-content: space-between;
            .time {
              display: flex;
              justify-content: space-between;
              align-items: center;
              div {
                width: 86px;
              }
              div:last-child {
                text-align: right;
              }
              span {
                width: 20px;
                height: 1px;
                background-color: white;
                margin-top: -10px;
              }
              p {
                font-size: 12px;
              }
            }
            .price {
              width: 94px;
              text-align: right;
              border-left: 1px solid #fff;
              h3 {
                font-size: 18px;
                color: #F3A825;
              }
            }
          }
        }
        img {
          width: 100%;
          max-height: 200px;
          margin-top: 16px;
          border-radius: 4px;
          vertical-align: bottom;
        }
        h2 {
          display: flex;
          align-items: center;
          justify-content: space-between;
          font-size: 16px;
          span {
            font-size: 20px;
            color: #F38525;
          }
        }
      }
      li + li {
        margin-top: 24px;
      }
    }
  }
  h1 {
    font-size: 20px;
    color: #2E312F;
    margin-bottom: 55px;
  }
  .fixed {
    position: fixed;
    top: 24px;
    right: 36px;
  }
}
</style>
