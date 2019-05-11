<template>
  <div id="homeStay">
    <transition name="router-fade" mode="out-in">
      <keep-alive :include="['collection', 'homeStayContent', 'msg', 'release', 'user']">
        <router-view/>
      </keep-alive>
    </transition>
    <div style="height: 118px" v-if="showActionBar"></div>
    <Action v-if="showActionBar"></Action>
  </div>
</template>

<script>
  import Action from './components/BactionBar'
  import {mapState, mapMutations} from 'vuex'
  const path = ['/login', '/signup', '/pop'];
  export default {
    data() {
      return {

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
    },
    watch: {
      $route(to, form) {
        this.IS_SHOW_NATION(!path.some(i => to.path.includes(i)));
        this.BEFORE_URL(form.path);
      }
    },
    mounted() {
      this.IS_SHOW_NATION(!path.some(i => this.$route.path.includes(i)))
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
  height: 100%;
}
html, body {
  height: 100%;
}
*{
  margin: 0;
  padding: 0
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
.router-fade-enter-active, .router-fade-leave-active {
  transition: opacity .3s;
}
.router-fade-enter, .router-fade-leave-active {
  opacity: 0;
}
</style>
