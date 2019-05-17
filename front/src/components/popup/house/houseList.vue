<template xmlns:v-hammer="http://www.w3.org/1999/xhtml">
  <div class="houseList">
    <h1>所有房源</h1>
    <div class="house-content">
      <ul v-if="houseList.length !== 0">
        <li v-for="(item, index) in houseList" :key="index" @click="handleTap(item)">
          <swiper :options="swiperOption" ref="city" class="swiper-content">
            <swiper-slide v-for="(img, imgIndex) in item.imgs" :key="imgIndex">
              <div>
                <img :src="img" alt="not find img">
              </div>
            </swiper-slide>
            <div class="swiper-paginations" slot="pagination"></div>
          </swiper>
          <h4 class="clamp2">{{ item.name }}</h4>
          <div>
            <p><span>￥{{ item.price }}</span> / 晚</p>
            <tag style="margin-top: 8px" bgColor="#25A3A8" v-for="(tag, i) in item.tag.split('|')" :key="i">{{ tag }}</tag>
          </div>
        </li>
      </ul>
      <div class="none" v-else>没有已发布的房源</div>
    </div>
  </div>
</template>

<script>
  // hotel/search_for_all
  import axios from '../../../utils/axios'
  import Storage from '../../../utils/localStorage'
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
          pagination: {
            el: '.swiper-paginations'
          }
        }
      }
    },
    methods: {
      handleTap(item) {
        Storage.set('now_checked_house', item);
        this.$router.push({
          path: '/PopHouse/houseDetail',
          query: {
            bgColor: '#fff',
            direction: 'pop-right',
            id: item.hotel_id
          }
        })
      }
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
    li {
      width: 80%;
      margin: 36px auto 0;
      h4 {
        margin-top: 8px;
        margin-bottom: 8px;
      }
      img {
        width: 100%;
        border-radius: 4px;
        vertical-align: bottom;
      }
      span {
        color: #EB0C0C;
      }
    }
    .none {
      font-size: 24px;
      text-align: center;
      line-height: 320px;
      color: #eaeaea;
    }
  }
}
</style>
