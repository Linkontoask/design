<template>
  <div class="svg-animation" v-if="vis">
    <div class="mask"></div>
    <icon class="animation" :svg="icon"></icon>
  </div>
</template>

<script>
  export default {
    name: "svgAnimation",
    props: {
      vis: {
        type: Boolean,
        default: false
      },
      icon: {
        type: String,
        default: ''
      }
    }
  }
</script>

<style scoped lang="less">
.svg-animation {
  position: fixed;
  left: 0;
  top: 0;
  width: 100%;
  height: 100%;
  z-index: 2001;
  .mask {
    position: fixed;
    left: 0;
    top: 0;
    width: 100vw;
    height: 100vh;
    background-color: #333;
    opacity: .8;
  }
  .animation {
    position: absolute;
    left: 50%;
    top: 50%;
    transform: translate(-50%, -50%);
    z-index: 9;
  }
}
</style>