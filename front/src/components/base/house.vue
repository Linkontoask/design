<template xmlns:v-hammer="http://www.w3.org/1999/xhtml">
  <div class="stay-house">
    <ul>
      <li v-for="(item, index) in data" :key="index" v-hammer:tap="handleView">
        <img :src="item.imgs[0]" alt="not find img">
        <div class="house-content">
          <p class="content-1">
            <span class="medium clamp1">{{ item.name }}</span>
            <span>{{ item.position.slice(0, 2) }}</span>
          </p>
          <div class="content-2 clamp2">{{ item.host_desc ? item.host_desc : '没有此房源的描述信息' }}</div>
          <div class="content-3">
            <strong>{{ item.price }}</strong>
            <p>{{ item.price + Math.floor(Math.random() * 100 + 20) }}</p>
          </div>
        </div>
      </li>
    </ul>
  </div>
</template>

<script>
  import Storage from '../../utils/localStorage'
  export default {
    name: 'stayHouse',
    props: {
      data: {
        type: Array,
        default: () => []
      }
    },
    methods: {
      handleView() {
        Storage.set('now_checked_house', this.data);
        this.$router.push({
          path: '/PopHouse/houseDetail',
          query: {
            bgColor: '#fff',
            direction: 'pop-bottom'
          }
        })
      }
    }
  }
</script>

<style lang="less" scoped>
.stay-house {
  ul {
    display: flex;
    justify-content: space-between;
    flex-wrap: wrap;
    li {
      width: 48%;
      margin-top: 24px;
      > img {
        width: 100%;
        border-radius: 4px;
      }
      .house-content {
        font-size: 14px;
        .content-1 {
          display: flex;
          align-items: center;
          justify-content: space-between;
          span:last-child {
            color: #8F9895;
            font-size: 12px;
            width: 24px;
            display: block;
            flex-shrink: 0;
          }
        }
        .content-2 {
          font-size: 12px;
          margin-top: 4px;
          line-height: 1.6;
        }
        .content-3 {
          display: flex;
          justify-content: flex-start;
          align-items: center;
          margin-top: 8px;
          color: #EB0C0C;
          p {
            margin-left: 20px;
            color: #5F6564;
            font-size: 10px;
            text-decoration: line-through;
          }
        }
      }
    }
  }

}
</style>
