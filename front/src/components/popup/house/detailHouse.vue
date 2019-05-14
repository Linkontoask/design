<template>
  <div class="detailHouse">
    <div class="detail-house-img">
      <swiper :options="swiperOption" ref="city" class="swiper-content">
        <swiper-slide v-for="(img, imgIndex) in house.imgs" :key="imgIndex">
          <div>
            <img :src="img" alt="not find img">
          </div>
        </swiper-slide>
        <div class="swiper-paginations" slot="pagination"></div>
      </swiper>
    </div>
    <div class="p36">
      <div class="detail-name" @click="handlelandlord">
        <div class="clamp2">{{ house.name }}</div>
        <tag class="tag" v-for="(item, index) in tag" :key="index">{{item}}</tag>
        <div class="detail-house-avatar" :style="{backgroundImage: `url(${house.avatar})`}"></div>
      </div>
      <div class="house-offer">
        特别优惠说明，4月17日 - 5月12日才可以
        享受此优惠政策
      </div>
      <div class="detail-box-t">
        <h3>房源设施 <span class="more" @click="handleMoreActive">更多设施</span></h3>
        <ul class="act">
          <li v-for="(item, index) in house.facility" :key="index" v-if="index !== 0"><img :src="require('../../../assets/'+radio[item].img)" alt=""><p>{{radio[item].name}}</p></li>
        </ul>
      </div>
      <div class="detail-box-t">
        <h3>房源描述 <span @click="handleMoreDesc">更多</span></h3>
        <div class="clamp2">{{ house.host_desc ? house.host_desc : '没有此房源的描述信息' }}</div>
      </div>
      <div class="detail-box-t">
        <h3>评价</h3>
        <div class="evaluation">
          <div class="t">
            <div class="detail-house-avatar" :style="{backgroundImage: `url(${house.avatar})`}"></div>
            <div class="content">
              <p>评价人</p>
              <p>2019年4月12日</p>
            </div>
          </div>
          <div class="clamp2">评价内容评价内容评价内容评价内容评价内容评价内容评价内容评价内容评价内容</div>
          <div class="btn">查看全部24条评价</div>
        </div>
      </div>
      <div class="map">
        <div class="container" id="container"></div>
        <ul>
          <li>轨道交通1号线。从上新街下车步行240米 就到了</li>
          <li>公交207上新街下车。往南步行356米右转 即可到达</li>
        </ul>
      </div>
      <div class="detail-box-t">
        <h3>周边美食</h3>
        <food :data="around_list"></food>
      </div>
      <div class="detail-box-t">
        <h3>相似房源</h3>
        <house :data="houseList"></house>
      </div>
    </div>
    <div class="control">
      <div>
        <p><span class="price">{{ house.price }}</span><span class="line">{{ house.price - Math.floor(Math.random() * 100 + 10) }}</span> / 一晚</p>
        <p>★★★★☆</p>
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
  import house from '../../base/house'
  export default {
    name: "detailHouse",
    components: {
      tag,
      food,
      house
    },
    data() {
      return {
        house: {},
        around_list: [],
        swiperOption: {
          slidesPerView: 'auto',
          pagination: {
            el: '.swiper-paginations'
          }
        },
        foodList: [],
        houseList: [],
        radio: [{
          name: '基本设施',
          desc: '毛巾、床单、洗浴用品、卫生纸和枕头',
          img: '',
          id: 0,
        },{
          name: '无线网络',
          desc: '在房源内免流量使用互联网',
          img: 'wifi.png',
          id: 1,
        },{
          name: '免费停车位',
          img: 'parkingSpace.png',
          desc: '',
          id: 2,
        },{
          name: '电视',
          img: 'tv.png',
          desc: '',
          id: 3,
        },{
          name: '暖气',
          img: 'Heating.png',
          desc: '中央暖气或房源内的暖气设备',
          id: 4,
        },{
          name: '洗衣机',
          img: 'machine.png',
          desc: '在建筑物内，并且免费供房客使用',
          id: 5,
        },{
          name: '洗发水',
          img: 'shampoo.png',
          desc: '',
          id: 6,
        },{
          name: '书桌',
          img: 'desk.png',
          desc: '一张能放电脑的桌子或书桌，和一把舒适的椅子',
          id: 7,
        }],
      }
    },
    computed: {
      tag() {
        return !this.house.tag ? [] : this.house.tag.split('|')
      }
    },
    methods: {
      handleMoreDesc() {
        this.$router.push('houseDesc')
      },
      handleMoreActive() {
        this.$router.push('houseFacility')
      },
      handlelandlord() {
        this.$router.push('landlord')
      },
      handleBook() {
        this.$router.push({
          path: '/PopHouse/houseBook',
          query: {
            control: 'close',
            direction: 'pop-right'
          }
        })
      },
      async getData() {
        const data = await axios.get.call(this, '/hotel/get_one_hotel/', {hotel_id: Storage.get('now_checked_house').hotel_id});
        this.house = data.data.hotel_dict[0];
        this.around_list = data.data.around_list;
      }
    },
    mounted() {
      setTimeout(() => {
        const a = document.createElement('script');
        a.src = 'https://webapi.amap.com/maps?v=1.4.14&key=d4123dab1e07c48600ba7a2e3ea143f7';
        document.body.appendChild(a);
        a.onload = () => {
          const map = new AMap.Map('container', {
            resizeEnable: true,
            zoom: 15,
            center: [106.613922, 29.53832]
          });
        };
      }, 1000);
    },
    async activated() {
      this.getData()
    },
    async beforeMount() {
      this.getData()
    }
  }
</script>

<style scoped lang="less">
.detailHouse {
  position: relative;
  margin-top: -56px;
  padding-bottom: 68px;
  .detail-house-img {
    position: relative;
    height: 280px;
    .swiper-content {
      height: 280px;
      img {
        max-height: 100%;
        max-width: 100%;
      }
    }

  }
  .p36 {
    padding: 0 36px 48px;
    position: relative;
    z-index: 1;
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
    bottom: 0;
    right: 0;
    width: 52px;
    height: 52px;
    border-radius: 50%;
    background-size: cover;
    background-position: center;
  }
  .detail-name {
    position: relative;
    margin-top: 34px;
    height: 100px;
    .clamp2 {
      font-size: 20px;
      font-weight: bold;
      color: #2E3130;
    }
    .tag {
      margin-top: 24px;
    }
  }
  .house-offer {
    margin-top: 46px;
    font-size: 14px;
    padding: 18px 0;
    border-top: 1px solid #E4ECE8;
    border-bottom: 1px solid #E4ECE8;
  }
  .detail-box-t {
    margin-top: 36px;
    padding-bottom: 24px;
    border-bottom: 1px solid #E4ECE8;
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
    .evaluation {
      .t {
        display: flex;
        align-items: center;
        .content {
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
      .clamp2 {
        font-size: 14px;
        margin-top: 16px;
        line-height: 1.5;
      }
      .btn {
        margin-top: 24px;
        color: #25A3A8;
      }
    }
  }
  .map {
    margin-top: 36px;
    #container {
      left: 0;
      top: 0;
      width: 100%;
      height: 246px;
      overflow: hidden;
    }
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
