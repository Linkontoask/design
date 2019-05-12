<template>
  <div class="collection">
    <div class="collection-stay">
      <h1>房源</h1>
      <div class="swiper-city">
        <ly-tab
          v-model="current"
          @change="handleNav"
          :items="citys"
          :options="{labelKey: 'city', activeColor: '#25A3A8'}">
        </ly-tab>
      </div>
      <hr>
      <swiper :options="swiperOption" ref="city" class="swiper-content">
        <swiper-slide v-for="(item, index) in citys" :key="index">
          <div>
            <img :src="require('../static/img/' + item.src)" alt="not find img">
          </div>
          <p class="sub">{{ item.len }} 个房源</p>
        </swiper-slide>
      </swiper>
    </div>
    <div class="collection-food">
      <h1>美食</h1>
      <img src="../static/img/food-1.png" alt="not find img">
      <p class="sub">12 种美食</p>
    </div>
    <div class="collection-story">
      <h1>故事</h1>
      <img src="../static/img/story-1.png" alt="not find img">
      <p class="sub">1 则故事</p>
    </div>
  </div>
</template>

<script>
  export default {
    name: 'collection',
    data() {
      return {
        current: 0,
        swiperOption: {
          slidesPerView: 'auto',
          spaceBetween: 24,
          on: {
            slideChange: () => {
              this.current = this.$refs.city.swiper.activeIndex
            },
          },
        },
        citys: [
          {id: '', len: 10, src: 'house-1.jpg', city: '重庆',},
          {id: '', len: 1, src: 'house-2.jpg', city: '北京',},
          {id: '', len: 2, src: 'house-3.jpg', city: '上海',},
          {id: '', len: 24, src: 'house-2.jpg', city: '湖南',},
          {id: '', len: 12, src: 'house-3.jpg', city: '广西',},
          {id: '', len: 3, src: 'house-1.jpg', city: '广东',},
          {id: '', len: 5, src: 'house-3.jpg', city: '上海',},
          {id: '', len: 8, src: 'house-2.jpg', city: '福建',},
        ],
      }
    },
    methods: {
      handleNav(item, index) {
        this.$refs.city.swiper.slideTo(index, 300, false);
      }
    },
    mounted() {

    },
    activated() {
      console.log('collection', 'keep-alive');
    }
  }
</script>

<style lang="less" scoped>
  @import "../style/global";
  .collection {
    .sub {
      font-size: 16px;
      margin-top: 12px;
      color: #909399;
    }
    h1 {
      font-size: 22px;
      font-weight: 400;
      letter-spacing: 2px;
      margin-bottom: 24px;
    }
    .collection-stay {
      padding: 0 36px;
      margin-top: 24px;
      overflow: hidden;
      h1 {
        margin-top: 66px - @topIndicator;
      }
      hr {
        height: 1px;
        background-color: #E4ECE8;
        border: none;
        margin-top: 4px;
      }
      .swiper-city {
        font-size: 14px;
        ul {
          display: flex;
          align-items: center;
          justify-content: space-between;
          overflow-x: auto;
          .active {
            border-bottom: 4px solid #25A3A8;
          }
          li {
            width: 16%;
            flex-shrink: 0;
            text-align: center;
            color: #606266;
            padding-bottom: 8px;
          }
        }
      }
      .swiper-content {
        margin-top: 16px;
        .swiper-slide {
          > div {
            border-radius: 8px;
            overflow: hidden;
            img {
              height: 240px;
              vertical-align: bottom;
            }
          }
        }
      }
    }
    .collection-food, .collection-story {
      margin-top: 48px;
      padding: 0 36px;
      overflow: hidden;
      img {
        width: 100%;
        border-radius: 8px;
        vertical-align: bottom;
      }
    }
  }
</style>
