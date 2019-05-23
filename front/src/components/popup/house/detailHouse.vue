<template>
  <div class="detailHouse">
    <div data-in="pulse" class="detail-house-img animated fast-time">
      <swiper :options="swiperOption" ref="city" class="swiper-content">
        <swiper-slide v-for="(img, imgIndex) in house.imgs" :key="imgIndex">
          <div class="img-content" :style="{backgroundImage: `url(${img})`}"></div>
        </swiper-slide>
        <div class="swiper-paginations" slot="pagination"></div>
      </swiper>
      <button ref="heartBox" class="icobutton--heart"><span :style="{color: house.is_collect ? '#FF6767' : '#fff'}"
                                                            ref="heart" class="heart fa fa-heart"></span></button>
    </div>
    <div data-in="bounceInUp" class="p36 animated fast-time">
      <div class="detail-name" @click="handlelandlord">
        <div class="clamp2">{{ house.name }}</div>
        <div style="color: #A8B2AF;font-size: 13px;margin-top: 8px">{{ house.position }}</div>
        <tag class="tag" v-for="(item, index) in tag" :key="index">{{item}}</tag>
        <div class="detail-house-avatar" v-if="hotel_user.avatar"
             :style="{backgroundImage: `url(${require('../../../assets/'+hotel_user.avatar)})`}"></div>
      </div>
      <div class="house-offer">
        特别优惠说明，4月17日 - 5月12日才可以
        享受此优惠政策
      </div>
      <div class="detail-box-t">
        <h3>房源设施 <span class="more" @click="handleMoreActive">更多设施</span></h3>
        <ul class="act">
          <li v-for="(item, index) in house.facility" :key="index" v-if="index !== 0"><img
                  :src="require('../../../assets/'+radio[item].img)" alt="">
            <p>{{radio[item].name}}</p></li>
        </ul>
      </div>
      <div class="detail-box-t">
        <h3>房源描述 <span @click="handleMoreDesc">更多</span></h3>
        <div class="clamp2">{{ house.host_desc ? house.host_desc : '没有此房源的描述信息' }}</div>
      </div>
      <div class="detail-box-t">
        <h3>评价</h3>
        <div class="evaluation">
          <evaluationBase :evaluation="hotel_Appraise.user_list"></evaluationBase>
          <div class="btn" @click="handleAllEvaluation">查看全部{{ hotel_Appraise.appraise_num }}条评价</div>
        </div>
      </div>
      <div class="map">
        <MapGd v-if="isShowMap"></MapGd>
        <ul>
          <li>轨道交通1号线。从上新街下车步行240米 就到了</li>
          <li>公交207上新街下车。往南步行356米右转 即可到达</li>
        </ul>
      </div>
      <div class="detail-box-t">
        <h3>周边美食</h3>
        <food v-if="around_list.length !== 0" :data="around_list"></food>
        <div v-else>没有周边美食</div>
      </div>
      <div class="detail-box-t">
        <h3 style="margin-bottom: 0">相似房源</h3>
        <House v-if="similar_hotel.length !== 0" :data="similar_hotel"></House>
        <div v-else>暂时还没有类似的房源，快去发布你的房源吧</div>
      </div>
    </div>
    <div data-in="fadeInRight" class="control">
      <div>
        <p><span class="price">{{ house.price }}</span><span class="line">{{ house.price - Math.floor(Math.random() * 100 + 10) }}</span>
          / 一晚</p>
        <p>
          <img v-for="(item, index) in start" :key="index"
               :src="require('../../../assets/' + (item ? 'start-fill' : 'start') + '.png')" alt="">
        </p>
      </div>
      <div class="btn-go" @touchend="handleBook">预定</div>
    </div>
  </div>
</template>

<script>
  import Storage from '../../../utils/localStorage'
  import axios from '../../../utils/axios'
  import tag from '../../base/ve-tag'
  import food from '../../base/food'
  import House from '../../base/house'
  import evaluationBase from '../../base/evaluationBase'
  import MapGd from '../../base/map'
  import Animocon from '../../../animation/animation'
  import {mapMutations} from 'vuex'

  export default {
    name: "detailHouse",
    components: {
      tag,
      food,
      House,
      MapGd,
      evaluationBase
    },
    data() {
      return {
        house: {},
        hotel_user: {},
        hotel_Appraise: {},
        isShowMap: false,
        around_list: [],
        swiperOption: {
          slidesPerView: 'auto',
          pagination: {
            el: '.swiper-paginations'
          },
          lazyLoadingInPrevNextAmount: 2
        },
        foodList: [],
        similar_hotel: [],
        radio: [{name: '基本设施', img: '', id: 0,},
          {name: '无线网络', img: 'wifi.png', id: 1,},
          {name: '免费停车位', img: 'parkingSpace.png', id: 2,},
          {name: '电视', img: 'tv.png', id: 3,},
          {name: '暖气', img: 'Heating.png', id: 4,},
          {name: '洗衣机', img: 'machine.png', id: 5,},
          {name: '洗发水', img: 'shampoo.png', id: 6,},
          {name: '书桌', img: 'desk.png', id: 7,}],
      }
    },
    computed: {
      tag() {
        return !this.house.tag ? [] : this.house.tag.split('|')
      },
      start() {
        const d = Array.from({length: 5 - this.house.total_score}).fill(false);
        return Array.from({length: this.house.total_score}).fill(true).concat(d)
      }
    },
    methods: {
      ...mapMutations([
        'BOOK_HOUSE'
      ]),
      async handleCollection(status) {
        let url = status ? '/hotel/user_collect/' : '/hotel/del_collect/';
        const data = await axios.get.call(this, url, {
          belong_class: this.house.obj_class,
          belong_id: this.house.hotel_id,
        });
        if (data.r === 0) {
          this.$msg({type: 'success', message: status ? '收藏成功' : '取消收藏成功'})
        } else {
          this.$msg({type: 'success', message: data.e})
        }
      },
      handleAllEvaluation() {
        this.$router.push({
          name: 'evaluation',
          query: {
            belong_class: this.house.obj_class,
            belong_id: this.house.hotel_id
          }
        })
      },
      handleMoreDesc() {
        this.$router.push('houseDesc')
      },
      handleMoreActive() {
        // facility
        this.$router.push({
          name: 'houseFacility',
          query: {
            facility: this.house.facility ? this.house.facility.join('|') : ''
          }
        })
      },
      handlelandlord() {
        this.$router.push({
          name: 'landlord',
          query: {
            uuid: this.house.user_id
          }
        })
      },
      handleBook() {
        this.BOOK_HOUSE({
          hotel_id: this.house.hotel_id,
          user_id: this.house.user_id,
          price: this.house.price,
          obj_class: this.house.obj_class,
        });
        this.$router.push({
          path: '/PopHouse/houseBook',
          query: {
            control: 'close',
            direction: 'pop-bottom',
            price: this.house.price
          }
        })
      },
      async getData() {
        const data = await axios.get.call(this, '/hotel/get_one_hotel/', {hotel_id: this.$route.query.id});
        this.house = data.data.hotel_dict[0];
        this.around_list = data.data.around_list;
        this.hotel_user = data.data.hotel_user;
        this.similar_hotel = data.data.similar_hotel;
        this.hotel_Appraise = data.data.hotel_Appraise;
      },
      scroll() {
        const top = document.documentElement.scrollTop || window.pageYOffset || document.body.scrollTop;
        if (top >= 430) {
          this.isShowMap = true;
          window.removeEventListener('scroll', this.scroll)
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
              onUpdate: (progress) => {
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
          onUnCheck() {
            vm.handleCollection(false);
            el16span.style.color = '#fff';
          },
          onCheck() {
            vm.handleCollection(true);
          }
        });
      }
    },
    mounted() {
      window.addEventListener('scroll', this.scroll)
      this.heartAnimation()
    },
    async activated() {
      this.getData()
    },
    async beforeMount() {
      // this.getData()
    }
  }
</script>

<style scoped lang="less">
  .detailHouse {
    position: relative;
    padding-bottom: 68px;
    background-color: #F3F3F3;
    .detail-house-img {
      position: relative;
      height: 280px;
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
        height: 280px;
        .img-content {
          height: 100%;
          background-repeat: no-repeat;
          background-position: center;
          background-size: cover;
        }
      }

    }
    .p36 {
      padding: 0 0 48px;
      position: relative;
      z-index: 1;
      > div {
        padding: 20px 36px;
        background-color: white;
      }
      .act {
        display: flex;
        flex-wrap: wrap;
        align-items: center;
        margin-top: -20px;
        li {
          margin-top: 20px;
          display: flex;
          align-items: center;
          justify-content: space-around;
          flex-wrap: wrap;
          width: 24%;
          img {
            width: 24px;
          }
          p {
            width: 100%;
            text-align: center;
            font-size: 13px;
            color: #A8B2AF;
            margin-top: 4px;
          }
        }
      }
    }
    .detail-house-avatar {
      position: absolute;
      top: 50%;
      transform: translateY(-50%);
      right: 36px;
      width: 52px;
      height: 52px;
      border-radius: 50%;
      background-size: cover;
      background-position: center;
    }
    .detail-name {
      position: relative;
      .clamp2 {
        font-size: 20px;
        font-weight: bold;
        color: #2E3130;
        width: 80%;
      }
      .tag {
        margin-top: 16px;
      }
    }
    .house-offer {
      margin-top: 16px;
      font-size: 14px;
      border-top: 1px solid #E4ECE8;
      border-bottom: 1px solid #E4ECE8;
    }
    .detail-box-t {
      margin-top: 16px;
      padding-bottom: 24px;
      border-bottom: 1px solid #E4ECE8;
      .evaluation {
        .btn {
          margin-top: 24px;
          color: #25A3A8;
        }
      }
      h3 {
        color: #2E3130;
        margin-bottom: 26px;
        font-weight: 500;
        font-size: 18px;
        span {
          float: right;
          color: #25A3A8;
          font-size: 14px;
        }
      }
      .clamp2 {
        font-size: 13px;
      }
    }
    .map {
      margin-top: 16px;
      ul {
        padding-left: 20px;
        li {
          margin-top: 24px;
          line-height: 1.5;
          font-size: 14px;
          color: #2E3130;
          list-style-type: lower-alpha;
        }
        li + li {

        }
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
      img {
        width: 14px;
      }
      p:first-child {
        font-size: 14px;
      }
      .price {
        font-size: 20px;
        font-weight: bold;
        color: #EB0C0C;
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
