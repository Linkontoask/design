<template>
  <div class="edit-information">
    <div class="save" @touchend="handleSave">保存</div>
    <img :src="require('../../../assets/'+user.avatar)" alt="服务器错误">
    <div class="titleInput new-box">
      <p>名字</p>
      <ve-plain-input ref="user_name" :target="['modify', 'blur']" type="reg" inspect="^.+$" message="取一个好听的名字吧" v-model="user.user_name" class="input" :errorOptions="{position: 'absolute'}"></ve-plain-input>
    </div>
    <div class="titleInput new-box">
      <p>个性签名</p>
      <ve-plain-input ref="show_name" :target="['modify', 'blur']" type="reg" inspect="^.+$" message="描述您的心情或心灵感触" v-model="user.show_name" class="input" :errorOptions="{position: 'absolute'}"></ve-plain-input>
    </div>
  </div>
</template>

<script>
  import axios from '../../../utils/axios'
  import Storage from '../../../utils/localStorage'
  export default {
    name: 'editInformation',
    data() {
      return {
        user: {}
      }
    },
    methods: {
      handleSave() {
        if (!this.$refs.show_name.error && !this.$refs.user_name.error) {
          this.$parent.handleTap()
        }

      },
      getDate() {
        this.user = Storage.get('user_info_')
        console.log(this.user)
      }
    },
    mounted() {

    },
    activated() {
      this.getDate()
    },
    beforeMount() {
      this.getDate()
    }
  }
</script>

<style scoped lang="less">
.edit-information {
  position: relative;
  padding: 0 36px;
  .save {
    position: fixed;
    top: 23px;
    right: 36px;
    font-size: 14px;
    color: #2E312F;
  }
  img {
    max-height: 160px;
    max-width: 100%;
    display: block;
    margin: 0 auto;
  }
  .new-box {
    margin-top: 36px;
  }
}
</style>
