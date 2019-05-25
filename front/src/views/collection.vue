<template>
  <div class="collection">
    <div class="none" v-if="citys.length === 0 && food.length === 0 && story.length === 0">您还没有收藏任何房源、美食或故事。快去 <a
           style="color: #25A3A8;" href="#" @click="$router.push('homeStay')">发现吧</a></div>
    <div class="collection-stay" v-if="citys.length !== 0">
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
          <div @click="handleHouseCollection(item)" class="img-content" :style="{backgroundImage: `url(${item.hotel[0].imgs[0]})`}">
          </div>
          <p class="sub">{{ item.hotel.length }} 个房源</p>
        </swiper-slide>
      </swiper>
    </div>
    <div class="collection-food" v-if="food.length !== 0">
      <h1>美食</h1>
      <img :src="food[0].belong_info[0].imgs[0]" alt="not find img" @click="handleFoodCollection">
      <p class="sub">{{food.length}} 种美食</p>
    </div>
    <div class="collection-story" v-if="story.length !== 0">
      <h1>故事</h1>
      <img :src="story[0].belong_info[0].imgs[0]" alt="not find img" @click="handleStoryCollection">
      <p class="sub">{{story.length}} 则故事</p>
    </div>
  </div>
</template>

<script>
  import axios from "../utils/axios";
  import Storage from '../utils/localStorage'
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
        citys: [],
        food: [],
        story: []
      }
    },
    methods: {
      handleHouseCollection(item) {
        Storage.set('noe_check_collection', item);
        this.$router.push({
          name: 'HouseCollection',
        })
      },
      handleFoodCollection() {
        Storage.set('noe_check_collection', this.food);
        this.$router.push({
          name: 'FoodCollection',
        })
      },
      handleStoryCollection() {
        Storage.set('noe_check_collection', this.story);
        this.$router.push({
          name: 'StoryCollection',
        })
      },
      handleNav(item, index) {
        this.$refs.city.swiper.slideTo(index, 300, false);
      },
      async getData() {
        const data = await axios.get.call(this, '/hotel/get_user_collect/', {});
        let citys = [],
          hotel = [],
          city = [],
          food = [],
          story = [];
        data.data.forEach(item => {
          if (item.belong_class === 'HotelRoom') {
            hotel.push(item.belong_info[0])
          }
          if (item.belong_class === 'AroundRegion') {
            food.push(item)
          }
          if (item.belong_class === 'StoryBoard') {
            story.push(item)
          }
        });
        hotel.forEach(item => {
          city.push({
            city: item.position.split('-')[0],
            hotel: item
          })
        });
        console.log(city)
        let hash = {};
        city.some((item, index) => {
          if (index === 0) {
            citys.push({
              city: item.city,
              hotel: [item.hotel]
            })
          } else {
            for (let i = 0; i < citys.length; i++) {
              if (citys[i].city === item.city) {
                citys[i].hotel.push(item.hotel)
                break;
              } else if (citys.every(obj => obj.city !== item.city)){
                citys.push({
                  city: item.city,
                  hotel: [item.hotel]
                })
                break;
              }
            }
          }
        });
        console.log('hash', hash)
        this.citys = citys;
        this.food = food;
        this.story = story;
        console.log(citys)
      }
    },
    mounted() {

    },
    activated() {
      this.getData();
      console.log('collection', 'keep-alive');
    }
  }
</script>

<style lang="less" scoped>
  @import "../style/global";
  .collection {
    .none {
      font-size: 20px;
      margin-top: 102px;
      padding: 0 36px;
      color: #C5D1CD;
    }
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
      padding: 0 24px;
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
          .img-content {
            height: 210px;
            background-repeat: no-repeat;
            background-position: center;
            background-size: cover;
          }
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
