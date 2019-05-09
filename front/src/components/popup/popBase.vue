<template xmlns:v-hammer="http://www.w3.org/1999/xhtml">
  <div class="popBase">
    <div :class="controlStyle">
      <div class="pop-control" v-hammer:tap="handleTap">
        <p></p>
        <p></p>
      </div>
      <span>
        <span style="margin-right: 10px" v-if="$route.meta.name !== 'type'" v-hammer:tap="handleNotSave">不保存并退出</span>
        <span v-if="$route.meta.name !== 'type'" v-hammer:tap="handleSave">保存并退出</span>
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
      handleNotSave() {
        window.localStorage.removeItem('current_hotel');
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
        const index = path.findIndex(i => this.$route.meta.name === i);
        if (index === 0) {
          this.$router.push({
            path: '/release'
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
      this.direction = 'pop-' + this.$route.query.direction;
      this.controlStyle = this.$route.path.includes('/type') ? 'close' : 'left'
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
  .pop-right-enter-active, .pop-right-leave-active, .pop-left-leave-active, .pop-left-leave-active {
    transition: left .3s, opacity .3s;
  }
  .pop-left-enter-active {
    left: -100%;
    opacity: 0;
  }
  .pop-left-leave-active {
    left: 0;
    opacity: 1;
  }
  .pop-left-leave-to {
    left: 100%;
    opacity: 0;
  }
  .pop-left-enter-to {
    left: 0;
    opacity: 1;
  }
  .pop-right-enter-active {
    left: 100%;
    opacity: 0;
  }
  .pop-right-leave-active {
    left: 0;
    opacity: 1;
  }
  .pop-right-leave-to {
    left: -100%;
    opacity: 0;
  }
  .pop-right-enter-to {
    left: 0;
    opacity: 1;
  }
  .pop-bottom-enter-active, .pop-bottom-leave-active {
    transition: top .3s, opacity .3s;
  }
  .pop-bottom-enter-active {
    top: 100vh;
    opacity: 0;
  }
  .pop-bottom-leave-active {
    top: 0;
    opacity: 1;
  }
  .pop-bottom-leave-to {
    top: 100vh;
    opacity: 0;
  }
  .pop-bottom-enter-to {
    top: 0;
    opacity: 1;
  }
  .popBase {
    position: relative;
    width: 100%;
    height: calc(100vh - 14px);
    .pop-control {
      position: relative;
      height: 46px;
      width: 46px;
      top: 10px;
    }
    .close, .left {
      display: flex;
      justify-content: space-between;
      align-items: center;
      margin-top: 12px;
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
