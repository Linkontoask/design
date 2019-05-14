<template>
  <div class="resultSearch">
    <ul class="house">
      <h5>关于<span>{{ searchString }}</span>热门房源</h5>
      <div>
        <li v-for="(item, index) in result['house']" :key="index" @touchend="handleHouse(item.id)">{{ item.name }}</li>
      </div>
    </ul>
    <ul class="food">
      <h5>关于<span>{{ searchString }}</span>热门美食</h5>
      <div>
        <li v-for="(item, index) in result['food']" :key="index" @touchend="handleFood(item.id)">
          <img :src="item.src" alt="获取图片发生未知错误">
          <p>{{ item.name }}</p>
        </li>
      </div>
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
          house: [{
            name: '一棵树景点房源',
            id: 0
          },{
            name: '洪崖洞 | 解放碑',
            id: 0
          },],
          food: [{
            src: 'http://172.16.1.11/YUN/issues/uploads/4a686fcf5f3e1a205ddb528e244f557c/image.png',
            name: '小龙虾',
            id: 0
          },{
            src: 'http://172.16.1.11/YUN/issues/uploads/4a686fcf5f3e1a205ddb528e244f557c/image.png',
            name: '青椒肉丝',
            id: 0
          },{
            src: 'http://172.16.1.11/YUN/issues/uploads/4a686fcf5f3e1a205ddb528e244f557c/image.png',
            name: '青椒肉丝',
            id: 0
          },]
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

      },
      handleFood(id) {

      }
    },
    async mounted() {
      this.SEARCH(this.$route.query.params)
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
