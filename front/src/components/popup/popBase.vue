<template xmlns:v-hammer="http://www.w3.org/1999/xhtml">
  <div class="popBase">
    <div :class="controlStyle">
      <div class="pop-control" v-hammer:tap="handleTap">
        <p></p>
        <p></p>
      </div>
      <span v-if="!$route.path.includes('/priceHouse')">
        <span style="margin-right: 10px" v-if="showTopControl" v-hammer:tap="handleNotSave">不保存并退出</span>
        <span v-if="showTopControl" v-hammer:tap="handleSave">保存并退出</span>
      </span>
    </div>
    <transition appear :name="direction" mode="out-in">
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
        console.log(this.direction)
      }
    },
    methods: {
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
          return this.$router.push({
            path: this.$route.query.back
          })
        }
        const index = path.findIndex(i => this.$route.meta.name === i);
        if (index === 0) {
          this.$router.push({
            path: '/release'
          });
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
  .popBase {
    position: relative;
    width: 100%;
    height: calc(100vh - 14px);
    .pop-control {
      position: relative;
      height: 56px;
      width: 46px;
      top: 18px;
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
      padding: 0 36px;
      span {
        font-size: 12px;
        color: #5F6564;
      }
      p {
        position: absolute;
        top: 8px;
        width: 16px;
        height: 2px;
        background-color: #2E312F;
        transition: transform .2s;
        transform: rotate(45deg);
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
