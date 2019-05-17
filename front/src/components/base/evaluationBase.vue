<template>
  <div class="evaluation-base">
    <ul>
      <li v-for="(item, index) in evaluation" :key="index">
        <div class="t">
          <div class="detail-house-avatar" :style="{backgroundImage: `url(${require('../../assets/'+item.user_info.avatar)})`}"></div>
          <div class="content">
            <p>{{ item.user_info.user_name }}</p>
            <p>{{ item.user_info.register_time }}</p>
          </div>
        </div>
        <div class="clamp2">{{ item.appraise }}</div>
        <img class="content-img" v-for="(img, i) in item.img" :key="i" :src="img" alt="服务器错误">
      </li>
    </ul>
  </div>
</template>

<script>
  export default {
    name: "evaluationBase",
    data() {
      return {
      }
    },
    props: {
      evaluation: {
        type: Array,
        default: () => []
      }
    },
    mounted() {
    }
  }
</script>

<style scoped lang="less">
.evaluation-base {
  li + li {
    margin-top: 48px;
  }
  .t {
    display: flex;
    align-items: center;
    .detail-house-avatar {
      width: 42px;
      height: 42px;
      border-radius: 50%;
      background-size: cover;
      background-position: center;
    }
    .content {
      margin-left: 20px;
      p:first-child {
        font-size: 14px;
        color: #5F6564;
      }
      p:last-child {
        margin-top: 8px;
        font-size: 12px;
        color: #C5D1CD;
      }
    }
  }
  .content-img {
    max-width: 40%;
    max-height: 260px;
    border-radius: 4px;
    margin-top: 12px;
    vertical-align: bottom;
  }
  .content-img + .content-img {
    margin-left: 10px;
  }
  .clamp2 {
    font-size: 14px;
    margin-top: 16px;
    line-height: 1.5;
  }
}
</style>
