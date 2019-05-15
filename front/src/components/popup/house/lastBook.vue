<template>
  <div class="last-book">
    <div class="user-info">
      <h3>房客信息 <span @touchend="handleChange">更改</span></h3>
      <ul>
        <li v-for="(item, index) in user" :key="index">
          <span>{{ item.name }}</span>
          <span>{{ item.id }}</span>
        </li>
      </ul>
      <h4>预定须知</h4>
      <div class="clamp2">预定的一些说明。比如不能携带宠物，或者说不能抽烟，举办派对</div>
    </div>
    <div class="control">
      <div>
        <p><span class="price">{{ '￥189' }}</span> / 一晚</p>
        <p>★★★★☆</p>
      </div>
      <div class="btn-go" @touchend="handleBook">立即预定</div>
    </div>
  </div>
</template>

<script>
  export default {
    name: "lastBook",
    data() {
      return {
        user: [{name: 'Link', id: '430723xxxxxxxx0124'},{name: 'Join', id: '562413xxxxxxxx1224'},]
      }
    },
    methods: {
      handleChange() {
        this.$router.push({
          path: '/PopHouse/newTenant'
        })
      },
      handleBook() {
        this.$router.push({
          path: '/success'
        })
      }
    }
  }
</script>

<style scoped lang="less">
.last-book {
  position: absolute;
  top: 0;
  .user-info {
    padding: 0 36px;
    margin-top: 60px;
    h3 {
      font-size: 16px;
      span {
        color: #25A3A8;
        float: right;
        font-weight: normal;
      }
    }
    ul {
      padding-bottom: 24px;
      border-bottom: 1px solid #E4ECE8;
      li {
        margin-top: 24px;
      }
      span:last-child {
        margin-left: 20px;
      }
    }
    h4 {
      margin-top: 34px;
    }
    .clamp2 {
      margin-top: 12px;
      font-size: 14px;
    }
  }
  .control {
    position: fixed;
    bottom: 0;
    left: 0;
    z-index: 9;
    width: calc(100% - 72px);
    height: 58px;
    padding: 12px 36px 24px;
    border-top: 1px solid #E3E9E6;
    display: flex;
    align-items: center;
    justify-content: space-between;
    background-color: white;
    p:first-child {
      font-size: 14px;
    }
    .price {
      font-size: 20px;
      font-weight: bold;
    }
    .line {
      margin-left: 12px;
      font-size: 12px;
      text-decoration: line-through;
    }
    .btn-go {
      padding: 10px 40px;
      border-radius: 4px;
      background-color: #25A3A8;
      color: white;
    }
  }
}
</style>
