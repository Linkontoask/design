<template xmlns:v-hammer="http://www.w3.org/1999/xhtml">
  <div class="popHouse">
    <div class="pop-control" :class="control" v-hammer:tap="handleTap">
      <p :style="{backgroundColor: bgColor}"></p>
      <p :style="{backgroundColor: bgColor}"></p>
    </div>
    <transition appear :name="direction">
      <keep-alive>
        <router-view />
      </keep-alive>
    </transition>
  </div>
</template>

<script>
  export default {
    name: "popHouse",
    data() {
      return {
        direction: 'pop-bottom',
        bgColor: '#2E312F',
        control: 'left'
      }
    },
    methods: {
      handleTap() {
        this.$router.back()
      },
      normalVal(to) {
        this.bgColor = to.query.bgColor || '#2E312F';
        this.direction = to.query.direction || 'pop-right';
        this.control = to.query.control || 'left';
      }
    },
    watch: {
      $route(to) {
        this.normalVal(to)
      }
    },
    computed: {

    },
    mounted() {
      this.normalVal(this.$route)
    }
  }
</script>

<style scoped lang="less">
.popHouse {
  .pop-control {
    position: relative;
    height: 56px;
    width: 46px;
    top: 18px;
  }
  .close, .left {
    display: flex;
    justify-content: space-between;
    align-items: center;
    padding: 0 36px;
    z-index: 2;
    p {
      position: absolute;
      top: 8px;
      width: 16px;
      height: 2px;
      transition: transform .2s;
      transform: rotate(45deg);
    }
    p + p {
      transform: rotate(-45deg);
    }
  }
  div.left {
    p {
      width: 14px;
      transform: rotate(-45deg);
    }
    p + p {
      transform: rotate(45deg);
      top: 17px;
    }
  }
}
</style>
