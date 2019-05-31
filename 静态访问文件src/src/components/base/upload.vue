<template>
  <div class="upload-box">
    <el-upload
            ref="upload"
            class="avatar-uploader"
            :action="action"
            list-type="picture-card"
            :file-list="fileList"
            :auto-upload="false"
            :show-file-list="true"
            :http-request="handleRequest"
            :on-change="handleChangeFile"
            :before-upload="beforeAvatarUpload"
            :on-preview="handlePictureCardPreview"
            :on-remove="handleRemove">
      <i class="el-icon-plus"></i>
    </el-upload>
    <el-dialog :visible.sync="dialogVisible">
      <img width="100%" :src="dialogImageUrl" alt="">
    </el-dialog>
  </div>
</template>

<script>
  export default {
    name: "uploadBox",
    data() {
      return {
        dialogImageUrl: '',
        dialogVisible: false,
        fileList: []
      }
    },
    props: {
      data: {
        type: Object,
        default: () => {}
      },
      action: {
        type: String,
        default: ''
      },
    },
    methods: {
      handleRequest(file) {
        this.$emit('append', file.file, file.name);
      },
      handleChangeFile(file, fileList) {
        this.$emit('change', fileList);
      },
      handlePictureCardPreview(file) {
        this.dialogImageUrl = file.url;
        this.dialogVisible = true;
      },
      handleRemove(file, fileList) {
        this.$emit('change', fileList);
      },
      beforeAvatarUpload(file) {
        /*const isJPG = file.type === 'image/jpeg' || file.type === 'image/png' || file.type === 'image/jpg';
        const isLt2M = file.size / 1024 / 1024 < 1;

        if (!isJPG) {
          this.$msg({
            type: 'error',
            message: '上传图片只能是 JPG 格式!'
          });
        }
        if (!isLt2M) {
          this.$msg({
            type: 'error',
            message: '上传图片大小不能超过 1MB!'
          });
        }
        return isJPG && isLt2M;*/
      },
    }
  }
</script>

<style scoped>

</style>
