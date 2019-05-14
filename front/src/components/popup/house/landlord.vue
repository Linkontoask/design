<template>
  <div class="landlord">
    <div class="user-info">
      <div class="user-info-text">
        <h3>{{ user.name }}</h3>
        <p>{{ user.join_time }}</p>
      </div>
      <img class="user-info-avatar" :src="require('../../../assets/'+user.avatar)" alt="">
    </div>
    <div class="text">
      <h1>心灵的旅行</h1>
      <div>
        这个城市
        或许陌生
        又或者熟悉

        可总有那么一个地方...</div>
    </div>
    <div class="other">
      <h3>房东的其它房源</h3>
      <house :data="houseList"></house>
    </div>
  </div>
</template>

<script>
  import house from '../../base/house'
  export default {
    name: "landlord",
    components: {
      house
    },
    data() {
      return {
        user: {
          name: 'Link',
          join_time: '2019年10月1号',
          avatar: 'avatar-1.png'
        },
        houseList: []
      }
    },
  }
</script>

<style scoped lang="less">
  @import "../../../style/global";
.landlord {
  .user-info {
    display: flex;
    align-items: center;
    justify-content: space-between;
    padding-bottom: 24px;
    width: calc(100% - 72px);
    margin: 108px - @topIndicator auto 0;
    border-bottom: 1px solid #E3E9E6;
    .user-info-text {
      h3 {
        color: #2E3130;
      }
      p {
        color: #909399;
        margin-top: 8px;
        font-size: 14px;
      }
    }
    .user-info-avatar {
      width: 64px;
    }
  }
  .text {
    margin-top: 48px;
    text-align: center;
    h1 {
      font-size: 16px;
      margin-bottom: 24px;
    }
    div {
      text-align: left;
      line-height: 2;
      white-space: pre-wrap;
      padding: 0 36px;
      font-size: 14px;
    }
  }
  .other {
    padding: 48px 36px;
    h3 {
      font-size: 16px;
      margin-bottom: 24px;
    }
  }
}
</style>
