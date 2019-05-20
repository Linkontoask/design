<template>
  <div class="resultSearch">
    <ul class="house">
      <h5>关于<span>{{ searchString }}</span>热门房源</h5>
      <div v-if="result.hotel_list.length !== 0">
        <li v-for="(item, index) in result['hotel_list']" :key="index" @touchend="handleHouse(item.hotel_id)">{{ item.name }}</li>
      </div>
      <div style="margin-left: 10px" v-else>未发现关于 {{ searchString }}的房源</div>
    </ul>
    <ul class="food">
      <h5>关于<span>{{ searchString }}</span>热门美食</h5>
      <div v-if="result.around_list.length !== 0">
        <li v-for="(item, index) in result.around_list" :key="index" @touchend="handleFood(item.around_id)">
          <img :src="item.imgs[0]" alt="获取图片发生未知错误">
          <p>{{ item.name }}</p>
        </li>
      </div>
      <div style="margin-left: 10px" v-else>未发现关于 {{ searchString }}的美食</div>
    </ul>
  </div>
</template>

<script>
  import axios from '../utils/axios'
  import {mapState, mapMutations} from 'vuex'
  export default {
    name: "resultSearch",
    data() {
      return {
        result: {
          hotel_list: [],
          around_list: []
        }
      }
    },
    computed: {
      ...mapState({
        searchString: state => state.searchString
      }),
    },
    watch: {
      $route(to) {
        this.SEARCH(to.query.params)
      }
    },
    methods: {
      ...mapMutations([
        'SEARCH',
      ]),
      handleHouse(id) {
        this.$router.push({
          name: 'houseDetail',
          query: {
            bgColor: '#fff',
            id
          }
        })
      },
      handleFood(id) {

      }
    },
    async activated() {

    },
    async mounted() {
      this.SEARCH(this.$route.query.params)
      const data = await axios.get.call(this, '/hotel/search_for_all/', {
        search: this.$route.query.params
      });
      this.result = data.data;
      /*const data = await axios.get.call(this, '/t', {});
      this.result = data.data;*/
    }
  }
</script>

<style scoped lang="less">
.resultSearch {
  position: relative;
  width: calc(80% + 40px);
  margin: 110px auto 0;
  .house, .food {
    color: #8F9895;
    > div {
      margin-top: 14px;
    }
    h5 {
      font-weight: normal;
      span {
        font-size: 14px;
        color: #2E3130;
        font-weight: 500;
      }
    }
  }
  .house {
    > div {
      display: flex;
      flex-wrap: wrap;
      margin-left: -10px;
      li {
        border: 1px solid #DCDFE6;
        border-radius: 4px;
        padding: 6px 20px;
        margin-top: 10px;
        margin-left: 10px;
        color: #2E3130;
      }
    }

  }
  .food {
    margin-top: 36px;
    div {
      display: flex;
      justify-content: space-between;
      flex-wrap: wrap;
    }
    li {
      margin-top: 10px;
      p {
        font-size: 14px;
      }
    }
    img {
      width: 180px;
    }
  }
}
</style>
