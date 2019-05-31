<template>
  <div class="houseFacility">
    <h3>更多设施</h3>
    <div class="box">
      <h5>基本设施</h5>
      <ul>
        <li v-for="(item, index) in base" :key="index">
          <img :src="require('../../../assets/'+item.icon)" alt="">
          <p>{{ item.name }}</p>
        </li>
      </ul>
    </div>
    <div class="box">
      <h5>用餐</h5>
      <ul>
        <li v-for="(item, index) in food" :key="index">
          <img :src="require('../../../assets/'+item.icon)" alt="">
          <p>{{ item.name }}</p>
        </li>
      </ul>
    </div>
    <div class="box">
      <h5>娱乐</h5>
      <ul>
        <li v-for="(item, index) in happy" :key="index">
          <img :src="require('../../../assets/'+item.icon)" alt="">
          <p>{{ item.name }}</p>
        </li>
      </ul>
    </div>
    <div class="box">
      <h5>安全设施</h5>
      <ul>
        <li v-for="(item, index) in safety" :key="index">
          <img :src="require('../../../assets/'+item.icon)" alt="">
          <p>{{ item.name }}</p>
        </li>
      </ul>
    </div>
  </div>
</template>

<script>
  import Storage from '../../../utils/localStorage'
  export default {
    name: "houseFacility",
    data() {
      return {
        base: [{name: '毛巾', icon: 'towel.png'},
          {name: '空调', icon: 'air.png'},
          {name: '热水', icon: 'Hotwater.png'},
          {name: '吹风机', icon: 'hairDryer.png'},
          {name: '卫生纸', icon: 'paper.png'},
          {name: '洗衣机', icon: 'machine.png'},
          {name: '书桌', icon: 'desk.png'},
        ],
        food: [{name: '餐具', icon: 'kitchen.png'},
          {name: '电饭煲', icon: 'cooker.png'},
        ],
        happy: [{name: '电视', icon: 'tv.png'},
          {name: 'WIFI', icon: 'wifi.png'},
        ],
        safety: [{name: '灭火器', icon: 'FireExtinguisher.png'},],
        facility: []
      }
    },
    methods: {
      getStorage() {
        this.facility = Storage.get('now_checked_house').facility
      }
    },
    activated() {
      this.getStorage()
    },
    mounted() {
      // this.getStorage()
    }
  }
</script>

<style scoped lang="less">
.houseFacility {
  padding: 84px 36px 0;
  h3 {
    color: #2E3130;
  }
  .box {
    margin-top: 24px;
    padding-bottom: 24px;
    border-bottom: 1px solid #E4ECE8;
    ul {
      display: flex;
      flex-wrap: wrap;
      align-items: center;
      li {
        margin-top: 20px;
        display: flex;
        align-items: center;
        justify-content: space-around;
        flex-wrap: wrap;
        width: 24%;
        img {
          width: 24px;
        }
        p {
          width: 100%;
          text-align: center;
          font-size: 13px;
          color: #A8B2AF;
          margin-top: 4px;
        }
      }
    }
  }
}
</style>
