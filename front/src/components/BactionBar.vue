<template>
  <div class="bottom-action-bar">
    <ul class="flex">
      <li v-for="(item, index) in action" :key="index" :class="{active: $route.path.includes(item.index)}" @click="handleJump(item)">
        <img :src="require('../assets/' + ($route.path.includes(item.index) ? item.focusIcon : item.icon))" :alt="item.index">
        <h5>{{ item.title }}</h5>
      </li>
    </ul>
  </div>
</template>

<script>
  import action from '../static/BactionBar'
  import {mapState, mapMutations} from 'vuex'

  export default {
    name: 'action',
    data() {
      return {
        action: action
      }
    },
    watch: {

    },
    methods: {
      handleJump(item) {
        this.$router.push({
          path: item.index
        })
      }
    },
    beforeMount() {

    },
    mounted() {

    },
    beforeCreate() {

    }
  }
</script>

<style lang="less" scoped>
  @import "../style/global";
.bottom-action-bar {
  position: fixed;
  bottom: 0;
  left: 0;
  width: 100%;
  border-top: 1px solid #E3E9E6;
  z-index: 9;
  background-color: white;
  .flex {
    display: flex;
    height: 6.25rem - @topIndicator;
    justify-content: space-between;
    align-items: flex-start;
    padding: 1rem 2.25rem;
    .active {
      color: #25A3A8;
    }
    img {
      width: 1.5rem;
    }
    h5 {
      text-align: center;
      margin-top: 0.5rem;
      font-size: 0.75rem;
      font-weight: 400;
    }
  }
}
</style>
