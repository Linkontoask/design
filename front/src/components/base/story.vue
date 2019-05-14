<template>
  <div class="Stay-story">
    <ul>
      <li v-for="(item, index) in data" :key="index">
        <img :src="item.imgs[0]" alt="not find img">
        <div class="content">
          <h4>{{ item.name }}</h4>
          <div class="desc clamp2">{{ item.content }}</div>
          <div class="comment">
            <div v-if="item.comment">
              <img v-for="obj in item.comment" :src="obj" alt="not find img">
            </div>
            <p v-if="item.extent">{{ item.extent }}条评论</p>
            <p style="margin-left: 0" v-else>这个故事还没有人评论哦</p>
          </div>
        </div>
      </li>
    </ul>
  </div>
</template>

<script>
  export default {
    name: 'stayStory',
    props: {
      data: {
        type: Array,
        default: () => []
      }
    }
  }
</script>

<style lang="less" scoped>
.Stay-story {
  ul {
    display: flex;
    flex-wrap: wrap;
    justify-content: space-between;
  }
  li {
    width: 48%;
    margin-top: 24px;
    > img {
      width: 100%;
      height: 118px;
      border-radius: 4px;
    }
    .content {
      h4 {
        margin-top: 8px;
        color: #8A7524;
        font-size: 14px;
        font-weight: 500;
      }
      .desc {
        margin-top: 4px;
        font-size: 12px;
      }
      .comment {
        display: flex;
        align-items: center;
        margin-top: 8px;
        p {
          font-size: 12px;
          color: #8F9895;
          margin-left: 20px;
        }
        > div {
          display: inline-block;
          float: left;
          img {
            width: 24px;
            height: 24px;
            border: 1px solid white;
            border-radius: 50%;
          }
          img:not(:first-child) {
            margin-left: -4px;
          }
        }
      }
    }
  }
}
</style>
