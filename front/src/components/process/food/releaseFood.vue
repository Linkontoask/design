<template>
  <div class="releaseFood">
    <h1>发布您觉得好吃的美食</h1>
    <div class="img-box-release">
      <p ref="img">美食照片</p>
      <upload ref="upload"
              @append="append"
              @change="handleFileListChange"></upload>
    </div>
    <div class="titleInput new-box">
      <p>美食名字</p>
      <div class="box">
        <ve-plain-input ref="name" @focus="getInputFocusScrollY" @blur="setWindowScrollY" :target="['modify', 'blur']" placeholder="请输入美食名字" type="reg" inspect="^.+$" message="请输入美食名字" v-model="releaseData.name" class="input" :errorOptions="{position: 'absolute'}"></ve-plain-input>
      </div>
    </div>
    <div class="titleInput new-box">
      <p>美食价格</p>
      <div class="box">
        <ve-plain-input ref="price" @focus="getInputFocusScrollY" @blur="setWindowScrollY" :target="['modify', 'blur']" placeholder="请输入美食价格" type="reg" inspect="^\d+$" message="请输入美食价格" v-model.number="releaseData.price" class="input" :errorOptions="{position: 'absolute'}"></ve-plain-input>
      </div>
    </div>
    <div class="titleInput new-box">
      <p>美食描述</p>
      <textarea class="textarea" v-model="releaseData.desc" name="" id="" cols="30" rows="10" placeholder="输入关于美食的描述"></textarea>
    </div>
    <div class="control-next">
      <ve-button class="primary" @click="handleReleaseFood">发布</ve-button>
    </div>
    <loading :vis="show"></loading>
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
        fileList: [],
        formDate: new FormData(),
        show: false,
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
      async handleReleaseFood() {
        if (this.fileList.length === 0) {
          this.animation('img', false, 'shake');
        } else if (!this.releaseData.name) {
          this.$refs.name.error = true;
          this.animation('name', true, 'bounce');
        } else if (!this.releaseData.price) {
          this.$refs.price.error = true;
          this.animation('price', true, 'bounce');
        } else {
          this.$refs.upload.$refs.upload.submit();
          for (let [key,value] of Object.entries(this.releaseData)) {
            this.formDate.append(key, value)
          }
          this.show = true;
          const data = await axios.postFile.call(this, '/hotel/around_region/', this.formDate);
          this.show = false;
          if (data.r === 0) {
            this.$msg({
              type: 'success',
              message: '美食发布成功'
            });
            this.$router.push({
              path: '/release'
            })
          }
        }

      },
      async setDate() {
        this.$refs.upload.$refs.upload.submit();

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
      handleFileListChange(fileList) {
        this.fileList = fileList;
      },
    },
  }
</script>

<style scoped>

</style>
