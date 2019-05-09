<template>
  <div class="styleHouse">
    <h1>您的房源是什么样子的</h1>
    <div class="styleHouse-box new-box">
      <div class="titleInput">
        <p>房源类型</p>
        <div class="simulation-input" @click="handleCheckType">
          <i v-if="!data.type">房源的建筑类型</i>
          <p v-else>{{ data.type }}</p>
        </div>
      </div>
    </div>
    <list :data="lists" :ckeck="check" v-if="showList" @change="handleChange"></list>
  </div>
</template>

<script>
  import list from '../../base/list'
  export default {
    name: 'styleHouse',
    components: {
      list
    },
    data() {
      return {
        showList: false,
        check: 0,
        data: {
          type: ''
        },
        lists: [
          {name: '公寓', id: 0},
          {name: '普通住宅', id: 1},
          {name: '特色房源', id: 2},
          {name: '精品酒店', id: 3},
        ],
      }
    },
    methods: {
      handleChange(index) {
        this.showList = false;
        this.data.type = this.lists[index].name;
        this.check = index;
      },
      handleCheckType() {
        this.showList = true
      }
    }
  }
</script>
