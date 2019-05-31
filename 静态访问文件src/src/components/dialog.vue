<template>
  <transition name="pop-bottom">
    <div class="ve-dialog" v-if="vis">
      <div class="pop-control close" id="dialog" @click="handleClose"><p></p><p></p></div>
      <div class="dialog-content">
        <slot></slot>
      </div>
    </div>
  </transition>
</template>

<script>
  export default {
    name: "Dialog",
    props: {
      vis: {
        type: Boolean,
        default: false
      }
    },
    watch: {
      vis(val) {
        if (val) {
          document.body.style.height = '100%';
          document.body.style.overflow = 'hidden'
        } else {
          document.body.style.height = '';
          document.body.style.overflow = ''
        }
      }
    },
    methods: {
      handleClose() {
        this.$emit('close')
      }
    }
  }
</script>

<style scoped lang="less">
  .ve-dialog {
    position: fixed;
    top: 0;
    left: 0;
    width: 100%;
    height: 100vh;
    background-color: white;
    z-index: 2001;
    .dialog-content {
      margin-top: 48px;
    }
    .pop-control {
      position: absolute;
      top: 14px;
      left: 8px;
      height: 36px;
      width: 46px;
    }
    .close, .left {
      display: flex;
      justify-content: space-between;
      align-items: center;
      z-index: 9;
      p {
        position: absolute;
        left: 0;
        top: 0;
        right: 0;
        bottom: 0;
        margin: auto;
        width: 22px;
        height: 2px;
        transition: transform .2s;
        transform: rotate(45deg);
        background-color: #333;
      }
      p + p {
        transform: rotate(-45deg);
      }
    }
  }
</style>