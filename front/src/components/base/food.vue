<template>
  <div class="Stay-food">
    <ul>
      <li v-for="(item, index) in data" :key="index">
        <div class="img-box" :style="{backgroundImage: `url(${item.imgs[0]})`}"></div>
        <div class="content">
          <h3>{{ item.name }}</h3>
          <p class="desc">{{ item.desc }}</p>
          <div class="price">
            <ve-tag v-for="obj in tag" :key="obj">{{ obj }}</ve-tag>
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
  export default {
    name: 'stayFood',
    components: {
      veTag
    },
    data() {
      return {
        tag: ['小吃', '美食', '性价比'],
        position: '重庆邮电大学',
        d: '距您180米'
      }
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
        margin-top: 1.5rem;
        display: flex;
        justify-content: flex-start;
        align-items: center;
        > p {
          font-size: 14px;
          margin-left: auto;
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
        margin-top: 16px;
      }
    }
  }
}
</style>
