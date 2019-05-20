<template xmlns:v-hammer="http://www.w3.org/1999/xhtml">
  <div class="popHouse">
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
        direction: '',
        bgColor: '#2E312F',
        control: 'left'
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
        if (this.$route.query.back !== '') {
          Storage.set('before_url_house_', []);
          return this.$router.push({
            name: this.$route.query.back,
          });
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
          this.$router.push({
            path: Storage.get('popHouse_before') || '',
            query: {
              direction: 'pop-bottom'
            }
          })
        }
      },
      normalVal(to) {
        this.bgColor = to.query.bgColor || '#2E312F';
        this.direction = to.query.direction || 'pop-right';
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
.popHouse {
  overflow-x: hidden;
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
