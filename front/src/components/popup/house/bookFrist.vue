<template>
  <div class="first-book">
    <div class="time">
      <div class="info">
        <span>入住时间</span>
        <span>离开时间</span>
      </div>
      <div class="time-a">
        <span>{{ time.m + '月' + time.d + '日' }}</span>
        <div><p>共{{ p }}晚</p><div class="line"></div></div>
        <span>{{ time.m + '月' + (time.d + p) + '日' }}</span>
      </div>
    </div>
    <div class="price">
      <strong>费用明细</strong>
      <ul>
        <li v-for="(item, index) in price" :key="index">
          <span class="n">{{ item.name }}</span>
          <span class="p">￥{{ item.price }}</span>
        </li>
      </ul>
      <div>
        <span>总共</span>
        <span>￥262</span>
      </div>
    </div>
    <div class="btn" @touchend="handleGo">立即预定</div>
  </div>
</template>

<script>
  const date = new Date()
  export default {
    name: "bookFrist",
    data() {
      return {
        p: 1,
        time: {
          m: date.getMonth() + 1,
          d: date.getDate()
        },
        price: [{name: '房源费用', price: 212},{name: '清洁费', price: 30},{name: '服务费', price: 20},],
      }
    },
    methods: {
      handleGo() {
        this.$router.push({
          path: '/PopHouse/houseBook/lastBook',
          query: {
            direction: 'pop-right'
          }
        })
      }
    }
  }
</script>

<style scoped lang="less">
.first-book {
  position: relative;
  .time {
    margin-top: 36px;
    padding: 0 36px;
    > div {
      display: flex;
      align-items: center;
      justify-content: space-between;
    }
    .info {
      font-size: 14px;
    }
    .time-a {
      margin-top: 12px;
      > div {
        width: 60%;
        color: #FE5656;
        text-align: center;
        font-size: 12px;
        position: relative;
        .line {
          position: absolute;
          width: 100%;
          top: 9px;
          border-bottom: 1px solid #EBF5F1;
        }
        p {
          position: relative;
          z-index: 2;
          background-color: white;
          width: 54px;
          margin: 0 auto;
        }
      }
      span {
        font-size: 18px;
        color: #25A3A8;
      }
    }
  }
  .price {
    padding: 36px 36px 0;
    > div {
      margin-top: 16px;
      display: flex;
      align-items: center;
      justify-content: space-between;
      span:last-child {
        font-size: 18px;
        color: #EB0C0C;
      }
      span:first-child {
        font-weight: bold;
      }
    }
    strong {
      font-size: 12px;
    }
    ul {
      padding-bottom: 24px;
      border-bottom: 1px solid #E4ECE8;
    }
    li {
      display: flex;
      align-items: center;
      justify-content: space-between;
      margin-top: 16px;
    }
    .n {
    }
    .p {
      font-size: 14px;
    }
  }
  .btn {
    position: fixed;
    left: 50%;
    transform: translateX(-50%);
    bottom: 34px;
    text-align: center;
    width: calc(100% - 144px);
    background-color: #25A3A8;
    border-radius: 8px;
    color: white;
    padding: 12px 36px;
  }
}
</style>
