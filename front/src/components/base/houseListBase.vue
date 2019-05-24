<template>
  <div class="house-list-base">
    <ul v-if="houseList.length !== 0">
      <li v-for="(item, index) in houseList" :key="index" @click="handleTap(item)" class="animated bounceInUp fast-time" :class="'delay-'+ (index * 600) + 'ms'">
        <swiper :options="swiperOption" ref="city" class="swiper-content">
          <swiper-slide v-for="(img, imgIndex) in item.imgs" :key="imgIndex">
            <div class="img-content" :style="{backgroundImage: `url(${img})`}"></div>
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
  </div>
</template>

<script>
  import Storage from '../../utils/localStorage'
  import tag from './ve-tag'
  export default {
    name: "houseListBase",
    components: {
      tag
    },
    props: {
      houseList: {
        type: Array,
        default: () => []
      }
    },
    data() {
      return {
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
    }
  }
</script>

<style scoped lang="less">
.house-list-base {
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
    .swiper-content {
      height: 210px;
      .img-content {
        height: 100%;
        background-repeat: no-repeat;
        background-position: center;
        background-size: cover;
      }
    }
  }
}
</style>
