<template>
  <div class="book-house">
    <div class="top">
      <img :src="house.imgs[0]" alt="">
      <div>
        <h3>{{ house.name }}</h3>
        <p>{{ house.hose_type }}</p>
      </div>
    </div>
    <div style="overflow: auto;position:relative;height: 402px;padding-bottom: 36px;">
      <transition name="pop-right">
        <router-view />
      </transition>
    </div>
  </div>
</template>

<script>
  import axios from '../../../utils/axios'
  import Storage from '../../../utils/localStorage'
  import first from './bookFrist'
  import last from './lastBook'
  export default {
    name: '',
    data() {
      return {
        house: {imgs: []},
        component: first
      }
    },
    methods: {
      tab() {
        this.component = last
      }
    },
    mounted() {

    },
    activated() {
      this.house = Storage.get('now_checked_house') || {};
    },
    beforeMount() {

    }
  }
</script>

<style scoped lang="less">
.book-house {
  position: relative;
  height: calc(100vh - 80px);
  .top {
    margin-top: 84px;
    padding: 0 36px 24px;
    border-bottom: 1px solid #E4ECE8;
    height: 80px;
    display: flex;
    img {
      width: 120px;
    }
    div {
      margin-left: 20px;
    }
    p {
      font-size: 14px;
      color: #8F9895;
      margin-top: 8px;
    }
  }

}
</style>
