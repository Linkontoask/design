<template>
  <div class="release">
    <h1>可发布的房屋类型</h1>
    <swiperBase :data="slides">
      <div class="mask">普通住宅</div>
    </swiperBase>
    <swiperBase :data="villa">
      <div class="mask">别墅</div>
    </swiperBase>
    <swiperBase :data="residence">
      <div class="mask">特色民居</div>
    </swiperBase>
    <div class="release-btn">
      <div>
        <span></span>
        <span></span>
      </div>
    </div>
  </div>
</template>

<script>
  import swiperBase from '../components/base/swiper'
  export default {
    name: "release",
    components: {
      swiperBase
    },
    data() {
      return {
        slides: ['banner-1.jpg', 'banner-2.jpg', 'banner-3.jpg'],
        villa: ['house-1.jpg', 'house-2.jpg', 'house-3.jpg', 'food-3.png'],
        residence: ['story-1.png', 'story-2.png', 'story-3.png'],
      }
    }
  }
</script>

<style scoped lang="less">
.release {
  padding: 0 36px;
  h1 {
    font-size: 22px;
    font-weight: 400;
    letter-spacing: 2px;
    margin-bottom: 24px;
    margin-top: 66px;
  }
  .release-btn {
    position: fixed;
    bottom: 170px;
    left: 50%;
    width: 74px;
    height: 36px;
    transform: translateX(-50%);
    background-color: #25A3A8;
    border-radius: 8px;
    box-shadow: 2px 4px 4px 0 #ababab;
    div {
      position: absolute;
      left: 50%;
      top: 50%;
      width: 22px;
      height: 22px;
      margin-left: -11px;
      margin-top: -11px;
    }
    span {
      position: absolute;
      left: 0;
      top: 8px;
      width: 22px;
      height: 6px;
      border-radius: 4px;
      background-color: white;
    }
    span:last-child {
      transform: rotate(90deg);
    }
  }
  .mask {
    position: absolute;
    left: 0;
    top: 0;
    width: 100%;
    height: 100%;
    z-index: 2;
    background-color: #333333ab;
    color: white;
    display: flex;
    align-items: center;
    justify-content: space-around;
    border-radius: 8px;
  }
}
</style>
