<template>
  <div class="priceHouse">
    <h1>您的房源价格</h1>
    <div class="img-box">
      <el-upload
          ref="upload"
          class="avatar-uploader"
          action="/"
          :data="houseData"
          list-type="picture-card"
          :file-list="fileList"
          :auto-upload="false"
          :show-file-list="true"
          :on-change="handleChangeFile"
          :on-success="handleAvatarSuccess"
          :before-upload="beforeAvatarUpload"
          :on-preview="handlePictureCardPreview"
          :on-remove="handleRemove">
        <i class="el-icon-plus"></i>
      </el-upload>
      <el-dialog :visible.sync="dialogVisible">
        <img width="100%" :src="dialogImageUrl" alt="">
      </el-dialog>
    </div>
    <div class="titleInput new-box">
      <p>基础价格</p>
      <div class="box">
        <ve-plain-input ref="price" :target="['modify', 'blur']" placeholder="请输入入住房源需要支付的金额" type="reg" inspect="^\d+$" message="请输入正确的金额" v-model="data.price" class="input" :errorOptions="{position: 'absolute'}"></ve-plain-input>
      </div>
    </div>
    <div class="titleInput new-box">
      <p>价格规则</p>
      <div class="simulation-input" @click="handleCheckType">
        <i v-if="!dataView.type">付款方式</i>
        <p v-else>{{ dataView.type }}</p>
      </div>
    </div>
    <div class="control-next">
      <ve-button class="primary" @click="handleRelease">发布</ve-button>
    </div>
    <list :data="dataView.lists" v-if="dataView.showList" @change="handleChange"></list>
  </div>
</template>

<script>
  import list from '../../base/list'
  export default {
    name: 'priceHouse',
    components: {
      list
    },
    data() {
      return {
        houseData: {}, // 所有关于房源的信息
        data: {
          price: ''
        },
        dataView: {
          type: '',
          showList: false,
          lists: [{name: '支付宝', id: 0},{name: '微信', id: 1},{name: '银联', id: 2},]
        },
        dialogImageUrl: '',
        dialogVisible: false,
        fileList: []
      }
    },
    methods: {
      handleChangeFile(file, fileList) {
        this.fileList = fileList
      },
      handlePictureCardPreview(file) {
        this.dialogImageUrl = file.url;
        this.dialogVisible = true;
      },
      handleRemove(file, fileList) {
        this.fileList = fileList
      },
      handleAvatarSuccess() {

      },
      beforeAvatarUpload(file) {
        const isJPG = file.type === 'image/jpeg' || file.type === 'image/png' || file.type === 'image/jpg';
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
        return isJPG && isLt2M;
      },
      handleRelease() {
        this.$refs.price.mergeMesh('blur');
        if (this.fileList.length <= 0) {
          this.$msg({
            type: 'error',
            message: '请上传房源图片'
          })
        } else if (this.dataView.type === '') {
          this.$msg({
            type: 'error',
            message: '请选择付款方式'
          })
        } else if (Number(this.data.price) >= 1000) {
          this.$msg({
            type: 'error',
            message: '房源的价格不能超过1000'
          })
        } else if (!this.$refs.price.error) {
          //TODO 发布房源，组装数据给后台
          this.$refs.upload.submit();
        }
      },
      handleCheckType() {
        this.dataView.showList = true;
      },
      handleChange(obj) {
        if (!this.dataView.type.includes(obj.name)) {
          this.dataView.type = ((this.dataView.type !== '' ? this.dataView.type + ',' : '') + obj.name);
        }
        this.dataView.showList = false;
      }
    },
    beforeMount() {
      this.houseData = JSON.parse(window.localStorage.getItem('houseData'))
    }
  }
</script>
