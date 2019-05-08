<template>
  <div class="swiper-base">
    <swiper :options="swiperOption">
      <swiper-slide v-for="(item, index) in data" :key="index">
        <img :src="require('../../static/img/' + item)" alt="not find img">
        <slot></slot>
      </swiper-slide>
      <div class="swiper-pagination" slot="pagination"></div>
    </swiper>
  </div>
</template>

<script>
  export default {
    name: "swiperBase",
    props: {
      data: {
        type: Array,
        default: []
      }
    },
    data() {
      return {
        swiperOption: {
          spaceBetween: 24,
          pagination: {
            el: '.swiper-pagination'
          }
        },
      }
    }
  }
</script>

<style scoped lang="less">
.swiper-base {
  position: relative;
  img {
    width: 100%;
    height: 142px;
    border-radius: 8px;
    vertical-align: bottom;
  }
  & + .swiper-base {
    margin-top: 24px;
  }
}
</style>
