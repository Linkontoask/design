<template xmlns:v-hammer="http://www.w3.org/1999/xhtml">
  <div class="houseList">
    <h1>所有房源</h1>
    <div class="house-content">
      <ul>
        <li v-for="(item, index) in houseList" :key="index" v-hammer:tap="handleTap">
          <swiper :options="swiperOption" ref="city" class="swiper-content">
            <swiper-slide v-for="(img, imgIndex) in item.imgs" :key="imgIndex">
              <div>
                <img :src="img" alt="not find img">
              </div>
            </swiper-slide>
          </swiper>
          <h4>{{ item.name }}</h4>
          <div>
            <p><span>{{ item.price }}</span> / 晚</p>
            <tag bgColor="#25A3A8" v-for="(tag, i) in item.tag" :key="i">{{ tag }}</tag>
          </div>
        </li>
      </ul>
    </div>
  </div>
</template>

<script>
  // hotel/search_for_all
  import axios from '../../../utils/axios'
  import tag from '../../base/ve-tag'
  export default {
    name: "houseList",
    components: {
      tag
    },
    data() {
      return {
        houseList: [],
        swiperOption: {
          slidesPerView: 'auto',
        }
      }
    },
    methods: {
      handleTap(item) {
        this.$router.push({
          path: '/PopHouse/houseDetail',
          query: {
            uuid: item.id
          }
        })
      }
    },
    mounted() {

    },
    async beforeMount() {
      const data = await axios.get.call(this, '/hotel/search_for_all', {});
      console.log(data)
      this.houseList = data.data.hotel_list;
    }
  }
</script>

<style scoped lang="less">
.houseList {
  position: relative;
  h1 {
    font-size: 20px;
    padding: 0 36px;
    margin-top: 36px;
    color: #2E312F;
  }
  .house-content {
    li {
      width: 80%;
      margin: 24px auto 0;
      img {
        width: 100%;
      }
    }
  }
}
</style>
