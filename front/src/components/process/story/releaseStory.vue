<template>
  <div class="releaseStory">
    <h1>发布有趣的故事</h1>
    <div class="img-box-release">
      <p ref="img">故事中的图片</p>
      <upload ref="upload"
              @append="append"
              @change="handleFileListChange"></upload>
    </div>
    <div class="titleInput new-box">
      <p>故事标题</p>
      <div class="box">
        <ve-plain-input ref="name" :target="['modify', 'blur']" placeholder="请输入故事标题" type="reg" inspect="^.+$" message="请输入故事的标题" v-model="releaseData.name" class="input" :errorOptions="{position: 'absolute'}"></ve-plain-input>
      </div>
    </div>
    <div class="titleInput new-box">
      <p ref="content">故事内容</p>
      <textarea class="textarea" v-model="releaseData.content" name="" id="" cols="30" rows="10" placeholder="分享让您印象深刻的旅行故事，比如有趣的瞬间，新奇的发现。"></textarea>
    </div>
    <div class="control-next">
      <ve-button class="primary" @click="handleRelease">发布</ve-button>
    </div>
    <loading :vis="show"></loading>
  </div>
</template>

<script>
  import upload from '../../base/upload'
  import axios from '../../../utils/axios'
  export default {
    name: "releaseStory",
    components: {
      upload,
    },
    data() {
      return {
        releaseData: {
          content: '',
          name: '',
        },
        show: false,
        fileList: [],
        formDate: new FormData()
      }
    },
    methods: {
      append(file, name) {
        this.formDate.append('files', file, name);
      },
      animation(name, isVueComponent, animat) {
        let node = this.$refs[name];
        if (isVueComponent) {
          node = this.$refs[name].$el.children[1]
        }
        node.classList.add('animated', animat, 'faster', 'red');
        function handleAnimationEnd() {
          node.classList.remove('animated', animat, 'red');
          node.removeEventListener('animationend', handleAnimationEnd)
        }
        node.addEventListener('animationend', handleAnimationEnd)
      },
      async handleRelease() {
        if (this.fileList.length === 0) {
          this.animation('img', false, 'shake');
        } else if (!this.releaseData.name) {
          this.$refs.name.error = true;
          this.animation('name', true, 'bounce');
        } else if (!this.releaseData.content) {
          this.animation('content', false, 'shake');
        } else {
          this.$refs.upload.$refs.upload.submit();
          for (let [key,value] of Object.entries(this.releaseData)) {
            this.formDate.append(key, value)
          }
          this.show = true;
          const data = await axios.postFile.call(this, '/hotel/story_board/', this.formDate);
          this.show = false;
          if (data && data.r === 0) {
            this.$msg({
              type: 'success',
              message: '故事发布成功'
            });
            this.$router.push({
              path: '/release'
            })
          }
        }
      },
      handleSuccess() {
        this.$msg({
          type: 'success',
          message: '故事发布成功'
        })
      },
      handleError(err) {},
      handleFileListChange(fileList) {
        this.fileList = fileList
      },
    },
    mounted() {
    }
  }
</script>

<style scoped>

</style>
