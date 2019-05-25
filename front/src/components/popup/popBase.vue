<template xmlns:v-hammer="http://www.w3.org/1999/xhtml">
  <div class="popBase" ref="popBase">
    <div class="pop-base-control">
      <div class="pop-control" :class="controlStyle" v-hammer:tap="handleTap">
        <p></p>
        <p></p>
      </div>
      <span v-if="!$route.path.includes('/priceHouse')">
        <span style="margin-right: 10px" v-if="showTopControl" v-hammer:tap="handleNotSave">不保存并退出</span>
        <span v-if="showTopControl" v-hammer:tap="handleSave">保存并退出</span>
      </span>
    </div>
    <transition appear :name="direction" mode="out-in"
                @before-enter="handleBeforeEnter"
                @enter="handleEnter"
                @after-enter="handleAfterEnter"
                @before-leave="handleBeforeLeave"
                @leave="handleLeave"
                @after-leave="handleAfterLeave">
      <router-view/>
    </transition>
  </div>
</template>

<script>
  import {mapState} from 'vuex'
  const path = [
    'type',
    'newHouse',
    'confirmHouse',
    'styleHouse',
    'descHouse',
    'ruleHouse',
    'facilityHouse',
    'rimHouse',
    'priceHouse'];
  export default {
    name: "popBase",
    computed: {
      ...mapState({
        beforeUrl: state => state.beforeUrl
      }),
      showTopControl() {
        return !['type', 'releaseFood', 'releaseStory', 'newHouse'].includes(this.$route.meta.name)
      }
    },
    data() {
      return {
        direction: 'pop-bottom',
        controlStyle: 'close',
      }
    },
    watch: {
      $route(to, from) {
        this.direction = 'pop-' + (to.query.direction || 'bottom');
        this.controlStyle = to.path.includes('/type') ? 'close' : 'left'
      }
    },
    methods: {
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
      handleSwiper(ev) {
        console.log(ev)
        if (ev.type === 'swiperight') {
          this.handleTap()
        }
      },
      handleNotSave() {
        this.$nextTick(() => {
          window.localStorage.removeItem('current_hotel');
          setTimeout(() => {window.localStorage.removeItem('houseData')}, 1000)
        });
        this.$router.push({
          path: '/release'
        })
      },
      handleSave() {
        window.localStorage.setItem('current_hotel', this.$route.path);
        this.$router.push({
          path: '/release'
        })
      },
      handleTap() {
        if (this.$route.query.back) {
          const node = this.$refs.popBase,
            vm = this;
          node.classList.add('UpBottom');
          function transitionend() {
            node.classList.remove('UpBottom');
            node.removeEventListener('animationend', transitionend);
            vm.$router.push({
              name: vm.$route.query.back,
            });
          }
          node.addEventListener('animationend', transitionend);
          return
        }
        const index = path.findIndex(i => this.$route.meta.name === i);
        if (index === 0) {
          const node = this.$refs.popBase,
          vm = this;
          node.classList.add('UpBottom');
          function handleAnimationEnd() {
            node.classList.remove('UpBottom');
            vm.$router.push({
              path: '/release'
            });
            node.removeEventListener('animationend', handleAnimationEnd)
          }

          node.addEventListener('animationend', handleAnimationEnd)
        } else if (this.$route.meta.name === 'releaseFood' || this.$route.meta.name === 'releaseStory') {
          this.$router.push({
            path: '/pop/type',
            query: {
              direction: 'left'
            }
          });
        } else this.$router.push({
          path: path[index - 1],
          query: {
            direction: 'left'
          }
        });
      }
    },
    beforeMount() {

    },
    mounted() {

    },
    activated() {
      this.direction = 'pop-' + this.$route.query.direction;
      this.controlStyle = this.$route.path.includes('/type') ? 'close' : 'left'
    }
  }
</script>

<style scoped lang="less">
  @keyframes UpBottom {
    0% {margin-top: 0;}
    100% {margin-top: 100vh;}
  }
  div.UpBottom {
    animation: UpBottom .3s ease-out forwards;
  }
  .popBase {
    position: relative;
    width: 100%;
    height: calc(100vh - 14px);
    .pop-base-control {
      display: flex;
      align-items: center;
      height: 68px;
      justify-content: space-between;
      span {
        margin-left: auto;
        font-size: 12px;
      }
      span + span {
        margin-right: 24px;
      }
    }
    & > div:last-child {
      padding-top: 32px;
    }
    .pop-control {
      position: absolute;
      top: 14px;
      left: 8px;
      height: 36px;
      width: 46px;
    }
    .pop-box {
    }
    @media screen and (max-width: 320px) {
      div.close, div.left {
        padding: 0 12px;
      }
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
    div.left {
      p {
        width: 14px;
        transform: rotate(-45deg);
      }
      p + p {
        transform: rotate(45deg);
        top: 17px;
      }
    }
  }
</style>
