<template>
  <div class="releaseFood">
    <h1>发布您觉得好吃的美食</h1>
    <div class="img-box">
      <p>美食照片</p>
      <upload ref="upload"
              :data="releaseData"
              :action="'/hotel/upload/house'"
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
      <p>房源特色</p>
      <textarea class="textarea" v-model="releaseData.desc" name="" id="" cols="30" rows="10" placeholder="输入关于美食的描述"></textarea>
    </div>
    <div class="control-next">
      <ve-button class="primary" @click="handleRelease">发布</ve-button>
    </div>
  </div>
</template>

<script>
  import upload from '../../base/upload'
  export default {
    name: "releaseFood",
    components: {
      upload,
    },
    data() {
      return {
        releaseData: {}
      }
    },
    methods: {
      handleRelease() {
        this.$refs.name.mergeMesh('blur');
        this.$refs.price.mergeMesh('blur');
        if (this.$refs.name.error || this.$refs.price.error || this.releaseData.desc) {
          this.$msg({
            type: 'error',
            message: '请填写相关信息后发布'
          })
        }
      },
      handleSuccess() {
        this.$msg({
          type: 'success',
          message: '美食发布成功，可以在房源发布的过程中选择您发布的美食了'
        })
      },
      handleError(err) {},
      handleFileListChange(fileList) {},
    },
  }
</script>

<style scoped>

</style>