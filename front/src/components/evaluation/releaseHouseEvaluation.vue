<template>
  <div class="release-evaluation">
    <div class="details">
      <ul>
        <li v-for="(item, index) in details" :key="index">
          <p>{{ item.name }}</p>
          <p>
            <img v-for="(img, i) in getStart(item.score)" :key="i" @touchend="handleScore(index, i)" :src="require('../../assets/' + (img ? 'start-fill' : 'start') + '.png')" alt="">
          </p>
        </li>
      </ul>
    </div>
    <textarea v-model="value" name="" id="" cols="30" rows="10" placeholder="留下你的笔记让其他人参考"></textarea>
    <upload class="upload" ref="upload"
            @append="append"
            @change="handleFileListChange"></upload>
    <ve-button class="primary" @click.native="handleRelease">发布</ve-button>
  </div>
</template>

<script>
  import upload from '../base/upload'
  import axios from '../../utils/axios'
  export default {
    name: "releaseEvaluation",
    components: {
      upload
    },
    data() {
      return {
        details: [{name: '整洁卫生', score: 0},{name: '描述相符', score: 0},{name: '安全程度', score: 0},{name: '交通位置', score: 0},{name: '性价比', score: 0}],
        value: '',
        formDate: new FormData()
      }
    },
    methods: {
      handleScore(index, i) {
        this.details[index].score = i + 1;
      },
      async handleRelease() {
        this.$refs.upload.$refs.upload.submit();
        let score = [];
        this.details.forEach(item => score.push(item.score));
        let avg_score = score.reduce((a,b) => a + b) / 5;
        this.formDate.append('avg_score', String(Math.floor(avg_score)));
        this.formDate.append('score_info', score.join(','));
        this.formDate.append('obj_class', this.$route.query.obj_class);
        this.formDate.append('belong_id', this.$route.query.uuid);
        this.formDate.append('order_id', this.$route.query.order_id);
        this.formDate.append('content', this.value);
        const data = await axios.postFile.call(this, '/hotel/user_appraise/', this.formDate);
        if (data.r === 0) {
          this.$msg({
            type: 'success',
            message: data.e
          });
          this.$parent.handleTap()
        } else {
          this.$msg({
            type: 'error',
            message: data.e
          });
        }
      },
      append(file, name) {
        this.formDate.append('files', file, name);
      },
      handleFileListChange() {},
      getStart(i) {
        const d = Array.from({length: 5 - i}).fill(false);
        return Array.from({length: i}).fill(true).concat(d)
      }
    }
  }
</script>

<style scoped lang="less">
.release-evaluation {
  padding: 0 36px;
  .upload {
    margin-top: 24px;
  }
  .primary {
    width: 100%;
    margin-top: 48px;
    margin-bottom: 36px;
  }
  textarea {
    font-family: PingFangSC-Regular, sans-serif;
    width: calc(100% - 24px);
    border-color: #dcdfe6;
    padding: 12px;
    border-radius: 8px;
    outline-color: #25A3A8;
    -moz-outline-radius: 8px;
    margin-top: 16px;
    font-size: 14px;
    box-shadow: none;
  }
  .details {
    margin-top: 86px;
    ul {
      padding-bottom: 20px;
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
      width: 24px;
      & + img {
        margin-left: 4px;
      }
    }
  }
}
</style>
