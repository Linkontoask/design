<template>
  <div class="feed-back">
    <h1>反馈</h1>
    <textarea v-model="value" class="textarea" name="" id="" cols="30" rows="10"></textarea>
    <p>输入您想反馈的信息</p>
    <ve-button class="primary" @click="handleSend">发送</ve-button>
  </div>
</template>

<script>
  import axios from '../../../utils/axios'
  export default {
    name: '',
    data() {
      return {
        value: ''
      }
    },
    methods: {
      handleSend() {
        if (!this.value) {
          this.$msg({
            type: 'error',
            message: '请输入需要反馈的信息后再点击发送'
          })
        } else {
          this.$router.back()
        }
      }
    },
    mounted() {

    },
    beforeMount() {

    }
  }
</script>

<style scoped lang="less">
.feed-back {
  position: relative;
  padding: 86px 24px 24px;
  p {
    font-size: 14px;
    color: #5F6564;
    margin-top: 8px;
  }
  .primary {
    margin-top: 24px;
  }
  h1 {
    font-size: 20px;
    color: #2E312F;
    margin-bottom: 55px;
  }
}
</style>
