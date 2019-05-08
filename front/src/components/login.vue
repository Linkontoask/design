<template xmlns:v-hammer="http://www.w3.org/1999/xhtml">
  <div class="login">
    <img src="../assets/logo.png" alt="LOGO" class="logo">
    <div class="login-box">
      <h4>用户名</h4>
      <ve-plain-input ref="user" v-model="data.username" message="请输入正确的用户名" :options="{min: 2, max: 6}" class="input" :errorOptions="{position: 'absolute'}"></ve-plain-input>
      <h4 style="padding-top: 6px">密码</h4>
      <ve-plain-input ref="password" v-model="data.password" message="请输入正确的密码" :options="{min: 6, max: 12}" class="input password" :errorOptions="{position: 'absolute'}" typeInput="password"></ve-plain-input>
      <div class="login-control">
        <div>
          <span v-hammer:tap="signup">注册</span>
          <span v-hammer:tap="forget">忘记密码</span>
        </div>
        <ve-button class="primary" @click="login">登录</ve-button>
      </div>
    </div>
  </div>
</template>

<script>
  import axios from 'utils/axios'
  import cookie from 'utils/cookie'
  export default {
    name: 'login',
    components: {
    },
    data() {
      return {
        data: {
          username: ''
        }
      }
    },
    methods: {
      async login() {
        this.$refs.user.mergeMesh('blur');
        this.$refs.password.mergeMesh('blur');
        if (!this.$refs.user.error && !this.$refs.password.error) {
          const data = await axios.get('/hotel/login_in', this.data);
          if (!data.r) {
            this.$msg({type: 'success', message: data.e, duration: 2000,});
            cookie.set('hotel_', this.data.username);
            this.$router.push('homeStay')
          } else {
            this.$msg({type: 'error', message: data.e, duration: 4000,});
          }
        }
      },
      signup() {
        this.$router.push('signup');
      },
      forget() {
        this.$msg({
          type: 'info',
          message :'暂时不提供修改密码，还未设计原型',
          showClose: false,
          duration: 2000,
        });
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
      .login-control {
        margin-top: 30px;
        display: flex;
        align-items: flex-end;
        justify-content: space-between;
        span {
          font-size: 14px;
          color: #25A3A8;
          margin-right: 20px;
        }
      }
    }
  }
</style>
