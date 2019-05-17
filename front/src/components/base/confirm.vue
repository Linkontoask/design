<template>
  <transition name="ev-fade">
    <div class="ev-confirm" v-if="vis">
      <div class="ev-content-box">
        <div class="ev-content">
          <slot></slot>
        </div>
        <div class="ev-confirm-btn-group">
          <div class="cancel" @click="cancel">取消</div>
          <div class="confirm" @click="confirm">确定</div>
        </div>
      </div>
    </div>
  </transition>
</template>

<script>
  export default {
    name: "confirm",
    props: {
      vis: {
        type: Boolean,
        default: false
      }
    },
    methods: {
      cancel() {
        this.$emit('status', false)
      },
      confirm() {
        this.$emit('status', false)
      },
    }
  }
</script>

<style scoped lang="less">
.ev-fade-enter-active, .ev-fade-leave-active {
  transition: opacity .3s, transform .3s;
}
.ev-fade-enter-active {
  transform: translateY(-34px);
}
.ev-fade-leave-active {

}
.ev-fade-enter-to {
  opacity: 1;
  transform: translateY(0);
}
.ev-fade-leave-to {
  opacity: 0;
  transform: translateY(34px);
}
.ev-confirm {
  position: fixed;
  left: 0;
  top: 0;
  width: 100%;
  height: 100%;
  z-index: 2001;
  background-color: #3e3e3ec9;
  .ev-content-box {
    position: absolute;
    left: 50%;
    top: 50%;
    transform: translate(-50%, -50%);
    width: 240px;
    border-radius: 4px;
    background-color: white;
    padding: 10px 20px;
    .ev-content {
      font-weight: bold;
      padding: 10px 0;
      color: #333;
      text-align: center;
    }
    .ev-confirm-btn-group {
      > div {
        display: inline-block;
        vertical-align: middle;
        width: 50%;
        text-align: center;
        padding-top: 12px;
        border-top: 1px solid #E3E9E6;
      }
      .confirm {
        width: calc(50% - 1px);
        color: #25A3A8;
        border-left: 1px solid #E3E9E6;
      }
    }
  }
}
</style>
