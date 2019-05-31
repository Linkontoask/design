<template>
  <div class="popSearch">
    <div class="close" @touchend="handleClose">取消</div>
    <div class="search-top" style="top: 64px;">
      <form @submit.prevent="formSubmit" action="javascript:return true">
        <input style="background-color: white" type="search" @blur="handleBlur" @keyup.enter="handleSearch" v-model="str" ref="input" aria-placeholder="输入城市、房源名" placeholder="输入城市、房源名">
      </form>
      <div class="btn-search" @touchend="handleSearch">搜索</div>
    </div>
    <transition :name="direction">
      <router-view :key="$route.fullPath" />
    </transition>
  </div>
</template>

<script>
  import Storage from '../../utils/localStorage'
  import {mapState, mapMutations} from 'vuex'
  export default {
    name: "popSearch",
    data() {
      return {
        str: '',
        direction: 'pop-left'
      }
    },
    computed: {
      ...mapState({
        searchString: state => state.searchString
      }),
    },
    watch: {
      searchString(val) {
        this.str = val;
        this.handleSearch()
      },
      $route(to) {
        this.direction = to.path.includes('normalSearch') ? 'pop-left' : 'pop-right'
      }
    },
    methods: {
      ...mapMutations([
        'SEARCH',
      ]),
      formSubmit() {
        return false;
      },
      handleSearch() {
        if (this.str === '') {
          return false;
        }
        this.$refs.input.blur();
        let searched_  = Storage.get('searched_');
        if (searched_) {
          searched_.push(this.searchString)
        } else {
          searched_ = [this.searchString]
        }
        searched_ = [...new Set(searched_)];
        Storage.set('searched_', searched_);
        this.$router.push({
          path: '/PopSearch/resultSearch',
          query: {
            params: this.str
          }
        })
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
      if (!this.$route.path.includes('resultSearch')) this.$refs.input.focus()
    }
  }
</script>

<style scoped lang="less">
  .popSearch {
    .close {
      position: fixed;
      top: 16px;
      right: 6%;
      text-align: right;
      height: 32px;
      line-height: 32px;
      font-size: 14px;
    }
  }
</style>
