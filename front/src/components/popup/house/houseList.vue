<template xmlns:v-hammer="http://www.w3.org/1999/xhtml">
  <div class="houseList">
    <h1>所有房源</h1>
    <div class="house-content">
      <houseListBase :houseList="houseList"></houseListBase>
      <div class="none" v-if="houseList.length === 0">没有已发布的房源</div>
    </div>
  </div>
</template>

<script>
  import axios from '../../../utils/axios'
  import Storage from '../../../utils/localStorage'
  import houseListBase from '../../base/houseListBase'
  export default {
    name: "houseList",
    components: {
      houseListBase
    },
    data() {
      return {
        houseList: [],
        swiperOption: {
          slidesPerView: 'auto',
          pagination: {
            el: '.swiper-paginations'
          }
        }
      }
    },
    methods: {
    },
    mounted() {

    },
    async activated() {
      const data = await axios.get.call(this, '/hotel/search_for_all', {});
      this.houseList = data.data.hotel_list;
    },
    async beforeMount() {

    }
  }
</script>

<style scoped lang="less">
.houseList {
  position: relative;
  h1 {
    font-size: 20px;
    padding: 0 36px;
    margin-top: 86px;
    color: #2E312F;
  }
  .house-content {
    padding-bottom: 36px;
    .none {
      font-size: 24px;
      text-align: center;
      line-height: 320px;
      color: #eaeaea;
    }
  }
}
</style>
