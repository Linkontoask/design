<template>
  <div class="story-detail">
    <div class="detail-story-img" :class="{show: isShowOpacity}">
      <swiper :options="swiperOption" ref="city" class="swiper-content">
        <swiper-slide v-for="(img, imgIndex) in story.imgs" :key="imgIndex">
          <div class="img-content" :style="{backgroundImage: `url(${img})`}"></div>
        </swiper-slide>
        <div class="swiper-paginations" slot="pagination"></div>
      </swiper>
      <button ref="heartBox" class="icobutton--heart"><span ref="heart" :style="{color: story.is_collect ? '#FF6767' : '#fff'}" class="heart fa fa-heart"></span></button>
    </div>
    <div class="content animated fast-time" data-in="slideInDown">
      <div class="story-user">
        <img v-if="user.avatar" :src="require('../../assets/'+user.avatar)" alt="">
        <div>
          <h4>{{ user.user_name }}</h4>
          <p>{{ story.create_time }}</p>
        </div>
      </div>
      <h1>{{ story.name }}</h1>
      <div class="story-content">{{ story.content }}</div>
    </div>
    <div class="evaluation animated fast-time" data-in="slideInDown">
      <div class="top">
        <p>{{ evaluation.length }}条评价</p>
        <p class="primary" @click="handleWriteEvaluation">写评论</p>
      </div>
      <div class="evaluation-content">
        <evaluationBase :evaluation="evaluation"></evaluationBase>
      </div>
      <div class="none" v-if="evaluation.length === 0">暂时还没有人对这条故事发表任何观点</div>
    </div>
  </div>
</template>

<script>
  import Storage from '../../utils/localStorage'
  import axios from '../../utils/axios'
  import evaluationBase from '../base/evaluationBase'
  import mixin from '../../mixin/detail'
  export default {
    name: "storyDetail",
    components: {
      evaluationBase
    },
    mixins: [mixin],
    data() {
      return {
        isShowOpacity: false,
        story: [],
        user: {},
        evaluation: [],
        swiperOption: {
          slidesPerView: 'auto',
          pagination: {
            el: '.swiper-paginations'
          }
        },
      }
    },
    methods: {
      handleWriteEvaluation() {
        this.$router.push({
          name: 'storyWriteEvaluation',
          query: {
            obj_class: this.story.obj_class,
            belong_id: this.story.story_id
          }
        })
      },
      async getUser() {
        const data = await axios.get.call(this, '/hotel/user_info/', {
          user_id: this.story.user_id
        });
        this.user = data.data;
        const evaluation = await axios.get.call(this, '/hotel/get_appraise/', {
          belong_class: this.story.obj_class,
          belong_id: this.story.story_id
        })
        this.evaluation = evaluation.data.user_list
      },
      getStorage() {
        this.story = Storage.get('now_checked_story')
      },
      async handleCollection(status) {
        let url = status ? '/hotel/user_collect/' : '/hotel/del_collect/';
        const data = await axios.get.call(this, url, {
          belong_class: this.story.obj_class,
          belong_id: this.story.story_id,
        });
        if (data.r === 0) {
          //this.$msg({type: 'success', message: status ? '收藏成功' : '取消收藏成功'})
        } else {
          //this.$msg({type: 'success', message: data.e})
        }
      },
    },
    activated() {
      this.heartAnimation();
      this.getStorage();
      this.getUser();
      setTimeout(() => {
        this.isShowOpacity = true
      }, 300)
    },
    beforeDestroy() {
      this.isShowOpacity = false
    },
    mounted() {
      /*this.heartAnimation();
      this.getStorage();
      this.getUser()*/
    }
  }
</script>

<style scoped lang="less">
.story-detail {
  position: relative;
  .evaluation {
    margin-top: 44px;
    padding: 0 36px;
    .top {
      display: flex;
      justify-content: space-between;
      align-items: center;
      p:first-child {
        color: #2E3130;
        font-size: 14px;
      }
    }
    .evaluation-content {
      margin-top: 24px;
      padding-bottom: 36px;
    }
    .none {
      color: #C5D1CD;
      padding-bottom: 36px;
    }
    .primary {
      font-size: 14px;
      color: #25A3A8;
    }
  }
  .content {
    padding: 36px;
    border-bottom: 1px solid #E3E9E6;
    .story-content {
      font-size: 14px;
      color: #8F9895;
      text-indent: 30px;
      line-height: 2;
    }
  }
  .story-user {
    display: flex;
    height: 56px;
    padding-bottom: 24px;
    img {
      flex-shrink: 0;
      width: 56px;
    }
    div {
      margin-left: 20px;
    }
    h4 {
      font-size: 16px;
      color: #2E3130;
    }
    p {
      font-size: 14px;
      color: #8F9895;
      margin-top: 16px;
    }
  }
  h1 {
    margin-top: 16px;
    margin-bottom: 24px;
    font-size: 20px;
    color: #2E3130;
  }
  div.show {
    opacity: 1;
  }
  .detail-story-img {
    position: relative;
    opacity: 0;
    .icobutton--heart {
      position: absolute;
      right: 36px;
      top: 1.625rem;
      border: none;
      background: transparent;
      z-index: 3;
    }
    .heart {
      font-size: 24px;
      color: white;
    }
    .swiper-content {
      height: 280px;
      .img-content {
        height: 100%;
        background-repeat: no-repeat;
        background-position: center;
        background-size: cover;
      }
    }
  }
}
</style>
