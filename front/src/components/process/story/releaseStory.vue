<template>
  <div class="releaseStory">
    <h1>发布有趣的故事</h1>
    <div class="img-box-release">
      <p>故事中的图片</p>
      <upload ref="upload"
              :data="releaseData"
              :action="'/hotel/upload/house'"
              @success="handleSuccess"
              @error="handleError"
              @change="handleFileListChange"></upload>
    </div>
    <div class="titleInput new-box">
      <p>故事标题</p>
      <div class="box">
        <ve-plain-input ref="name" :target="['modify', 'blur']" placeholder="请输入美食名字" type="reg" inspect="^.+$" message="请输入故事的标题" v-model="releaseData.name" class="input" :errorOptions="{position: 'absolute'}"></ve-plain-input>
      </div>
    </div>
    <div class="titleInput new-box">
      <p>故事内容</p>
      <textarea class="textarea" v-model="releaseData.content" name="" id="" cols="30" rows="10" placeholder="分享让您印象深刻的旅行故事，比如有趣的瞬间，新奇的发现。"></textarea>
    </div>
    <div class="control-next">
      <ve-button class="primary" @click="handleRelease">发布</ve-button>
    </div>
  </div>
</template>

<script>
  import upload from '../../base/upload'
  export default {
    name: "releaseStory",
    components: {
      upload,
    },
    data() {
      return {
        releaseData: {
          content: '',
          fileList: []
        }
      }
    },
    methods: {
      handleRelease() {
        this.$refs.name.mergeMesh('blur');
        if (this.$refs.name.error || this.releaseData.content === '' || this.fileList.length === 0) {
          this.$msg({
            type: 'error',
            message: '请填写相关信息后发布'
          })
        }
      },
      handleSuccess() {
        this.$msg({
          type: 'success',
          message: '故事发布成功，可以在房源发布的过程中选择您发布的美食了'
        })
      },
      handleError(err) {},
      handleFileListChange(fileList) {
        this.fileList = fileList
      },
    },
  }
</script>

<style scoped>

</style>
