<template xmlns:v-hammer="http://www.w3.org/1999/xhtml">
  <div class="Stay-story">
    <ul ref="storyBox">
      <li v-for="(item, index) in data" :key="index" v-hammer:tap="elm => handleView(elm, item, index)">
        <div class="img-content" :style="{backgroundImage: `url(${require('../../static/data/imgs/'+item.imgs[0])})`}"></div>
        <div class="content">
          <h4>{{ item.name }}</h4>
          <div class="desc clamp2">{{ item.content }}</div>
          <div class="comment">
            <p v-if="item.appraise.appraise_num !== 0">{{ item.appraise.appraise_num }}条评论</p>
            <p style="margin-left: 0" v-else>这个故事还没有人评论哦</p>
          </div>
        </div>
      </li>
    </ul>
  </div>
</template>

<script>
  import Storage from '../../utils/localStorage'
  export default {
    name: 'stayStory',
    props: {
      data: {
        type: Array,
        default: () => []
      }
    },
    data() {
      return {
      }
    },
    methods: {
      handleView(elm, obj, index) {
        Storage.set('now_checked_story', this.data[index]);
        const box = document.createElement('div');
        const node = document.createElement('div');
        const rect = this.$refs.storyBox.childNodes[index].childNodes[0].getBoundingClientRect()
        node.setAttribute('style', `background-image: url(${this.data[index].imgs[0]})`);
        box.setAttribute('class', 'animation-form');
        box.setAttribute('data-id', new Date().getTime());
        box.setAttribute('style', `left: ${rect.left}px;top: ${rect.top}px;width: ${rect.width}px; height: ${rect.height}px`);
        box.appendChild(node);
        document.body.appendChild(box);
        setTimeout(() => {
          document.body.removeChild(box);
        }, 600)
        this.$router.push({
          path: '/PopHouse/StoryDetail',
          query: {
            bgColor: '#fff',
            control: 'close',
            direction: 'pop-bottom',
            id: this.data[index].story_id
          }
        })
      },
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
    box-shadow: 0 0.0625rem 0.125rem #cbdad8;
    > img {
      width: 100%;
      height: 118px;
      border-radius: 4px;
    }
    .img-content {
      height: 118px;
      background-repeat: no-repeat;
      background-position: center;
      background-size: cover;
      border-radius: 4px;
    }
    .content {
      padding: 0 4px 4px;
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
