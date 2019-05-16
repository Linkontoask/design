<template>
  <div class="houseFacility">
    <h3>更多设施</h3>
    <div class="box">
      <h5>基本设施</h5>
      <ul>
        <li v-for="(item, index) in facility.base" :key="index">
          <img :src="item.img" alt="">
          <p>{{ item.name }}</p>
        </li>
      </ul>
    </div>
    <div class="box">
      <h5>用餐</h5>
      <ul>
        <li v-for="(item, index) in facility.food" :key="index">
          <img :src="item.img" alt="">
          <p>{{ item.name }}</p>
        </li>
      </ul>
    </div>
    <div class="box">
      <h5>娱乐</h5>
      <ul>
        <li v-for="(item, index) in facility.happy" :key="index">
          <img :src="item.img" alt="">
          <p>{{ item.name }}</p>
        </li>
      </ul>
    </div>
    <div class="box">
      <h5>安全设施</h5>
      <ul>
        <li v-for="(item, index) in facility.safety" :key="index">
          <img :src="item.img" alt="">
          <p>{{ item.name }}</p>
        </li>
      </ul>
    </div>
  </div>
</template>

<script>
  export default {
    name: "houseFacility",
    data() {
      return {
        facility: []
      }
    }
  }
</script>

<style scoped lang="less">
.houseFacility {
  padding: 84px 36px 0;
  .box {
    margin-top: 24px;
    padding-bottom: 24px;
    border-bottom: 1px solid #E4ECE8;
  }
}
</style>
