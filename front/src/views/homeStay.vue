<template xmlns:v-hammer="http://www.w3.org/1999/xhtml">
  <div class="homeStay-content" ref="homeStay">
    <transition name="show">
      <div class="search-top" :class="{focusTop: focus}" v-if="isStart">
        <input type="text" @focus="handleFocus" aria-placeholder="输入城市、房源名" placeholder="输入城市、房源名">
        <div class="btn-search">搜索</div>
      </div>
    </transition>
    <div class="content" @touchstart="handleStart" @touchend="handleEnd" @touchmove="handleMove" ref="content">
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
              <span>重庆 - 邮电大学</span>
              <div>
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
        <div class="line-primary">更多房源</div>
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
        <div class="line-primary">更多美食</div>
      </div>
      <div class="homeStay-house homeStay-food homeStay-story">
        <h2>精彩故事</h2>
        <Story :data="storyViews" style="margin-top: 12px"></Story>
        <div class="line-primary">更多故事</div>
      </div>
    </div>
  </div>
</template>

<script>
  import House from 'components/base/house'
  import Food from 'components/base/food'
  import Story from 'components/base/story'
  import house from '../static/house'
  import BScroll from 'better-scroll'
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
        return `${ date.getMonth() + 1 }.${ date.getDate() } 周${ Day[date.getDay() - 1] } - ${ date.getMonth() + 1 }.${ date.getDate()+1 } 周${ Day[date.getDay()===7?1:date.getDay()] }`
      }
    },
    data() {
      return {
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
          src: 'static/img/food-1.png',
          desc: '亚参叻沙是叻沙的一种，是马来西亚槟城的代表食物之一Asam在马来语里面有“酸”的意思，顾名思义，亚参叻沙，Asam在马来语里面有“酸”的意思，顾名思义，亚参叻沙'
        }, {
          src: 'static/img/food-2.png',
          desc: '亚参叻沙是叻沙的一种，是马来西亚槟城的代表食物之一Asam在马来语里面有“酸”的意思，顾名思义，亚参叻沙'
        }, {
          src: 'static/img/food-3.png',
          desc: '亚参叻沙是叻沙的一种，是马来西亚槟城的代表食物之一Asam在马来语里面有“酸”的意思，顾名思义，亚参叻沙'
        }],
        foodViews: [
          {
            src: 'static/img/food-1.png',
            title: '特色小龙虾',
            desc: '《韩非子·六反》：“今家人之治产也，相忍以饥寒，相强以劳苦，虽犯军旅之难，饥馑之患，温衣美食者必是家也。',
            tag: ['小吃', '美食'],
            price: 46,
            position: '鹅岭正街附近',
            d: '距您178m',
            uuid: 'xad634313443'
          },
          {
            src: 'static/img/food-2.png',
            title: '特色小龙虾',
            desc: '冬天温暖，夏天凉爽，宾至如归才是招揽顾客的秘诀。',
            tag: ['小吃'],
            price: 43,
            position: '鹅岭正街附近',
            d: '距您968m',
            uuid: 'xad634313443'
          },
          {
            src: 'static/img/food-3.png',
            title: '特色小龙虾',
            desc: '美食当前,总能有所思,或馋性千娇,食前观察、吃中思想、品后体味, 食为天性,静静地咀嚼。',
            tag: ['小吃', '美食', '特色'],
            price: 89,
            position: '鹅岭正街附近',
            d: '距您188m',
            uuid: 'xad634313443'
          },],
        storyViews: [{
          src: 'static/img/story-1.png',
          title: '广西北海 - 房源',
          desc: '重庆可以看到美丽的山水之城,犹在美丽的山水之间，看见人世繁华',
          comment: ['static/img/avatar-1.png', 'static/img/avatar-3.png'],
          extent: 78,
          uuid: 'aa154613146434154axd'
        },{
          src: 'static/img/story-2.png',
          title: '广西北海 - 房源',
          desc: '重庆可以看到美丽的山水之城,犹在美丽的山水之间，看见人世繁华',
          comment: ['static/img/avatar-3.png', 'static/img/avatar-3.png'],
          extent: 45,
          uuid: 'aa154613146434154axd'
        },{
          src: 'static/img/story-3.png',
          title: '广西北海 - 房源',
          desc: '重庆可以看到美丽的山水之城,犹在美丽的山水之间，看见人世繁华',
          comment: ['static/img/avatar-1.png', 'static/img/avatar-3.png', 'static/img/avatar-2.png'],
          extent: 25,
          uuid: 'aa154613146434154axd'
        },{
          src: 'static/img/story-1.png',
          title: '广西北海 - 房源',
          desc: '重庆可以看到美丽的山水之城,犹在美丽的山水之间，看见人世繁华',
          comment: ['static/img/avatar-1.png'],
          extent: 5,
          uuid: 'aa154613146434154axd'
        },],
        house: house,
      }
    },
    methods: {
      handleSearch() {
        this.$router.push({
          path: '/PopSearch/resultSearch',
          query: {
            params: this.searchString
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
      }
    },
    mounted() {
      this.$nextTick(() => {
        this.scroll = new BScroll(this.$refs.homeStay, {
          scrollX: false,
          scrollY: true,
          momentum: true,
          bounce: true,
        });
        this.scroll.on('scrollEnd', p => {
          if (this.isStart && -p.y < 426 && this.dir === 'up') {
            this.isStart = false;
          }
        });
      })
    },
    activated() {
      console.log('homestay', 'keep-alive');
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
    .search-top {
      display: flex;
      align-items: center;
      position: fixed;
      top: 24px;
      left: 50%;
      transform: translateX(-50%);
      width: 80%;
      height: 32px;
      box-shadow: 0 4px 7px 0 #e6e6e6;
      padding: 10px 20px;
      border-radius: 4px;
      background-color: white;
      z-index: 9;
      transition: top .3s ease-in-out;
      input {
        border: none;
        height: 100%;
        font-size: 14px;
      }
      input:focus {
        outline: none;
      }
      .btn-search {
        background-color: #25A3A8;
        color: white;
        text-align: center;
        position: absolute;
        right: 0;
        top: 0;
        width: 54px;
        height: 100%;
        line-height: 52px;
        font-size: 14px;
        border-top-right-radius: 4px;
        border-bottom-right-radius: 4px;
      }
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
