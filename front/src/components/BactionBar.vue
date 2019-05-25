<template>
  <div class="bottom-action-bar">
    <ul class="flex" :class="{qq: isQQ}">
      <li v-for="(item, index) in action" :key="index" :class="{active: $route.path.includes(item.index)}" @click="handleJump(item)">
        <img :src="require('../assets/' + ($route.path.includes(item.index) ? item.focusIcon : item.icon))" :alt="item.index">
        <h5>{{ item.title }}</h5>
      </li>
    </ul>
  </div>
</template>

<script>
  import action from '../static/BactionBar'
  import browser from '../utils/browser'
  export default {
    name: 'action',
    data() {
      return {
        action: action,
        isQQ: false
      }
    },
    watch: {

    },
    methods: {
      handleJump(item) {
        this.$router.push({
          path: item.index
        })
      }
    },
    beforeMount() {

    },
    mounted() {
      this.isQQ = !!(browser.ios && browser.qq && (screen.width === 414 || screen.width === 375) && (screen.height === 896 || screen.height === 812));
    },
    beforeCreate() {

    }
  }
</script>

<style lang="less" scoped>
  @import "../style/global";
.bottom-action-bar {
  position: fixed;
  bottom: 0;
  left: 0;
  width: 100%;
  border-top: 1px solid #E3E9E6;
  z-index: 9;
  background-color: white;
  .flex.qq {
    padding-bottom: 34px;
  }
  .flex {
    display: flex;
    justify-content: space-between;
    align-items: flex-start;
    padding: 6px 0;
    .active {
      color: #25A3A8;
    }
    img {
      width: 1.5rem;
    }
    h5 {
      text-align: center;
      margin-top: 4px;
      font-size: 0.75rem;
      font-weight: 400;
      width: 100%;
    }
    li {
      width: 20%;
      display: flex;
      align-items: center;
      justify-content: space-around;
      flex-wrap: wrap;
    }
  }
}
</style>
