<template>
  <div class="popSearch">
    <div class="close" @touchend="handleClose">取消</div>
    <div class="search-top" style="top: 64px;">
      <input type="text" @blur="handleBlur" v-model="searchString" ref="input" aria-placeholder="输入城市、房源名" placeholder="输入城市、房源名">
      <div class="btn-search" @touchend="handleSearch">搜索</div>
    </div>
    <transition name="pop-bottom">
      <router-view />
    </transition>
  </div>
</template>

<script>
  import Storage from '../../utils/localStorage'
  export default {
    name: "popSearch",
    data() {
      return {
        searchString: this.$route.query.params
      }
    },
    computed: {
    },
    methods: {
      handleSearch() {
        let searched_  = Storage.get('searched_');
        if (searched_) {
          searched_.push(this.searchString)
        } else {
          searched_ = [this.searchString]
        }
        searched_ = [...new Set(searched_)];
        Storage.set('searched_', searched_)
      },
      handleBlur() {

      },
      handleClose() {
        this.$router.push({
          path: '/homeStay'
        })
      }
    },
    mounted() {
      this.$refs.input.focus()
    }
  }
</script>

<style scoped lang="less">
  .popSearch {
    .close {
      text-align: right;
      margin-right: 6%;
      height: 32px;
      line-height: 32px;
      margin-top: 16px;
      font-size: 14px;
    }
  }
</style>
