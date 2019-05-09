<template>
  <label :for="'radio' + i" class="ve-radio" @touchend="handleTouchEnd">
    <input type="radio" :id="'radio' + i" :value="value" name="ve-radio">
    <div class="ve-label">
      <slot></slot>
    </div>
  </label>
</template>

<script>
  export default {
    name: "radio",
    data() {
      return {
        value: ''
      }
    },
    props: {
      i: {
        type: Number,
        default: 0
      }
    },
    methods: {
      handleTouchEnd() {
        this.$emit('click', this.value)
      }
    }
  }
</script>

<style scoped lang="less">
  @keyframes scale-in {
    100% {
      transform: scale(1);
    }
  }
  .ve-radio {
    display: flex;
    align-items: center;
    input[type="radio"] {
      position: relative;
      margin-left: 4px;
      margin-top: 4px;
      &:checked::before {
        content: '';
        display: block;
        position: absolute;
        left: 0;
        top: 0;
        width: 16px;
        height: 16px;
        background-color: white;
        z-index: 2;
        border-radius: 50%;
        transform: scale(0);
        animation: scale-in .2s ease-out forwards;
      }
      &::after {
        content: '';
        display: block;
        position: relative;
        margin-left: -4px;
        margin-top: -4px;
        width: 24px;
        height: 24px;
        background-color: #25A3A8;
        border-radius: 50%;
      }
    }
    .ve-label {
      margin-left: 24px;
    }
  }
</style>
