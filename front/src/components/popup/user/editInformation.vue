<template>
  <div class="edit-information">
    <div class="save" @touchend="handleSave">保存</div>
    <img v-if="user.avatar" :src="require('../../../assets/'+user.avatar)" alt="服务器错误">
    <div class="titleInput new-box">
      <p>名字</p>
      <ve-plain-input ref="user_name" :readonly="true" :target="['modify', 'blur']" type="reg" inspect="^.+$" message="取一个好听的名字吧" v-model="user.user_name" class="input" :errorOptions="{position: 'absolute'}"></ve-plain-input>
    </div>
    <div class="titleInput new-box">
      <p>个性签名</p>
      <ve-plain-input ref="show_name" @focus="getInputFocusScrollY" @blur="setWindowScrollY" :target="['modify', 'blur']" type="reg" inspect="^.+$" message="描述您的心情或心灵感触" v-model="user.signature" class="input" :errorOptions="{position: 'absolute'}"></ve-plain-input>
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
      async handleSave() {
        if (this.user.signature === '') {
          this.$refs.show_name.error = true;
          const node = this.$refs.show_name.$el.children[1];
          node.classList.add('animated', 'bounce', 'faster');
          function handleAnimationEnd() {
            node.classList.remove('animated', 'bounce');
            node.removeEventListener('animationend', handleAnimationEnd)
          }

          node.addEventListener('animationend', handleAnimationEnd)
        }
        if (this.user.signature !== '') {
          const data = await axios.get.call(this, '/hotel/edit_user_info/', {
            signature: this.user.signature
          }) || {};
          if (data.r === 0 ) {
            this.$msg({type: 'success', message: '信息已更新哦，快去我的界面看看吧'})
            this.$parent.handleTap()
          }
          data.r === 1 && this.$msg({type: 'error', message: '操作失败，请刷新重试'})
        }
      },
      async getDate() {
        this.$refs.show_name.error = false;
        const data = await axios.get.call(this, '/hotel/user_info/', {});
        this.user = data.data;
        Storage.set('user_info_', this.user);
      }
    },
    mounted() {

    },
    activated() {
      this.getDate()
    },
    beforeMount() {
      // this.getDate()
    }
  }
</script>

<style scoped lang="less">
.edit-information {
  position: relative;
  padding: 108px 24px 0;
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
