<template>
  <div class="stay-house">
    <ul>
      <li v-for="(item, index) in data" :key="index">
        <img :src="require('../../static/img/' + item.src)" alt="not find img">
        <div class="house-content">
          <p class="content-1">
            <span class="medium">{{ item.title }}</span>
            <span>{{ item.position }}</span>
          </p>
          <div class="content-2 clamp2">{{ item.desc }}</div>
          <div class="content-3">
            <strong>{{ item.price }}</strong>
            <p>{{ item.oldPrice }}</p>
          </div>
        </div>
      </li>
    </ul>
  </div>
</template>

<script>
  export default {
    name: 'stayHouse',
    props: {
      data: {
        type: Array,
        default: []
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
      width: 178px;
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
