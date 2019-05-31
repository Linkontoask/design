<template>
  <div id="homeStay">
    <img :class="['qr', isScale]" @click="isScale='isScale'" src="https://avatars2.githubusercontent.com/u/26475695?s=400&u=142d954d23b6a68283e98154836dc5818f3cdd81&v=4" alt="在线二维码">
    <div v-if="isScale" class="mask-qr" @click="isScale=''"></div>
    <!--<icon svg="icon-chef"></icon>-->
    <!--<transition
            name="router-fade"
            mode="out-in"
            @before-enter="handleBeforeEnter"
            @enter="handleEnter"
            @after-enter="handleAfterEnter"
            @before-leave="handleBeforeLeave"
            @leave="handleLeave"
            @after-leave="handleAfterLeave"
    >-->
      <keep-alive :include="['collection', 'homeStayContent', 'msg', 'release', 'user']">
        <router-view/>
      </keep-alive>
    <!--</transition>-->
    <div style="height: 118px" v-if="showActionBar"></div>
    <transition name="action">
      <Action v-if="showActionBar"></Action>
    </transition>
  </div>
</template>

<script>
  import Action from './components/BactionBar'
  import {mapState, mapMutations} from 'vuex'
  const path = ['/login', '/signup', '/pop', '/PopSearch', '/PopHouse', '/success', '/chat', 'welcome', '/DatePicker'];
  export default {
    data() {
      return {
        isScale: ''
      }
    },
    components: {
      Action,
    },
    methods: {
      ...mapMutations([
        'IS_SHOW_NATION',
        'BEFORE_URL'
      ]),
      handleBeforeEnter(el) {
        // console.log('handleBeforeEnter', el)
      },
      handleEnter(el) {
        // console.log('handleEnter', el)
      },
      handleAfterEnter(el) {
        // console.log('handleAfterEnter', el)
      },
      handleBeforeLeave(el) {
        // console.log('handleBeforeLeave', el)
      },
      handleLeave(el) {
        // console.log('handleLeave', el)
      },
      handleAfterLeave(el) {
        // console.log('handleAfterLeave', el)
      },
    },
    watch: {
      $route(to, form) {
        this.IS_SHOW_NATION(!path.some(i => to.path.includes(i)));
        this.BEFORE_URL(form.path);
      }
    },
    mounted() {
      document.querySelector('#loadingStart').style.display = 'none'; // 关闭加载动画
      this.IS_SHOW_NATION(!path.some(i => this.$route.path.includes(i)));
    },
    computed: {
      ...mapState({
        showActionBar: state => state.showActionBar
      }),
    },

  }
</script>

<style lang="less">
#homeStay {
  font-family: PingFangSC-Regular, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  color: #5F6564;
  font-size: 16px;
  .qr {
    position: fixed;
    top: 0;
    right: 0;
    z-index: 9999;
    width: 44px;
    transition: all .3s;
  }
  .qr.isScale {
    width: 80%;
    left: 50%;
    top: 50%;
    transform: translate(-50%, -50%);
  }
  .mask-qr {
    position: fixed;
    left: 0;
    top: 0;
    width: 100vw;
    height: 100vh;
    z-index: 9998;
    background-color: #292929c9;
  }
}
.action-enter-active, .action-leave-active {
  transition: bottom .3s;
}
.action-leave-to {
  bottom: -98px !important;
}
.action-enter-active {
  bottom: -98px !important;
}
.action-enter-to {
  bottom: 0 !important;
}
li {
  list-style-type: none
}
  .medium {
    font-family: PingFangSC-Medium, sans-serif;
  }
  .clamp2 {
    overflow: hidden;
    text-overflow: ellipsis;
    display: -webkit-box;
    -webkit-line-clamp: 2;
    -webkit-box-orient: vertical;
  }
  .clamp1 {
    overflow: hidden;
    text-overflow: ellipsis;
    white-space: nowrap;
  }
</style>
