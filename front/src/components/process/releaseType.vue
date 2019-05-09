<template>
  <div class="release-type">
    <h1>发布类型</h1>
    <Radio class="release-radio" v-for="(item, index) in radio" :i="index" :key="item.id" @click="handleCheck(index)">
      <h4>{{ item.name }}</h4>
      <p class="margin4">{{ item.desc }}</p>
    </Radio>
    <div class="control-next">
      <ve-button class="primary" @click="handleNext">下一步</ve-button>
    </div>
  </div>
</template>

<script>
  import Radio from 'components/base/radio'
  export default {
    name: 'releaseType',
    components: {
      Radio
    },
    data() {
      return {
        radio: [{
          name: '房源',
          desc: '发布房源的相关说明',
          id: 0,
        },{
          name: '美食',
          desc: '发布美食的相关说明',
          id: 1,
        },{
          name: '故事',
          desc: '发布故事的相关说明',
          id: 2,
        },],
        index: -1
      }
    },
    methods: {
      handleCheck(index) {
        this.index = index;
      },
      handleNext() {
        if (this.index === -1) {
          return this.$msg({
            type: 'warning',
            message: '请至少选择一项进行发布'
          })
        }
        if (this.index === 0) {
          this.$router.push({
            path: '/pop/newHouse',
            query: {
              direction: 'right',
            }
          })
        }
      }
    },
    mounted() {
      // window.localStorage.setItem('current_hotel', this.$route.path);
    }
  }
</script>
