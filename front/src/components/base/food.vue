<template>
  <div class="Stay-food">
    <ul>
      <li v-for="(item, index) in data" :key="index" @touchend="handleView(index)" @touchmove="handleMove">
        <div class="img-box" :style="{backgroundImage: `url(${item.imgs[0]})`}"></div>
        <div class="content">
          <h3>{{ item.name }}</h3>
          <p class="desc">{{ item.detail }}</p>
          <div class="price">
            <div class="tag">
              <ve-tag v-for="obj in tag" :key="obj">{{ obj }}</ve-tag>
            </div>
            <p>人均：<span>￥{{ item.price }}</span></p>
          </div>
          <p class="position">
            <span>{{ position }}</span>
            <span>{{ d }}</span>
          </p>
        </div>
      </li>
    </ul>
  </div>
</template>

<script>
  import veTag from './ve-tag'
  import Storage from '../../utils/localStorage'
  export default {
    name: 'stayFood',
    components: {
      veTag
    },
    data() {
      return {
        tag: ['小吃', '美食', '性价比'],
        position: '重庆邮电大学',
        d: '距您180米',
        isMove: false
      }
    },
    methods: {
      handleView(index) {
        if (this.isMove) {
          this.isMove = false;
          return false
        }
        Storage.set('now_checked_food', this.data[index]);
        this.$router.push({
          path: '/PopHouse/FoodDetail',
          query: {
            bgColor: '#fff',
            direction: 'pop-bottom',
            id: this.data[index].hotel_id
          }
        })
      },
      handleMove() {
        this.isMove = true
      },
    },
    props: {
      data: {
        type: Array,
        default: () => [],
      }
    }
  }
</script>

<style lang="less" scoped>
.Stay-food {
  .img-box {
    width: 100px;
    height: 100px;
    background-position: center;
    background-size: 150%;
    border-radius: 4px;
  }
  li {
    display: flex;
    justify-content: flex-start;
    height: 114px;
    border-bottom: 1px solid #E4ECE8;
    + li {
      margin-top: 16px;
    }
    .content {
      flex: 1;
      margin-left: 20px;
      width: 60%;
      h3 {
        font-weight: 400;
        font-size: 16px;
      }
      .desc {
        color: #8F9895;
        font-size: 12px;
        margin-top: 4px;
        overflow: hidden;
        white-space: nowrap;
        text-overflow: ellipsis;
      }
      .price {
        margin-top: 0.5rem;
        display: flex;
        justify-content: flex-start;
        align-items: center;
        @media screen and (max-width: 375px) {
          & {
            margin-top: 10px;
          }
          .tag {
          }
          > p {
            display: none;
          }
        }
        .tag {
          flex-shrink: 0;
        }
        > p {
          font-size: 14px;
          margin-left: auto;
          width: 94px;
          text-align: right;
          span {
            color: #DB3F1F;
          }
        }
      }
      .position {
        display: flex;
        justify-content: space-between;
        font-size: 12px;
        color: #8F9895;
        margin-top: 12px;
      }
    }
  }
}
</style>
