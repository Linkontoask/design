<template>
  <div class="order-detail">
    <div class="top"></div>
  </div>
</template>

<script>
  import axios from '../../../utils/axios'
  export default {
    name: 'orderDetail',
    data() {
      return {

      }
    },
    methods: {

    },
    mounted() {

    },
    beforeMount() {

    }
  }
</script>

<style scoped lang="less">
.order-detail {
  position: relative;
  margin-top: -56px;
  .top {
    width: 100%;
    height: 266px;
    background: url("../../../assets/order.png") no-repeat;
    background-size: 100%;
  }
}
</style>
