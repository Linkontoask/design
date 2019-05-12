<template>
  <div class="normalSearch">
    <div class="searched">
      <ul>
        <li v-for="(item, index) in searchStr" :key="index">
          {{ item }}
        </li>
      </ul>
    </div>
    <div class="search-content">
      <ly-tab
        v-model="current"
        @change="handleNav"
        :items="citys"
        :options="{labelKey: 'city', activeColor: '#25A3A8'}">
      </ly-tab>
      <swiper :options="swiperOption" ref="city" class="swiper-content">
        <swiper-slide v-for="(item, index) in citys" :key="index">
          <div class="swiper-slide-content" v-for="(obj, i) in item['content']" :key="i">
            <h5>{{ obj.name }}</h5>
            <div>
              <p>{{ obj.pos }}</p>
              <p>{{ obj.price }}</p>
            </div>
          </div>
        </swiper-slide>
      </swiper>
    </div>
  </div>
</template>

<script>
  import Storage from '../utils/localStorage'
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
        citys: [
          {id: '', city: '热门民宿', content: [{
              name: '民宿名称，可能很长', pos: '重庆', price: 235
            },{
              name: '重庆洪崖洞', pos: '重庆', price: 235
            },{
              name: '重庆一棵树，解放碑', pos: '重庆', price: 235
            },]},
          {id: '', city: '热门美食', content: [{
              name: '美食名字', pos: '美食地点', price: 235
            }]},
        ],
      }
    },
    methods: {
      handleBlur() {

      },
      handleNav(item, index) {
        this.$refs.city.swiper.slideTo(index, 300, false);
      }
    },
    mounted() {

    }
  }
</script>

<style scoped lang="less">
.normalSearch {
  width: calc(80% + 40px);
  margin: 0 auto;
  .searched {
    margin-top: 110px;
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
    margin-top: 36px;
    .swiper-content {
      margin-top: 36px;
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
          p + p {
            margin-left: 20px;
          }
        }
        & + .swiper-slide-content{
          margin-top: 24px;
        }
      }
    }
  }
}
</style>
