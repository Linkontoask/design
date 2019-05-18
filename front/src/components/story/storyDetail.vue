<template>
  <div class="story-detail">
    <div class="detail-story-img">
      <swiper :options="swiperOption" ref="city" class="swiper-content">
        <swiper-slide v-for="(img, imgIndex) in story.imgs" :key="imgIndex">
          <div class="img-content" :style="{backgroundImage: `url(${img})`}"></div>
        </swiper-slide>
        <div class="swiper-paginations" slot="pagination"></div>
      </swiper>
      <button ref="heartBox" class="icobutton--heart"><span ref="heart" :style="{color: story.is_collect ? '#FF6767' : '#fff'}" class="heart fa fa-heart"></span></button>
    </div>
    <div class="content">
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
    <div class="evaluation">
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
  import Animocon from '../../animation/animation'
  import Storage from '../../utils/localStorage'
  import axios from '../../utils/axios'
  import evaluationBase from '../base/evaluationBase'
  export default {
    name: "storyDetail",
    components: {
      evaluationBase
    },
    data() {
      return {
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
          this.$msg({type: 'success', message: status ? '收藏成功' : '取消收藏成功'})
        } else {
          this.$msg({type: 'success', message: data.e})
        }
      },
      // 点赞动画
      heartAnimation() {
        let vm = this;
        let el16 = vm.$refs.heartBox, el16span = vm.$refs.heart;
        let opacityCurve16 = mojs.easing.path('M0,0 L25.333,0 L75.333,100 L100,0');
        let translationCurve16 = mojs.easing.path('M0,100h25.3c0,0,6.5-37.3,15-56c12.3-27,35-44,35-44v150c0,0-1.1-12.2,9.7-33.3c9.7-19,15-22.9,15-22.9');
        let squashCurve16 = mojs.easing.path('M0,100.004963 C0,100.004963 25,147.596355 25,100.004961 C25,70.7741867 32.2461944,85.3230873 58.484375,94.8579105 C68.9280825,98.6531013 83.2611815,99.9999999 100,100');
        new Animocon.Animocon(el16, {
          tweens: [
            // burst animation (circles)
            new mojs.Burst({
              parent: el16,
              count: 6,
              radius: {0: 150},
              degree: 50,
              angle: -25,
              opacity: 0.3,
              children: {
                fill: '#FF6767',
                scale: 1,
                radius: {'rand(5,15)': 0},
                duration: 1700,
                delay: 350,
                easing: mojs.easing.bezier(0.1, 1, 0.3, 1)
              }
            }),
            new mojs.Burst({
              parent: el16,
              count: 3,
              degree: 0,
              radius: {80: 250},
              angle: 180,
              children: {
                top: [45, 0, 45],
                left: [-15, 0, 15],
                shape: 'line',
                radius: {60: 0},
                scale: 1,
                stroke: '#FF6767',
                opacity: 0.4,
                duration: 650,
                delay: 200,
                easing: mojs.easing.bezier(0.1, 1, 0.3, 1)
              },
            }),
            // icon scale animation
            new mojs.Tween({
              duration: 500,
              onUpdate: function (progress) {
                let translateProgress = translationCurve16(progress),
                  squashProgress = squashCurve16(progress),
                  scaleX = 1 - 2 * squashProgress,
                  scaleY = 1 + 2 * squashProgress;

                el16span.style.WebkitTransform = el16span.style.transform = 'translate3d(0,' + -180 * translateProgress + 'px,0) scale3d(' + scaleX + ',' + scaleY + ',1)';

                el16span.style.opacity = opacityCurve16(progress);

                el16span.style.color = progress >= 0.75 ? '#FF6767' : '#fff';
              }
            })
          ],
          onUnCheck: function () {
            vm.handleCollection(false);
            el16span.style.color = '#fff';
          },
          onCheck() {
            vm.handleCollection(true);
          }
        });
      }
    },
    activated() {
      this.heartAnimation();
      this.getStorage();
      this.getUser()
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
      margin-top: 24px;
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
  .detail-story-img {
    position: relative;
    .icobutton--heart {
      position: absolute;
      right: 36px;
      top: 18px;
      border: none;
      background: transparent;
      z-index: 3;
    }
    .heart {
      font-size: 24px;
      color: white;
    }
    .swiper-content {
      height: 234px;
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
