<template>
  <div class="success">
    <div>
      <img src="../../../assets/success.png" alt="">
    </div>
    <p>预定成功</p>
    <div @touchend="handleView">查看订单信息</div>
  </div>
</template>

<script>
  export default {
    name: "success",
    methods: {
      handleView() {

      }
    }
  }
</script>

<style scoped lang="less">
.success {
  display: flex;
  align-items: center;
  justify-content: space-around;
  flex-wrap: wrap;
  position: absolute;
  left: 50%;
  top: 50%;
  transform: translate(-50%,-50%);
  img {
    display: block;
    margin: 0 auto;
  }
  p {
    margin: 24px 0 36px;
  }
  div {
    width: 100%;
    color: #25A3A8;
    font-size: 20px;
    text-align: center;
  }
}
</style>
