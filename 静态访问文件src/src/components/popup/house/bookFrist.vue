<template>
  <div class="first-book">
    <Time :time="bTime" @change="handleChange"></Time>
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
        <span>￥{{priceAll}}</span>
      </div>
    </div>
    <div class="btn" @touchend="handleGo">继续完成预定</div>
  </div>
</template>

<script>
  import {mapState, mapMutations} from 'vuex'
  import Time from '../../base/time'
  const date = new Date();
  export default {
    name: "bookFrist",
    components: {
      Time
    },
    data() {
      const time = {
        m: date.getMonth() + 1,
        d: date.getDate()
      };
      return {
        bTime: [time.m + '月' + time.d + '日', time.m + '月' + (time.d + 1) + '日'],
        priceAll: '',
        price: [{name: '房源费用', price: 212},{name: '清洁费', price: 30},{name: '服务费', price: 20},],
      }
    },
    computed: {
    },
    methods: {
      ...mapMutations([
        'BOOK_HOUSE'
      ]),
      handleChange(time, current) {
        this.bTime = time;
        console.log(Number(current.match(/\d+/)[0]))
      },
      handleGo() {
        this.BOOK_HOUSE({
          time: this.bTime
        });
        this.$router.push({
          path: '/PopHouse/houseBook/lastBook',
          query: {
            direction: 'pop-right',
            is_check: '430723xxxxxxxx0124'
          }
        })
      },
      update() {
        this.priceAll = this.$route.query.price;
        this.$set(this.price, 0, {name: '房源费用', price: this.priceAll - 50})
      }
    },
    activated() {
      this.update()
    },
    beforeMount() {
      this.update()
    }
  }
</script>

<style scoped lang="less">
.first-book {
  position: relative;
  .price {
    padding: 36px 24px 0;
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
