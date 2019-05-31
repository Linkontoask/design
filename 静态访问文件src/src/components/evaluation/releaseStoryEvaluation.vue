<template>
  <div class="write-story-evaluation">
    <div class="save" @click="handleSave">保存</div>
    <textarea v-model="value" name="" id="" cols="30" rows="10" placeholder="写评价..."></textarea>
  </div>
</template>

<script>
  import axios from '../../utils/axios'
  export default {
    name: "storyWriteEvaluation",
    data() {
      return {
        value: ''
      }
    },
    methods: {
      async handleSave() {
        if (this.value === '') {
          return this.$msg({type: 'error', message: '先填写评价内容后再保存哦'})
        }
        let query = this.$route.query;
        let formData = new FormData();
        formData.append('content', this.value);
        for (let [key,value] of Object.entries(query)) {
          formData.append(key, value)
        }
        const data = await axios.postFile.call(this, '/hotel/user_appraise/', formData)
        if (data.r === 0) {
          //this.$msg({type: 'success', message: '评价成功'});
          this.$parent.handleTap()
        } else {
          //this.$msg({type: 'error', message: data.e});
        }
      }
    }
  }
</script>

<style scoped lang="less">
  .write-story-evaluation {
    height: 100vh;
    .save {
      float: right;
      margin-right: 24px;
      padding-top: 24px;
      font-size: 14px;
      color: #2E3130;
    }
    textarea {
      width: calc(100% - 48px);
      height: calc(100% - 98px);
      margin-top: 32px;
      padding: 12px 24px;
      border: none;
      outline: none;
      border-top: 1px solid #E3E9E6;
      font-size: 16px;
      &::placeholder {
        color: #5F6564;
      }
    }
  }
</style>