<template>
  <div class="normalSearch">
    <div class="searched">
      <ul>
        <li v-for="(item, index) in searchStr" :key="index" @click="handleOld(item)">
          {{ item }}
        </li>
      </ul>
    </div>
    <div class="search-content">
      <ly-tab
        v-model="current"
        @change="handleNav"
        :items="recommend"
        :options="{labelKey: 'city', activeColor: '#25A3A8'}">
      </ly-tab>
      <swiper :options="swiperOption" ref="city" class="swiper-content">
        <swiper-slide v-for="(item, index) in recommend" :key="index">
          <div class="swiper-slide-content" v-for="(obj, i) in item.content" :key="i" @click="handleView(obj, item.id)">
            <h5>{{ obj.name }}</h5>
            <div>
              <p v-if="item.id === 1">{{ obj.position }}</p>
              <p v-if="item.id === 1 && obj.detail !== ''">{{ obj.detail }}</p>
              <p>{{ obj.price }}</p>
            </div>
          </div>
        </swiper-slide>
      </swiper>
    </div>
    <div class="city">
      <h3>热门目的地城市</h3>
      <ul>
        <li v-for="(item, index) in citys" :key="index" @touchend="handleCity(item)">{{ item }}</li>
      </ul>
    </div>
  </div>
</template>

<script>
  import Storage from '../utils/localStorage'
  import axios from '../utils/axios'
  import { mapMutations } from 'vuex'
  export default {
    name: "normalSearch",
    data() {
      return {
        searchStr: Storage.get('searched_'),
        current: 0,
        swiperOption: {
          slidesPerView: 'auto',
          spaceBetween: 24,
          on: {
            slideChange: () => {
              this.current = this.$refs.city.swiper.activeIndex
            },
          },
        },
        recommend: [
          {id: 1, city: '热门民宿', content: []},
          {id: 2, city: '热门美食', content: []},
        ],
        citys: ['北京', '重庆', '上海', '南京', '成都', '广州']
      }
    },
    methods: {
      ...mapMutations([
        'SEARCH',
      ]),
      handleView(item, id) {
        if (id === 1) {
          Storage.set('now_checked_house', item);
          this.$router.push({
            name: 'houseDetail',
            query: {
              bgColor: '#fff',
              id: item.hotel_id,
              back: this.$route.name
            }
          })
        } else {
          Storage.set('now_checked_food', item);
          this.$router.push({
            path: '/PopHouse/FoodDetail',
            query: {
              bgColor: '#fff',
              direction: 'pop-bottom',
              back: this.$route.name,
              id: item.hotel_id
            }
          })
        }

      },
      handleOld(str) {
        this.$router.push({
          path: '/PopSearch/resultSearch',
          query: {
            params: str
          }
        })
      },
      handleCity(item) {
        this.SEARCH(item)
      },
      handleBlur() {

      },
      handleNav(item, index) {
        this.$refs.city.swiper.slideTo(index, 300, false);
      }
    },
    async mounted() {
      const food = await axios.get.call(this, '/hotel/get_around/', {is_all: 'yes'});
      const house = await axios.get.call(this, '/hotel/get_hotel/', {is_all: 'yes'});
      this.recommend[0].content = house.data.slice(0, 6);
      this.recommend[1].content = food.data.slice(0, 4);
    }
  }
</script>

<style scoped lang="less">
.normalSearch {
  position: relative;
  width: calc(80% + 40px);
  margin: 0 auto;
  .searched {
    margin-top: 140px;
    overflow: hidden;
    ul {
      display: flex;
      align-items: center;
      width: 100%;
      overflow: auto;
      li {
        flex-shrink: 0;
        padding: 10px 20px;
        border-radius: 4px;
        border: 1px solid #E4ECE8;
      }
      li + li {
        margin-left: 20px;
      }
    }
  }
  .search-content {
    margin-top: 24px;
    .swiper-content {
      margin-top: 24px;
      .swiper-slide-content {
        padding-bottom: 8px;
        border-bottom: 1px solid #E4E7ED;
        h5 {
          color: #303133;
          font-size: 14px;
          font-weight: normal;
        }
        > div {
          margin-top: 8px;
          display: flex;
          align-items: center;
          p {
            font-size: 12px;
            color: #909399;
          }
          p:first-child {
            margin-right: 20px;
          }
        }
        & + .swiper-slide-content{
          margin-top: 24px;
        }
      }
    }
  }
  .city {
    margin-top: 24px;
    padding-bottom: 36px;
    h3 {
      color: #5D5D5D;
      font-size: 16px;
      font-weight: normal;
    }
    ul {
      margin-top: 14px;
      display: flex;
      flex-wrap: wrap;
      margin-left: -10px;
      li {
        border: 1px solid #DCDFE6;
        border-radius: 4px;
        padding: 6px 20px;
        margin-top: 10px;
        margin-left: 10px;
      }
      li + li {

      }
    }
  }
}
</style>
