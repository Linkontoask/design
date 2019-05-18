<template>
  <div class="loading" v-if="vis">
    <div class="mask"></div>
    <div class="ball-spin-fade-loader">
      <div v-for="item in [0,1,2,3,4,5,6,7]" :key="item"></div>
    </div>
  </div>
</template>

<script>
  export default {
    name: "loading",
    props: {
      vis: {
        type: Boolean,
        default: false
      }
    },
    watch: {
      vis(val) {
        if (val) {
          document.addEventListener('touchmove', this.preventDefault, {passive: false});
        } else {
          document.removeEventListener('touchmove', this.preventDefault, {passive: false});
        }
      }
    },
    methods: {
      preventDefault(e) {
        e.preventDefault();
      },
    }
  }
</script>

<style scoped lang="less">
.loading {
  position: fixed;
  left: 0;
  top: 0;
  width: 100%;
  height: 100%;
  z-index: 2001;
  .ball-spin-fade-loader {
    position: absolute;
    left: 50%;
    top: 50%;
    transform: translate(-50%, -50%);
    z-index: 9;
  }
  .mask {
    position: fixed;
    left: 0;
    top: 0;
    width: 100vw;
    height: 100vh;
    background-color: #333;
    opacity: .8;
  }
}
</style>