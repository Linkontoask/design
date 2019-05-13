<template>
  <div class="user-information">
    <div class="user-info">
      <div class="user-info-text">
        <h3>{{ user.name }}</h3>
        <p>{{ user.join_time }}</p>
      </div>
      <div class="user-info-avatar" :style="{backgroundImage: `url(${user.avatar})`}"></div>
    </div>
    <div class="box">
      <h4>我发布的故事</h4>
      <story :data="storyList"></story>
    </div>
    <div class="box">
      <h4>我发布的房源</h4>
      <story :data="houseList"></story>
    </div>
  </div>
</template>

<script>
  import axios from '../../../utils/axios'
  import cookie from '../../../utils/cookie'
  import story from '../../base/story'
  export default {
    name: 'userInformation',
    data() {
      return {
        user: {
          name: 'Link',
          join_time: '2019年10月1号'
        },
        storyList: [],
        houseList: []
      }
    },
    components: {
      story
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
  @import "../../../style/global";
.user-information {
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
      height: 64px;
      background: no-repeat center;
    }
  }
  .box {
    padding: 0 36px;
    margin-top: 32px;
    h4 {
      font-weight: 500;
    }
  }
}
</style>