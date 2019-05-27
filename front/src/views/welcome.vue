<template>
  <div class="welcome">
    <swiper :options="swiperOptionBanner" class="swiper" ref="swiper">
      <swiper-slide v-for="(item, index) in slides" :key="index">
        <div class="swiper-box">
          <img :src="require('../static/img/' + item.src)" alt="not find img">
          <img class="title" :src="require('../static/img/' + item.name)" alt="not find img" @click="next(index)">
        </div>
      </swiper-slide>
    </swiper>
    <div class="slider-bottom">
      <ul>
        <li v-for="item in [0,1,2]" :key="item" :class="{active: item === current}"></li>
      </ul>
    </div>
  </div>
</template>

<script>
  import Storage from '../utils/localStorage'
  import cookie from '../utils/cookie'
  export default {
    name: "welcome",
    data() {
      return {
        current: 0,
        swiperOptionBanner: {
          on: {
            slideChange: () => {
              this.current = this.$refs.swiper.swiper.activeIndex
            },
            touchEnd: () => {
              const swiper = this.$refs.swiper.swiper;
              console.log(swiper.swipeDirection, swiper.activeIndex)
              if (swiper.activeIndex === 2 && swiper.swipeDirection === 'next') {
                this.next()
              }
            }
          },
          pagination: {
            el: '.swiper-paginations'
          }
        },
        slides: [{name: 'welcome-text-2.png', src: 'welcome-1.jpg'},{name: 'welcome-text-1.png', src: 'welcome-2.jpg'},{name: 'welcome-text-3.png', src: 'welcome-3.jpg'},],
      }
    },
    methods: {
      next(index = 2) {
        if (index !== 2) return false;
        cookie.set('first', true, 0);
        Storage.set('first', true);
        this.$router.push({
          name: 'homeStay'
        })
      }
    },
    mounted() {

    },
  }
</script>

<style scoped lang="less">
.welcome {
  position: relative;
  width: 100vw;
  height: 100vh;
  overflow: hidden;
  .slider-bottom {
    position: absolute;
    bottom: 34px;
    left: 0;
    width: 100%;
    height: 26px;
    ul {
      position: absolute;
      left: 50%;
      top: 50%;
      width: 120px;
      height: 100%;
      transform: translate(-50%, -50%);
      text-align: center;
      li.active {
        background-color: #25A3A8;
      }
      li {
        display: inline-block;
        vertical-align: middle;
        width: 10px;
        height: 10px;
        border-radius: 50%;
        background-color: #d6e4e4;
        & + li {
          margin-left: 10px;
        }
      }
    }
  }
  .swiper {
    position: relative;
    width: 100%;
    height: 100%;
    overflow: auto;
    .swiper-box {
      position: absolute;
      top: 50%;
      transform: translateY(-50%);
    }
    .swiper-wrapper {
      position: absolute;
      left: 0;
      top: 0;
      right: 0;
      bottom: 0;
      margin: auto;
      width: 100%;
      .swiper-slide:nth-child(3) {
        .title {
          width: 164px;
          border-bottom: 1px solid #fe6b6b;
          padding-bottom: 10px;
        }
      }
      .title {
        text-align: center;
        width: 120px;
        display: block;
        margin: 2.25rem auto;
      }
      img:first-child {
        width: 100%;
      }
    }
  }
  .swiper-paginations {
    position: fixed;
    bottom: 100px;
  }
}
</style>
