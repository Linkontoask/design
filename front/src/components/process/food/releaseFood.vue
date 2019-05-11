<template>
  <div class="releaseFood">
    <h1>发布您觉得好吃的美食</h1>
    <div class="img-box-release">
      <p>美食照片</p>
      <upload ref="upload"
              :action="'/hotel/around_region/'"
              @append="append"
              @success="handleSuccess"
              @error="handleError"
              @change="handleFileListChange"></upload>
    </div>
    <div class="titleInput new-box">
      <p>美食名字</p>
      <div class="box">
        <ve-plain-input ref="name" :target="['modify', 'blur']" placeholder="请输入美食名字" type="reg" inspect="^.+$" message="请输入美食名字" v-model="releaseData.name" class="input" :errorOptions="{position: 'absolute'}"></ve-plain-input>
      </div>
    </div>
    <div class="titleInput new-box">
      <p>美食价格</p>
      <div class="box">
        <ve-plain-input ref="price" :target="['modify', 'blur']" placeholder="请输入美食价格" type="reg" inspect="^\d+$" message="请输入美食价格" v-model="releaseData.price" class="input" :errorOptions="{position: 'absolute'}"></ve-plain-input>
      </div>
    </div>
    <div class="titleInput new-box">
      <p>美食描述</p>
      <textarea class="textarea" v-model="releaseData.desc" name="" id="" cols="30" rows="10" placeholder="输入关于美食的描述"></textarea>
    </div>
    <div class="control-next">
      <ve-button class="primary" @click="handleReleaseFood">发布</ve-button>
    </div>
  </div>
</template>

<script>
  import upload from '../../base/upload'
  import axios from '../../../utils/axios'
  import cookie from '../../../utils/cookie'

  export default {
    name: "releaseFood",
    components: {
      upload,
    },
    data() {
      return {
        releaseData: {
          type: 1
        },
        formDate: new FormData()
      }
    },
    methods: {
      append(file) {
        this.formDate.append('files', file);
      },
      async handleReleaseFood() {
        this.$refs.name.mergeMesh('blur');
        this.$refs.price.mergeMesh('blur');
        if (this.$refs.name.error || this.$refs.price.error || this.releaseData.desc === '') {
          this.$msg({
            type: 'error',
            message: '请填写相关信息后发布'
          })
        } else {
          await this.setDate();
        }

      },
      async setDate() {
        this.$refs.upload.$refs.upload.submit();
        return await axios.post(this.action, Object.assign({
          'X-CSRFToken': cookie.get('csrftoken')
        }, ...this.releaseData, this.formDate))
      },
      handleSuccess() {
        this.$msg({
          type: 'success',
          message: '美食发布成功，可以在房源发布的过程中选择您发布的美食了'
        })
        this.$router.push({
          path: '/release'
        })
      },
      handleError(err) {},
      handleFileListChange(fileList) {},
    },
  }
</script>

<style scoped>

</style>
