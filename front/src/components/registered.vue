<template>
  <div class="login">
    <img src="../assets/logo.png" alt="LOGO" class="logo">
    <div class="login-box">
      <h4>用户名</h4>
      <ve-plain-input ref="user" v-model="data.user" message="请输入正确的用户名" :options="{min: 2, max: 6}" class="input" :errorOptions="{position: 'absolute'}"></ve-plain-input>
      <h4 style="padding-top: 6px">密码</h4>
      <ve-plain-input ref="password" v-model="data.password" message="请输入正确的密码" :options="{min: 6, max: 12}" class="input password" :errorOptions="{position: 'absolute'}" typeInput="password"></ve-plain-input>
      <h4 style="padding-top: 6px">确认密码</h4>
      <ve-plain-input ref="checkpass" v-model="data.checkPassword" message="两次密码输入不一致" class="input password" :errorOptions="{position: 'absolute'}" typeInput="password" @blur="handleBlur"></ve-plain-input>
      <ve-button class="primary" @click="registered">注册</ve-button>
    </div>
  </div>
</template>

<script>
  import fetch from 'utils/fetch'
  export default {
    name: 'registered',
    components: {
    },
    data() {
      return {
        data: {
          user: '',
          password: '',
          checkPassword: ''
        }
      }
    },
    methods: {
      async registered() {
        this.$refs.user.mergeMesh('blur');
        this.$refs.password.mergeMesh('blur');
        this.handleBlur();
        if (!this.$refs.user.error && !this.$refs.password.error) {
          const data = await fetch('/hotel/login', this.data);
        }
      },
      async handleBlur(ev) {
        this.$refs.checkpass.error = this.data.checkPassword !== this.data.password;
        if (!this.data.checkPassword) {
          this.$refs.checkpass.error = true;
        }
      }
    }
  }
</script>

<style lang="less" scoped>
  .login {
    .logo {
      display: block;
      margin: 6.625rem auto 0;
      width: 8.75rem;
    }
    .login-box {
      padding: 0 2.25rem;
      margin: 7.875rem auto 0;
      h4 {
        font-size: 1rem;
        font-weight: 400;
      }
      .input {
        margin-top: 14px;
      }
    }
  }
</style>
