<template>
  <div class="time">
    <div class="info">
      <span>入住时间</span>
      <span>离开时间</span>
    </div>
    <div class="time-a">
      <span>{{ time[0] }}</span>
      <div><p>共{{ day }}晚</p><div class="line"></div></div>
      <span>{{ time[1] }}</span>
    </div>
  </div>
</template>

<script>
  export default {
    name: "Time",
    props: {
      time: {
        type: Array,
        default: () => []
      },
      day: {
        type: [String, Number],
        default: 1
      }
    }
  }
</script>

<style scoped lang="less">
  .time {
    margin-top: 36px;
    padding: 0 36px;
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
        width: 74px;
        flex-shrink: 0;
        text-align: center;
      }
    }
  }
</style>
