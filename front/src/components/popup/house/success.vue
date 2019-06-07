<template xmlns:v-hammer="http://www.w3.org/1999/xhtml">
  <div class="success">
    <div class="pop-control left" v-hammer:tap="handleTap">
      <p></p>
      <p></p>
    </div>
    <transition name="hidden">
      <div class="success-content" v-if="timeout">
        <div>
          <icon svg="icon-ok" v-if="!isIos"></icon>
          <img v-else src="../../../assets/success.png" alt="">
        </div>
      </div>
    </transition>
    <div v-if="!timeout">
      <div class="bg">
        <h2>预定成功</h2>
        <p>2019.05.12 - 2019.05.13</p>
        <div style="font-size: 16px" @click="handleViewOrder">查看订单信息</div>
      </div>
      <div class="content-order">
        <div class="t">
          <div class="detail-house-avatar" v-if="user_info.avatar" :style="{backgroundImage: `url(${require('../../../assets/'+user_info.avatar)})`}"></div>
          <div class="content">
            <p>{{ hotelName }}</p>
            <p>房东：{{ user_info.user_name }}</p>
          </div>
        </div>
        <div class="white"></div>
        <div class="btn-pink" v-hammer:tap="() => chat = true">联系房东</div>
        <div class="box-content">
          <div class="box">
            <p>天气</p>
            <img src="../../../static/img/weather.jpg" alt="">
          </div>
          <div class="box">
            <p>地理位置</p>
            <MapGd v-if="map"></MapGd>
          </div>
          <div class="box">
            <p>附近景点</p>
            <div class="grid">
              <li :style="{backgroundImage: `url(${require('../../../static/img/story-1.jpg')})`}"><span>涠洲岛</span></li>
              <li :style="{backgroundImage: `url(${require('../../../static/img/story-2.jpg')})`}"><span>壮族名宅</span></li>
              <li :style="{backgroundImage: `url(${require('../../../static/img/story-3.jpg')})`}"><span>云南大理</span></li>
              <li :style="{backgroundImage: `url(${require('../../../static/img/banner-2.jpg')})`}"><span>广西桂林风景区</span></li>
            </div>
          </div>
        </div>
      </div>
    </div>
    <Chat :showChat="chat" :name="hotelName" @close="chat = false"></Chat>
  </div>
</template>

<script>
  import Storage from '../../../utils/localStorage'
  import browser from '../../../utils/browser'
  import MapGd from '../../base/map'
  import Chat from '../../base/chat'
  let ticking = false;
  export default {
    name: "success",
    components: {
      MapGd,
      Chat
    },
    data() {
      return {
        isIos: false,
        timeout: true,
        user_info: {},
        hotelName: '',
        chat: false,
        map: false
      }
    },
    methods: {
      handleTap() {
        this.$router.push({
          name: 'homeStay'
        })
      },
      handleViewOrder() {
        Storage.remove('before_url_house_');
        this.$router.push({name: 'userOrderDetail',
          query: {
            bgColor: '#fff',
            order_id: this.$route.query.uuid
        }})
      },
      scroll(e) {
        if(!ticking) {
          requestAnimationFrame(this.change);
          ticking = true;
        }

      },
      change() {
        ticking = false;
        // console.log(document.documentElement.scrollTop || document.body.scrollTop)
      }
    },
    mounted() {
      window.addEventListener('scroll', this.scroll, false);
      setTimeout(() => {
        this.map = true
      }, 2000)
    },
    beforeMount() {
      this.user_info = Storage.get('now_check_hotel_user') || {};
      this.hotelName = Storage.get('now_checked_house')['name'] || '';
      this.isIos = browser.ios;
      setTimeout(() => {
        this.timeout = false
      }, 1000)
    }
  }
</script>

<style scoped lang="less">
  @keyframes fade {
    80% {border-radius: 40%}
    to {
      width: 100%;
      height: 100vh;
      border-radius: 0;
    }
  }
  @keyframes btot {
    to{
      top: 200px;
    }
  }
.success {
  position: relative;
  width: 100vw;
  height: 100vh;
  .content-order {
    position: absolute;
    top: 100vh;
    left: 0;
    width: calc(100% - 48px);
    border-top-right-radius: 16px;
    border-top-left-radius: 16px;
    animation: btot .4s .4s ease-in forwards;
    text-align: left;
    padding: 24px;
    overflow: hidden;
    background-color: white;
    .box-content {
      margin-top: 36px;
      .box {
        text-align: left;
        img {
          width: 100%;
        }
        .grid {
          display: grid;
          grid-template-columns: repeat(3, 1fr);
          grid-template-rows: repeat(2, 1fr);
          grid-gap: 12px;
          justify-content: center;
          align-items: center;
          width: 100%;
          height: 240px;
          li {
            background-size: cover;
            background-position: center;
            height: 100%;
            border-radius: 8px;
            position: relative;
            span {
              position: absolute;
              bottom: 4px;
              left: 4px;
              color: white;
              font-size: 14px;
            }
          }
          li:first-child {
            grid-row: span 2;
          }
          li:last-child {
            grid-column: span 2;
          }
        }
        p {
          font-size: 18px;
          color: #007479;
          margin: 24px 0 12px;
        }
      }
    }

    .white {
      position: absolute;
      right: 3.25rem;
      top: 52px;
      width: 82px;
      height: 82px;
      border-radius: 50%;
      background-color: white;
      z-index: 2;
    }
    .btn-pink {
      position: absolute;
      right: 0;
      top: 0;
      width: 20%;
      height: 74px;
      font-size: 16px;
      display: flex;
      align-items: center;
      justify-content: space-around;
      color: white;
      border-bottom-left-radius: 8px;
      background-color: #ff8a83;
    }
    .t {
      width: 80%;
      display: flex;
      align-items: center;
      position: relative;
      z-index: 3;
      .detail-house-avatar {
        width: 42px;
        height: 42px;
        border-radius: 50%;
        background-size: cover;
        background-position: center;
        flex-shrink: 0;
      }
      .content {
        margin-left: 20px;
        text-align: left;
        p {
          margin: 0;
        }
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
  }
  .bg {
    position: fixed;
    width: 120px;
    height: 120px;
    border-radius: 50%;
    left: 50%;
    top: 50%;
    background-color: #25A3A8;
    transform: translate(-50%, -50%);
    text-align: center;
    color: white;
    animation: fade .4s ease-in forwards;
    p {
      font-size: 14px;
      margin: 12px 0;
    }
    > div {
      text-decoration: underline;
    }
    h2 {
      letter-spacing: 1px;
      font-weight: normal;
      font-size: 24px;
      padding-top: 64px;
    }
  }
  .pop-control {
    position: fixed;
    top: 14px;
    left: 8px;
    height: 36px;
    width: 46px;
  }
  .close, .left {
    display: flex;
    justify-content: space-between;
    align-items: center;
    z-index: 9;
    p {
      position: absolute;
      left: 0;
      top: 0;
      right: 0;
      bottom: 0;
      margin: auto;
      width: 22px;
      height: 2px;
      transition: transform .2s;
      transform: rotate(45deg);
      background-color: #333;
    }
    p + p {
      transform: rotate(-45deg);
    }
  }
  .success-content {
    display: flex;
    align-items: center;
    justify-content: space-around;
    flex-wrap: wrap;
    position: absolute;
    left: 50%;
    top: 50%;
    transform: translate(-50%,-50%);
    div {
      color: #25A3A8;
    }
  }
  img {
    display: block;
    margin: 0 auto;
  }
  p {
    margin: 24px 0 36px;
  }
  div {
    width: 100%;
    font-size: 20px;
    text-align: center;
  }
}
</style>
