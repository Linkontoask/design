<template xmlns:v-hammer="http://www.w3.org/1999/xhtml">
  <div class="time" @click="handleDate">
    <div class="info">
      <span>入住时间</span>
      <span>离开时间</span>
    </div>
    <div class="time-a">
      <span>{{ time[0] }}</span>
      <div><p>共{{ day }}晚</p><div class="line"></div></div>
      <span>{{ time[1] }}</span>
    </div>
    <Dialog :vis="visDialog" @close="dialogClose">
      <datePicker :showAmount="5" @complete="dateComplete"></datePicker>
    </Dialog>
  </div>
</template>

<script>
  import Dialog from '../dialog'
  import datePicker from './datePicker'

  export default {
    name: "Time",
    components: {
      Dialog,
      datePicker
    },
    props: {
      time: {
        type: Array,
        default: () => []
      },
    },
    data() {
      return {
        visDialog: false,
        isX: false,
        day: 1,
      }
    },
    watch: {
    },
    methods: {
      handleDate(el) {
        // console.log(el.composedPath()) // el.path兼容性解决方案
        !this.$route.path.includes('/userOrderDetail') &&
        !el.composedPath().some(item => item.id === 'dialog') && (this.visDialog = true)
      },
      dateComplete(start, end, format, current) {
        this.dialogClose();
        this.day = Number(current.match(/\d+/)[0]);
        this.$emit('change', [start, end], current)
      },
      dialogClose() {
        this.visDialog = false;
      },
    },
    mounted() {

    }
  }
</script>

<style scoped lang="less">
  .time {
    margin-top: 36px;
    padding: 0 24px;
    cursor: pointer;
    -webkit-tap-highlight-color: transparent;
    > div {
      display: flex;
      align-items: center;
      justify-content: space-between;
    }
    .info {
      font-size: 14px;
    }
    .time-a {
      margin-top: 12px;
      > div {
        width: 60%;
        color: #FE5656;
        text-align: center;
        font-size: 12px;
        position: relative;
        .line {
          position: absolute;
          width: 100%;
          top: 9px;
          border-bottom: 1px solid #EBF5F1;
        }
        p {
          position: relative;
          z-index: 2;
          background-color: white;
          width: 54px;
          margin: 0 auto;
        }
      }
      span {
        font-size: 18px;
        color: #25A3A8;
        width: 5rem;
        flex-shrink: 0;
        text-align: center;
      }
    }
  }
</style>
