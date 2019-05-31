<template>
  <div class="food-detail">
    <div class="detail-food-img animated fast-time" data-in="pulse" :class="{show: isShowOpacity}">
      <swiper :options="swiperOption" ref="city" class="swiper-content">
        <swiper-slide v-for="(img, imgIndex) in food.imgs" :key="imgIndex">
          <div class="img-content" :style="{backgroundImage: `url(${img})`}"></div>
        </swiper-slide>
        <div class="swiper-paginations" slot="pagination"></div>
      </swiper>
      <button ref="heartBox" class="icobutton--heart"><span ref="heart" :style="{color: food.is_collect[0] ? '#FF6767' : '#fff'}" class="heart fa fa-heart"></span></button>
    </div>
    <div class="food-content animated fast-time" data-in="bounceInRight">
      <div class="food-name">
        <h3>{{ food.name }}</h3>
        <p>{{ food.position }}</p>
      </div>
      <div class="price">
        ￥{{ food.price }}
      </div>
    </div>
    <div class="food-desc animated fast-time" data-in="bounceInUp">
      <h4>美食描述</h4>
      <div v-if="food.detail">{{ food.detail }}</div>
      <div v-else>没有这个美食的的描述哦</div>
    </div>
  </div>
</template>

<script>
  import Storage from '../../utils/localStorage'
  import axios from '../../utils/axios'
  import mixin from '../../mixin/detail'
  export default {
    name: "foodDetail",
    mixins: [mixin],
    data() {
      return {
        isShowOpacity: false,
        food: {
          is_collect: []
        },
        swiperOption: {
          slidesPerView: 'auto',
          pagination: {
            el: '.swiper-paginations'
          }
        },
      }
    },
    methods: {
      getStorage() {
        this.food = Storage.get('now_checked_food')
      },
      async handleCollection(status) {
        let url = status ? '/hotel/user_collect/' : '/hotel/del_collect/';
        const data = await axios.get.call(this, url, {
          belong_class: this.food.obj_class,
          belong_id: this.food.id,
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
      setTimeout(() => {
        this.isShowOpacity = true
      }, 300)
    },
    beforeDestroy() {
      this.isShowOpacity = false
    },
    mounted() {
      /*this.heartAnimation()
      this.getStorage()*/
    }
  }
</script>

<style scoped lang="less">
.food-detail {
  position: relative;
  padding-bottom: 68px;
  .food-desc {
    padding: 36px;
    h4 {
      color: #2E3130;
      text-align: center;
    }
    div {
      font-size: 14px;
      margin-top: 12px;
      text-indent: 30px;
      line-height: 2;
    }
  }
  .food-content {
    padding: 24px 36px;
    border-bottom: 1px solid #E3E9E6;
    display: flex;
    justify-content: space-between;
    .food-name {
      h3 {
        font-size: 20px;
        color: #2E3130;
      }
      p {
        color: #8F9895;
        font-size: 14px;
        margin-top: 16px;
      }
    }
    .price {
      color: #EB0C0C;
    }
  }
  div.show {
    opacity: 1;
  }
  .detail-food-img {
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
