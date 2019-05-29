<template>
  <div class="facilityHouse">
    <h1>描述一下您的房源周边美食和景点</h1>
    <div class="titleInput new-box">
      <p>周边美食</p>
      <div class="food-img">
        <img v-for="(item, index) in checkedImgList" :key="index" :src="item" alt="服务器错误">
      </div>
      <div class="simulation-input" @click="handleCheckType(0)">
        <i v-if="!dataView.food">请选择美食</i>
        <p v-else>{{ dataView.food }}</p>
      </div>
    </div>
    <div class="titleInput new-box">
      <p>周边著名景点</p>
      <div class="simulation-input" @click="handleCheckType(1)">
        <i v-if="!dataView.attractions">请选择景点</i>
        <p v-else>{{ dataView.attractions }}</p>
      </div>
    </div>
    <div class="control-next">
      <ve-button class="primary" @click="handleNext">下一步</ve-button>
    </div>
    <list :data="lists" v-if="showList" @change="handleChange"></list>
  </div>
</template>

<script>
  import list from '../../base/list'
  import axios from 'utils/axios'
  import Storage from '../../../utils/localStorage'
  export default {
    name: 'facilityHouse',
    components: {
      list,
    },
    data() {
      return {
        dataView: {
          attractions: '',
          food: ''
        },
        data: {
          food: [],
          attractions: [],
        },
        lists: [],
        getList: {
          food: [],
          attractions: [{name: '北海', id: 0}, {name: '重庆邮电大学老校门', id: 1},],
        },
        checkedImgList: [],
        index: 0,
        showList: false,
      }
    },
    methods: {
      handleNext() {
        this.save();
        this.$router.push({
          path: '/pop/priceHouse',
          query: {
            direction: 'right',
          }
        })
      },
      handleCheckType(index) {
        this.index = index;
        if (index === 0) {
          this.lists = this.getList.food
        } else {
          this.lists = this.getList.attractions
        }
        this.showList = true;
      },
      handleChange(obj) {
        if (!obj) {
          this.showList = false;
          return
        }
        if (this.index === 0) {
          if (!this.dataView.food.includes(obj.name)) {
            this.dataView.food = ((this.dataView.food !== '' ? this.dataView.food + ',' : '') + obj.name);
          }
          if (!this.data.food.find(i => i === obj.id)) {
            this.data.food.push(obj.id);
            this.checkedImgList.push(obj.imgs[0])
          }
        } else {
          if (!this.dataView.attractions.includes(obj.name)) {
            this.dataView.attractions = ((this.dataView.attractions !== '' ? this.dataView.attractions + ',' : '') + obj.name);
          }
          if (!this.data.attractions.find(i => i === obj.id)) {
            this.data.attractions.push(obj.id);
          }
        }
        this.showList = false;
      },
      save() {
        // TODO 存储到本地
        const houseData = Storage.get('houseData');
        Storage.set('houseData', Object.assign(houseData || {}, {
          rimView: this.dataView,
          rim: this.data
        }));
      },
      async getFood() {
        const data = await axios.get.call(this, '/hotel/get_around/', {});
        this.getList.food = data.data;
      },
      async getAttractions() {
        const data = await axios.get.call(this, '/', {});
        this.getList.attractions = data.data;
      }
    },
    mounted() {
      const houseData = Storage.get('houseData') || {};
      if (houseData.rimView) {
        this.dataView = houseData.rimView;
        this.data = houseData.rim;
      }
      this.getFood()
    },
    beforeDestroy() {
      this.save();
    }
  }
</script>
