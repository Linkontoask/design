<template xmlns:v-hammer="http://www.w3.org/1999/xhtml">
  <div class="success">
    <div class="pop-control left" v-hammer:tap="handleTap">
      <p></p>
      <p></p>
    </div>
    <div class="success-content">
      <div>
        <img src="../../../assets/success.png" alt="">
      </div>
      <p>预定成功</p>
      <!--<div @click="handleViewOrder">查看订单信息</div>-->
    </div>
  </div>
</template>

<script>
  import Storage from '../../../utils/localStorage'
  export default {
    name: "success",
    methods: {
      handleTap() {
        this.$router.push({
          name: 'homeStay'
        })
      },
      handleViewOrder() {
        Storage.remove('before_url_house_');
        this.$router.push({name: 'userOrderDetail', query: {bgColor: '#fff', order_id: this.$route.query.uuid}})
      }
    }
  }
</script>

<style scoped lang="less">
.success {
  position: relative;
  width: 100vw;
  height: 100vh;
  .pop-control {
    position: fixed;
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
  .success-content {
    display: flex;
    align-items: center;
    justify-content: space-around;
    flex-wrap: wrap;
    position: absolute;
    left: 50%;
    top: 50%;
    transform: translate(-50%,-50%);
    div {
      color: #25A3A8;
    }
  }
  img {
    display: block;
    margin: 0 auto;
  }
  p {
    margin: 24px 0 36px;
  }
  div {
    width: 100%;
    font-size: 20px;
    text-align: center;
  }
}
</style>
