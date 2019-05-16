<template xmlns:v-hammer="http://www.w3.org/1999/xhtml">
  <div class="popHouse">
    <div class="pop-control" :class="control" v-hammer:tap="handleTap">
      <p :style="{backgroundColor: bgColor}"></p>
      <p :style="{backgroundColor: bgColor}"></p>
    </div>
    <transition appear :name="direction" mode="out-in">
      <keep-alive>
        <router-view :key="$route.fullPath" />
      </keep-alive>
    </transition>
  </div>
</template>

<script>
  import cookie from '../../utils/cookie'
  import Storage from '../../utils/localStorage'
  export default {
    name: "popHouse",
    data() {
      return {
        direction: 'pop-bottom',
        bgColor: '#2E312F',
        control: 'left'
      }
    },
    methods: {
      handleTap(ev, query = {}) {
        let url = Storage.get('before_url_house_');
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
    mounted() {
      this.normalVal(this.$route)
    }
  }
</script>

<style scoped lang="less">
.popHouse {
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
