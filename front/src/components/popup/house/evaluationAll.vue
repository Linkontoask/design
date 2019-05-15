<template>
  <div class="evaluation">
    <h1>全部{{ data.num }}条评价</h1>
    <p class="start">
      <img v-for="(item, index) in getStart(data.score)" :key="index" :src="require('../../../assets/' + (item ? 'start-fill' : 'start') + '.png')" alt="">
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
      <evaluationBase :evaluation="data.evaluation"></evaluationBase>
    </div>
  </div>
</template>

<script>
  import evaluationBase from '../../base/evaluationBase'
  export default {
    name: "evaluationAll",
    components: {
      evaluationBase
    },
    data() {
      return {
        data: {
          num: 12,
          score: 4,
          details: [{name: '整洁卫生', score: 3},{name: '描述相符', score: 5},{name: '安全程度', score: 5},{name: '交通位置', score: 4},{name: '性价比', score: 5}],
          evaluation: [{avatar: 'https://secure.gravatar.com/avatar/e4fdea5792f1b89f112307232e6056d1?s=800&d=identicon',
            name: 'Link',
            time: '2019年5月20日',
            content: '多么痛的领悟',
            imgs: ['https://secure.gravatar.com/avatar/e4fdea5792f1b89f112307232e6056d1?s=800&d=identicon', 'https://secure.gravatar.com/avatar/aed31b37c4d05315f295aa4e28d30039?s=800&d=identicon']}]
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
      }
    }
  }
</script>

<style scoped lang="less">
.evaluation {
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
