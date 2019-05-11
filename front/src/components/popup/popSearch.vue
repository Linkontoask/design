<template>
  <div class="popSearch">
    <div class="search-top">
      <input type="text" @blur="handleBlur" aria-placeholder="输入城市、房源名" placeholder="输入城市、房源名">
      <div class="btn-search">搜索</div>
    </div>
    <transition name="pop-bottom">
      <router-view />
    </transition>
  </div>
</template>

<script>
  export default {
    name: "popSearch",
    methods: {
      handleBlur() {

      }
    }
  }
</script>

<style scoped lang="less">
  .search-top {
    display: flex;
    align-items: center;
    position: fixed;
    top: 64px;
    left: 50%;
    transform: translateX(-50%);
    width: 80%;
    height: 32px;
    box-shadow: 0 4px 7px 0 #e6e6e6;
    padding: 10px 20px;
    border-radius: 4px;
    background-color: white;
    z-index: 9;
    transition: top .3s;
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
</style>
