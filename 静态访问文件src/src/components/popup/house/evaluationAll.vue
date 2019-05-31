<template>
  <div class="evaluation">
    <h1>全部{{ data.appraise_num }}条评价</h1>
    <p class="start">
      <img v-for="(item, index) in getStart(data.total_appraise.total_score)" :key="index" :src="require('../../../assets/' + (item ? 'start-fill' : 'start') + '.png')" alt="">
    </p>
    <div class="details">
      <ul>
        <li v-for="(item, index) in data.details" :key="index">
          <p>{{ item.name }}</p>
          <p>
            <img v-for="(img, i) in getStart(item.score)" :key="i" :src="require('../../../assets/' + (img ? 'start-fill' : 'start') + '.png')" alt="">
          </p>
        </li>
      </ul>
    </div>
    <div class="box">
      <evaluationBase :evaluation="data.user_list"></evaluationBase>
    </div>
  </div>
</template>

<script>
  import evaluationBase from '../../base/evaluationBase'
  import axios from "../../../utils/axios";
  export default {
    name: "evaluationAll",
    components: {
      evaluationBase
    },
    data() {
      return {
        data: {
          total_appraise: {},
          user_list: [],
          details: [{name: '整洁卫生', score: 3},{name: '描述相符', score: 5},{name: '安全程度', score: 5},{name: '交通位置', score: 4},{name: '性价比', score: 5}],
        }
      }
    },
    computed: {
      start() {
        const d = Array.from({length: 5 - this.data.score}).fill(false);
        return Array.from({length: this.data.score}).fill(true).concat(d)
      }
    },
    methods: {
      getStart(i) {
        const d = Array.from({length: 5 - i}).fill(false);
        return Array.from({length: i}).fill(true).concat(d)
      },
      async getData() {
        let data = await axios.get.call(this, '/hotel/get_appraise/', this.$route.query);
        data.data.user_list = data.data.user_list.reverse();
        let details = data.data.total_appraise.score_info.split(',');
        details.forEach((item, index) => {
          details[index] = {name: this.data.details[index].name, score: Number(item)}
        });
        this.data = data.data;
        this.data.details = details;
      }
    },
    async activated() {
      this.getData()
    },
    async beforeMount() {

    }
  }
</script>

<style scoped lang="less">
.evaluation {
  margin-top: 54px;
  h1 {
    font-size: 20px;
    color: #2E3130;
    padding: 36px 36px 16px;
  }
  .start {
    padding: 0 36px 40px;
    img {
      width: 18px;
    }
    img + img {
      margin-left: 4px;
    }
  }
  .details {
    padding: 0 36px;
    ul {
      padding-bottom: 20px;
      border-bottom: 1px solid #E4ECE8;
      li {
        display: flex;
        justify-content: space-between;
        color: #2E3130;
        & + li {
          margin-top: 16px;
        }
      }
    }
    img {
      width: 16px;
      & + img {
        margin-left: 4px;
      }
    }
  }
  .box {
    padding: 38px 36px 24px;
    h3 {
      font-weight: 500;
    }
  }
}
</style>
