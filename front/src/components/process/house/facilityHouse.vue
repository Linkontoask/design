<template>
  <div class="facilityHouse">
    <h1>房源设施</h1>
    <p></p>
    <Radio class="release-radio" v-for="(item, index) in radio" :checked="checkedList[index]" :i="index" type="checkbox" :key="item.id" :value="item.id" @click="value => handleCheck(index, value)">
      <h4>{{ item.name }}</h4>
      <p class="margin4" v-if="item.desc">{{ item.desc }}</p>
    </Radio>
    <div class="control-next">
      <ve-button class="primary" @click="handleNext">下一步</ve-button>
    </div>
  </div>
</template>

<script>
  import Radio from 'components/base/radio'
  import Storage from '../../../utils/localStorage'
  export default {
    name: 'facilityHouse',
    components: {
      Radio
    },
    data() {
      return {
        radio: [{
          name: '基本设施',
          desc: '毛巾、床单、洗浴用品、卫生纸和枕头',
          id: 0,
        },{
          name: '无线网络',
          desc: '在房源内免流量使用互联网',
          id: 1,
        },{
          name: '免费停车位',
          desc: '',
          id: 2,
        },{
          name: '电视',
          desc: '',
          id: 3,
        },{
          name: '暖气',
          desc: '中央暖气或房源内的暖气设备',
          id: 4,
        },{
          name: '洗衣机',
          desc: '在建筑物内，并且免费供房客使用',
          id: 5,
        },{
          name: '洗发水',
          desc: '',
          id: 6,
        },{
          name: '书桌',
          desc: '一张能放电脑的桌子或书桌，和一把舒适的椅子',
          id: 7,
        }],
        checkedList: [false, false, false, false, false, false, false, false]
      }
    },
    methods: {
      handleNext() {
        const d = this.checkedList;
        if (d.length !== 0) {
          this.save();
          this.$router.push({
            path: '/pop/rimHouse',
            query: {
              direction: 'right',
            }
          })
        } else return this.$msg({
          type: 'error',
          message: '至少勾选一种设施'
        })
      },
      handleCheck(index, value) {
        this.checkedList[index] = value;
      },
      save() {
        // TODO 存储到本地
        const houseData = Storage.get('houseData');
        Storage.set('houseData', Object.assign(houseData || {}, {
          facitity: this.checkedList
        }));
      }
    },
    mounted() {
      const houseData = Storage.get('houseData') || {};
      if (houseData.facitity) {
        this.checkedList = houseData.facitity
      }
    },
    beforeDestroy() {
      this.save();
    }
  }
</script>
