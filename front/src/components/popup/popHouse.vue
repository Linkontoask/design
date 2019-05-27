<template xmlns:v-hammer="http://www.w3.org/1999/xhtml">
  <div class="popHouse" :class="{dropOut: dropOut}" ref="popHouse">
    <div class="pop-control" :class="control" v-hammer:tap="handleTap">
      <p :style="{backgroundColor: bgColor}"></p>
      <p :style="{backgroundColor: bgColor}"></p>
    </div>
    <transition appear :name="direction" mode="out-in"
                @before-enter="handleBeforeEnter"
                @enter="handleEnter"
                @after-enter="handleAfterEnter"
                @before-leave="handleBeforeLeave"
                @leave="handleLeave"
                @after-leave="handleAfterLeave">
      <keep-alive>
        <router-view :key="$route.fullPath" />
      </keep-alive>
    </transition>
  </div>
</template>

<script>
  import cookie from '../../utils/cookie'
  import Storage from '../../utils/localStorage'
  const ClassIn = ['bounceInUp', 'pulse']
  const ClassOut = ['bounceOutDown', 'bounceOutUp']
  export default {
    name: "popHouse",
    data() {
      return {
        direction: 'pop-bottom',
        bgColor: '#2E312F',
        control: 'left',
        dropOut: false,
      }
    },
    methods: {
      animation(elm, animat) {
        let node = elm;
        node.classList.add(animat, 'faster');
        function handleAnimationEnd() {
          node.classList.remove(animat);
          node.removeEventListener('animationend', handleAnimationEnd)
        }
        node.addEventListener('animationend', handleAnimationEnd)
      },
      loopElm(el, out) {
        try {
          el.childNodes.forEach(item => {
            if (out && item.dataset.out) {
              this.animation(item, item.dataset.out)
            } else if (item.dataset && item.dataset.in) {
              this.animation(item, item.dataset.in)
            }
            /*if (item.childNodes.length !== 0) {
              this.loopElm(item)
            }*/
          })
        } catch (e) {

        }

      },
      handleBeforeEnter(el) {
        this.loopElm(el, false)
      },
      handleEnter(el) {
        // console.log('handleEnter', el)
      },
      handleAfterEnter(el) {
        // console.log('handleAfterEnter', el)
      },
      handleBeforeLeave(el) {
        this.loopElm(el, true)
      },
      handleLeave(el) {
        // console.log('handleLeave', el)
      },
      handleAfterLeave(el) {
        // console.log('handleAfterLeave', el)
      },
      handleTap(ev, query = {}) {
        let url = Storage.get('before_url_house_');
        if (this.$route.query.back) {
          Storage.set('before_url_house_', []);
          this.dropOut = true;
          const node = this.$refs.popHouse,
          vm = this;
          function handleAnimationEnd() {
            vm.dropOut = false;
            node.removeEventListener('transitionend', handleAnimationEnd);
            vm.$router.push({
              name: vm.$route.query.back,
            });
          }
          node.addEventListener('transitionend', handleAnimationEnd);
          return
        }
        if (url) {
          this.$router.push({
            path: url[url.length === 1 ? 0 : (url.length - 1)],
            query: Object.assign({direction: 'pop-left'}, query)
          });
          this.$nextTick(() => {
            url.pop();
            Storage.set('before_url_house_', url);
          });
        }
        if (!url || (url && url.length === 0)) {
          this.dropOut = true;
          const node = this.$refs.popHouse,
            vm = this;
          function transitionendEnd() {
            vm.dropOut = false;
            node.removeEventListener('transitionend', transitionendEnd);
            vm.$router.push({
              path: Storage.get('popHouse_before') || '',
              query: {
                direction: 'pop-bottom'
              }
            })
          }
          node.addEventListener('transitionend', transitionendEnd);

        }
      },
      normalVal(to) {
        this.bgColor = to.query.bgColor || '#2E312F';
        this.direction = to.name === 'houseDetail' || to.name === 'StoryDetail' ? '' : (to.query.direction || 'pop-right');
        this.control = to.query.control || 'left';
      },
    },
    beforeRouteUpdate (to, from, next) {
      let url = Storage.get('before_url_house_') || [];
      url.push(from.fullPath);
      url = [...new Set(url)];
      Storage.set('before_url_house_', url);
      next()
    },
    watch: {
      $route(to, form) {
        this.normalVal(to)
      }
    },
    computed: {

    },
    destroyed() {
      Storage.remove('before_url_house_')
    },
    mounted() {
      this.normalVal(this.$route)
    }
  }
</script>

<style scoped lang="less">
.popHouse.dropOut {
  position: relative;
  top: 100vh;
}
.popHouse {
  transition: top .3s;
  overflow-x: hidden;
  top: 0;
  .pop-control {
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
