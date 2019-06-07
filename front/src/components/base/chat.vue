<template xmlns:v-hammer="http://www.w3.org/1999/xhtml">
  <transition name="right">
    <div class="chat" ref="chat" v-show="showChat" v-hammer:swipe.right="handleSwiper">
      <div class="top">
        <div class="control close" @touchend="handleClose"><p></p><p></p></div>
        <h3>{{ name }}</h3>
      </div>
      <div class="chat-content" ref="contentBox">
        <ul ref="content">
          <li v-for="(item, index, key) in chatRecord" :key="index" :class="item.own ? 'own' : 'other'">
            <img v-if="item.avatar" class="avatar" :src="require('../../assets/'+item.avatar)" alt="">
            <div class="content" v-html="item.content"></div>
          </li>
          <p ref="bottom"></p>
        </ul>
      </div>
      <div class="input">
        <div class="input-type">
          <img :src="require('../../assets/' + img)" alt="">
        </div>
        <div class="input-style">
          <form @submit.prevent="formSubmit" action="javascript:return true">
            <input name="done" ref="text" v-model="txt" @focus="getInputFocusScrollY" @keyup.enter="handleSend" @blur="setWindowScrollY">
          </form>
        </div>
        <div class="input-send">
          <div class="btn" @click="handleSend">发送</div>
        </div>
      </div>
    </div>
  </transition>
</template>

<script>
  import axios from '../../utils/axios'
  import Storage from '../../utils/localStorage'
  import BScroll from 'better-scroll'
  export default {
    name: "chat",
    data() {
      return {
        user: {
          name: 'Link'
        },
        txt: '',
        scroll: null,
        lastScrollY: 0,
        img: 'audio.png',
        chatRecord: [{content: '您好', avatar: 'avatar-1.png'}, {content: '这是一款关于<strong>民宿服务类型</strong>的APP，每个用户都可以上传<span>美食</span>、<span>故事</span>以及<span>房源</span>，如果有人预定你发布的房源那么在 <a href="/front-hotel/#/user">“我”的界面中</a>会看到余额增加，如果你预定了其他人的房源并且支付成功那么你的积分也会有一定的增加。赶快去体验一下吧。有什么不合理的地方或体验不好的地方可在反馈界面进行反馈，祝您旅途愉快', avatar: 'avatar-1.png'}]
      }
    },
    props: {
      name: {
        type: String,
      },
      showChat: {
        type: Boolean,
        default: false
      }
    },
    watch: {
      showChat(val) {
        if (val && !this.scroll) {
          this.init()
        }
      }
    },
    methods: {
      formSubmit() {
        return false;
      },
      handleSwiper() {
        this.$emit('close')
      },
      scrollBottom() {
        this.$nextTick(() => {
          const _this = this;
          let y = this.$refs.content.clientHeight - this.scroll.wrapperHeight;
          if (y <= 0) {
            return false;
          }
          this.scroll && this.scroll.refresh();
          _this.scroll.scrollBy(0, -90, 200);
        });
      },
      async handleSend() {
        this.$refs.text.focus();
        if (this.txt !== '') {
          this.chatRecord.push({
            own: true,
            content: this.txt,
            avatar: this.user.avatar
          })
          const t = this.txt;
          this.txt = '';
          this.scrollBottom();
          const audio = new Audio(require('../../static/information.mp3')) // 'http://gddx.sc.chinaz.com/Files/DownLoad/sound1/201706/8855.wav'
          const data = await axios.get.call(this, `/hotel/chat/?msg=${t}`);
          this.chatRecord.push({
            own: false,
            content: data.content,
            avatar: 'avatar-1.png'
          });
          navigator.vibrate = navigator.vibrate || navigator.webkitVibrate || navigator.mozVibrate || navigator.msVibrate;
          try {
            navigator.vibrate(10);
          } catch (e) {

          }
          audio.play();
          this.scrollBottom();
        }
      },
      handleClose() {
        this.$emit('close')
      },
      init() {
        this.$nextTick(() => {
          this.scroll = new BScroll(this.$refs.contentBox, {
            scrollX: false,
            scrollY: true,
            momentum: true,
            bounce: true,
          });
        })
      }
    },
    async beforeMount() {

    },
    async mounted() {
      if (Storage.get('user_info_')) {
        this.user.avatar = Storage.get('user_info_').avatar;
      } else {
        const data = await axios.get.call(this, '/hotel/user_info/', {});
        Storage.set('user_info_', data.data);
        this.user.avatar = data.data.avatar;
      }

      this.$nextTick(() => {
        if (!this.showChat) return;
        this.init()
      })
    }

  }
</script>

<style scoped>
  .content>>>span {
    color: #FE5656;
  }
  .content>>>a {
    color: #25A3A8;
  }
</style>
<style scoped lang="less">
  @h: 42px;
  .right-enter-active {
    left: 100% !important;
  }
  .right-enter-to {
    left: 0 !important;
  }
  .right-leave-active {
    left: 0 !important;
  }
  .right-leave-to {
    left: 100% !important;
  }
.chat {
  width: 100%;
  height: 100vh;
  overflow: auto;
  background-color: #F5F5F5;
  position: fixed;
  top: 0;
  left: 0;
  transition: left .3s;
  z-index: 2001;
  .input {
    position: fixed;
    bottom: 0;
    left: 0;
    width: calc(100% - 24px);
    height: 46px;
    background-color: white;
    padding: 10px 12px;
    display: flex;
    align-items: center;
    > div {
      height: @h;
    }
    .input-type {
      width: 56px;
      flex-shrink: 0;
      display: flex;
      align-items: center;
      justify-content: space-around;
      img {
        width: 26px;
      }
    }
    .input-style {
      flex-grow: 1;
      input {
        width: calc(100% - 16px);
        height: @h;
        border: 1px solid #E3E9E6;
        border-radius: 4px;
        outline: none;
        font-size: 16px;
        padding: 0 8px;
        color: #313332;
      }
    }
    .input-send {
      width: 86px;
      flex-shrink: 0;
      background-color: #25A3A8;
      color: white;
      border-radius: 4px;
      text-align: center;
      line-height: @h;
      margin-left: 10px;
    }
  }
  .chat-content {
    height: calc(100% - 126px);
    ul {
      padding: 24px 24px;
      li {
        display: flex;
        img.avatar {
          width: 42px;
          height: 42px;
          border-radius: 50%;
          margin-right: 12px;
          flex-shrink: 0;
        }
        div.content {
          position: relative;
          border-radius: 4px;
          padding: 10px;
          background-color: white;
          border: 1px solid #E3E9E6;
          font-size: 16px;
          word-break: break-all;
          direction: ltr;
        }
        div.content::before, div.content::after {
          content: '';
          position: absolute;
          left: -24px;
          top: 8px;
          width: 0;
          height: 0;
          border: 12px solid transparent;
          border-right: 12px solid #E3E9E6;
        }
        div.content::after {
          left: -23px;
          border-right-color: #fff;
        }
      }
      li.own {
        direction: rtl;
        div.content {
        }
        div.content::before, div.content::after {
          left: auto;
          right: -24px;
          border: 12px solid transparent;
          border-left: 12px solid #E3E9E6;
        }
        div.content::after {
          right: -23px;
          border-left-color: #fff;
        }
        img.avatar {
          margin-left: 12px;
          margin-right: 0;
        }
      }
      li + li {
        margin-top: 24px;
      }
    }
  }
  .top {
    height: 60px;
    background-color: white;
    display: flex;
    align-items: center;
    border-bottom: 1px solid #E4ECE8;
    z-index: 9;
    position: relative;
    h3 {
      flex: 1;
      text-align: center;
      font-size: 16px;
    }
  }
  .control {
    position: absolute;
    top: 14px;
    left: 8px;
    height: 36px;
    width: 46px;
  }
  .close, .left {
    display: flex;
    justify-content: space-between;
    align-items: center;
    z-index: 2;
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
}
</style>
