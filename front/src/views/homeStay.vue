<template xmlns:v-hammer="http://www.w3.org/1999/xhtml">
  <div class="homeStay-content" ref="homeStay">
    <transition name="show">
      <div class="search-top" :class="{focusTop: focus}" v-if="isStart">
        <input type="text" @focus="handleFocus" aria-placeholder="输入城市、房源名" placeholder="输入城市、房源名">
        <div class="btn-search" @touchend="handleSearchGo">搜索</div>
      </div>
    </transition>
    <div class="content" :style="{paddingBottom: bottom}" @touchstart="handleStart" @touchend="handleEnd" @touchmove="handleMove" ref="content">
      <div class="homeStay-banner">
        <swiper :options="swiperOptionBanner" class="swiper">
          <swiper-slide v-for="(item, index) in slides" :key="index">
            <img :src="require('../' + item)" alt="not find img">
          </swiper-slide>
          <div class="swiper-pagination" slot="pagination"></div>
        </swiper>
        <span aria-city="地点" class="city">重庆</span>
      </div>
      <transition name="hide">
        <div class="homeStay-search" v-if="!isStart">
          <ul>
            <li>
              <img src="../assets/city-fill.png" alt="city" class="t">
              <input type="text" @blur="handleSearchBlur" v-model="searchStr">
              <div @touchend="searchStr = '重庆 - 邮电大学'">
                <span>我的附近</span>
                <img src="../assets/locat.png" alt="locat" class="s">
              </div>
            </li>
            <li>
              <img src="../assets/calender.png" alt="city" class="t">
              <strong class="day">{{ date.getDate() }}</strong>
              <span>{{ searchString }}</span>
              <div>
                <span>共一晚</span>
              </div>
            </li>
          </ul>
          <ve-button class="primary" @click="handleSearch">搜索房源</ve-button>
        </div>
        <div class="homeStay-search" style="opacity: 0;height: 136px" v-else></div>
      </transition>
      <div class="normal" ref="normal"></div>
      <div class="homeStay-house">
        <h2>热门房源</h2>
        <House :data="house" class="house-content"></House>
        <div class="line-primary" v-hammer:tap="handleMoreHouse">更多房源</div>
      </div>
      <div class="homeStay-house homeStay-food">
        <h2>热门美食</h2>
        <swiper :options="swiperOptionFood" class="swiper food-swiper">
          <swiper-slide v-for="(item, index) in foodSlider" :key="index">
            <img :src="require('../' + item.src)" alt="not find img">
            <div class="mask-food">
              <h4>推荐理由</h4>
              <div class="clamp2">{{ item.desc }}</div>
            </div>
          </swiper-slide>
        </swiper>
        <Food :data="foodViews" style="margin-top: 24px"></Food>
        <!--<div class="line-primary">更多美食</div>-->
      </div>
      <div class="homeStay-house homeStay-food homeStay-story">
        <h2>精彩故事</h2>
        <Story :data="storyViews" style="margin-top: 12px"></Story>
        <div class="line-primary">更多故事</div>
      </div>
    </div>
    <div class="bg-logo" v-show="!isStart" :style="{opacity}">
      <img src="../assets/logo.png" alt="not find img">
    </div>
  </div>
</template>

<script>
  import House from 'components/base/house'
  import Food from 'components/base/food'
  import Story from 'components/base/story'
  import BScroll from 'better-scroll'
  import axios from "../utils/axios";
  import browser from '../utils/browser'
  let y = 0;
  const Day =  ['一','二','三','四','五','六','日'];
  export default {
    name: 'homeStayContent',
    components: {
      House,
      Food,
      Story
    },
    computed: {
      searchString() {
        const date = this.date;
        return `${ date.getMonth() + 1 }.${ date.getDate() } 周${ Day[date.getDay() === 0 ? 6 : date.getDay() - 1] } - ${ date.getMonth() + 1 }.${ date.getDate()+1 } 周${ Day[date.getDay()] }`
      }
    },
    data() {
      return {
        bottom: '118px',
        searchStr: '上海',
        opacity: 0.1,
        focus: false,
        dir: 'down',
        Day: Day,
        isStart: false,
        date: new Date(),
        swiperOptionBanner: {
          loop: true,
          autoplay: {
            delay: 4900,
            disableOnInteraction: false
          },
          pagination: {
            el: '.swiper-pagination'
          }
        },
        swiperOptionFood: {
          slidesPerView: 'auto',
          spaceBetween: 30,
        },
        slides: ['static/img/banner-1.jpg', 'static/img/banner-2.jpg', 'static/img/banner-3.jpg'],
        foodSlider: [{
          src: 'static/img/food-1.jpg',
          desc: '亚参叻沙是叻沙的一种，是马来西亚槟城的代表食物之一Asam在马来语里面有“酸”的意思，顾名思义，亚参叻沙，Asam在马来语里面有“酸”的意思，顾名思义，亚参叻沙'
        }, {
          src: 'static/img/food-2.jpg',
          desc: '亚参叻沙是叻沙的一种，是马来西亚槟城的代表食物之一Asam在马来语里面有“酸”的意思，顾名思义，亚参叻沙'
        }, {
          src: 'static/img/food-3.jpg',
          desc: '亚参叻沙是叻沙的一种，是马来西亚槟城的代表食物之一Asam在马来语里面有“酸”的意思，顾名思义，亚参叻沙'
        }],
        foodViews: [],
        storyViews: [],
        house: [],
      }
    },
    methods: {
      handleSearchBlur() {
        this.scroll && this.scroll.refresh();
      },
      handleMoreHouse() {
        this.$router.push({
          path: '/PopHouse/houseList'
        })
      },
      handleSearchGo() {
        this.focus = true;
        setTimeout(() => {
          this.$router.push({
            path: '/PopSearch'
          })
        }, 300)
      },
      handleSearch() {
        this.$router.push({
          path: '/PopSearch/resultSearch',
          query: {
            params: this.searchStr
          }
        })
      },
      handleFocus() {
        this.focus = true;
        setTimeout(() => {
          this.$router.push({
            path: '/PopSearch'
          })
        }, 300)
      },
      handleStart(ev) {
        y = Math.floor(this.$refs.content.getBoundingClientRect().y);
      },
      handleEnd(ev) {
        let top = Math.floor(this.$refs.content.getBoundingClientRect().y);
        this.dir = top > y ? 'up' : 'down';
        if (top !== y && this.dir === 'down' && -top < 426) {
          this.isStart = true;
          this.scroll.scrollToElement(this.$refs.normal, 300, 'ease')
        } else if (-top < 426) {
          this.isStart = false;
        }
      },
      handleMove(e) {
        e.preventDefault();
      },
      async getData() {
        const food = await axios.get.call(this, '/hotel/get_around/', {is_all: 'yes'});
        const house = await axios.get.call(this, '/hotel/get_hotel/', {is_all: 'yes'});
        const story = await axios.get.call(this, '/hotel/get_story/', {is_all: 'yes'});
        this.storyViews = story.data.slice(0, 8);
        this.foodViews = food.data.slice(0, 4);
        this.house = house.data.slice(0, 6);
      }
    },
    async beforeMount() {
      // this.getData();
    },
    async mounted() {
      /*alert(browser.qq)
      if (!browser.weChat) {
        this.bottom = '236px'
      }*/
      if (browser.uc) {
        this.bottom = '118px'
      }
      this.$nextTick(() => {
        this.scroll = new BScroll(this.$refs.homeStay, {
          scrollX: false,
          scrollY: true,
          momentum: true,
          bounce: true,
          probeType: 3
        });
        this.scroll.on('scroll', p => {
          let y = Math.floor(p.y);
          if (y >= 24) {
            // 性能优化
            setTimeout(() => {
              this.opacity = 1 - ((100 - y) / 100).toFixed(2);
            }, 0)
          }
          if (this.isStart && -p.y < 426 && this.dir === 'up') {
            this.isStart = false;
          }
          if (-p.y > 426) {
            this.isStart = true;
          }
        })
      })
    },
    async activated() {
      this.getData();
      this.scroll && this.scroll.refresh();
      this.isStart = -this.$refs.content.getBoundingClientRect().y >= 426;
      this.focus = false;
    }
  }
</script>

<style lang="less" scoped>
  @import "../style/global";
  .show-enter-active, .show-leave-active {
    transition: opacity .3s, width .3s;
  }
  .hide-enter-active {
    max-height: 0;
    padding: 0 !important;
    opacity: 0
  }
  .hide-leave-active {
    max-height: 134px;
    opacity: 1;
  }
  .hide-leave-to {
    max-height: 0;
    opacity: 0;
  }
  .hide-enter-to {
    max-height: 134px;
    padding: 24px 40px !important;
    opacity: 1;
  }
  .show-enter-active {
    width: 0 !important;
    opacity: 0
  }
  .show-leave-active {
    width: 80% !important;
    opacity: 1;
  }
  .show-leave-to {
    width: 0 !important;
    opacity: 0;
  }
  .show-enter-to {
    width: 80% !important;
    opacity: 1;
  }
  .homeStay-content {
    height: 100vh;
    .bg-logo {
      position: fixed;
      top: 0;
      width: 100%;
      z-index: -1;
      img {
        display: block;
        width: 64px;
        margin: 24px auto 0;
      }
    }
    .content {
      padding-bottom: 96px;
    }
    .homeStay-banner {
      position: relative;
      .swiper {
        height: 20.125rem;
        img {
          height: 100%;
        }
      }
      .city {
        position: absolute;
        left: 2rem;
        top: 2.75rem;
        color: white;
        font-size: 0.875rem;
        letter-spacing: 2px;
        z-index: 1;
      }
    }
    .normal {
      position: absolute;
      top: 426px;
    }
    div.focusTop {
      top: 64px;
    }
    .homeStay-search {
      position: relative;
      margin: -10px auto 0;
      width: 262px;
      transition: max-height .3s, opacity .3s, padding .3s;
      padding: 24px 40px;
      border-radius: 12px;
      box-shadow: 0 3px 4px rgba(59, 59, 59, 0.16);
      border: 1px solid #E4ECE8;
      background-color: white;
      overflow: hidden;
      z-index: 4;
      input {
        border: none;
        height: 26px;
        width: 140px;
        margin-left: 10px;
        color: #5F6564;
        font-size: 14px;
      }
      input:focus {
        outline: none;
      }
      ul {
        padding: 0;
        li {
          position: relative;
          display: flex;
          align-items: center;
          height: 26px;
          font-size: 14px;
          border-bottom: 1px solid #E4ECE8;
          .day {
            position: absolute;
            left: 0;
            top: 8px;
            width: 20px;
            text-align: center;
            font-size: 12px;
            color: #25A3A8;
          }
          > span {
            display: inline-block;
            margin-left: 10px;
          }
          > div {
            display: flex;
            align-items: center;
            margin-left: auto;
            font-size: 10px;
            color: #8F9895;
            span {
              display: inline-block;
              margin-right: 10px;
            }
          }
          .t {
            width: 20px;
          }
          .s {
            width: 16px;
          }
        }
        li + li {
          margin-top: 22px;
        }
      }
      .primary {
        margin-top: 18px;
        height: 42px;
        line-height: 42px;
      }
    }
    .homeStay-house {
      margin-top: 56px;
      padding: 0 24px;
      .house-content {
        margin-top: 0.75rem;
      }
      h2 {
        font-size: 20px;
        color: #2E3130;
        font-weight: 500;
      }
      .swiper {
        height: 230px;
        margin-left: -24px;
        margin-top: 24px;
        .mask-food {
          position: absolute;
          width: calc(100% - 16px);
          height: 62px;
          bottom: 0;
          background: rgba(43, 43, 43, 0.53);
          border-radius: 0 0 8px 8px;
          color: white;
          padding: 8px;
          h4 {
            font-size: 14px;
          }
          div {
            font-size: 12px;
            margin-top: 8px;
          }
        }
        img {
          width: 100%;
          height: 100%;
          border-radius: 8px;
        }
      }
      .food-swiper {
        width: calc(100% + 48px);
        .wc-slide {
          width: 90%;
          margin-left: 20px;
        }
      }
    }
  }


</style>
