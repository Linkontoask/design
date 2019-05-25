<template xmlns:v-hammer="http://www.w3.org/1999/xhtml">
  <div class="login">
    <img src="../assets/logo.png" alt="LOGO" class="logo">
    <div class="login-box">
      <h4 @click="$refs.user.$el.children[0].focus()">用户名</h4>
      <ve-plain-input ref="user" @focus="getInputFocusScrollY" @blur="setWindowScrollY" v-model.trim="data.username" message="请输入正确的用户名，只能是数字或者字母组合" type="reg" inspect="^[a-zA-Z]|[0-9]{2,6}$" class="input" :errorOptions="{position: 'absolute'}"></ve-plain-input>
      <h4 style="padding-top: 6px" @click="$refs.password.$el.children[0].focus()">密码</h4>
      <form @submit.prevent="formSubmit" action="javascript:return true">
        <ve-plain-input name="done" ref="password" @focus="getInputFocusScrollY" @blur="setWindowScrollY" @keyup.enter.native="login" v-model.trim="data.password" message="请输入正确的密码" :options="{min: 6, max: 12}" class="input password" :errorOptions="{position: 'absolute'}" typeInput="password"></ve-plain-input>
      </form>
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
        data: {},
      }
    },
    methods: {
      formSubmit() {
        return false;
      },
      async login() {
        this.$refs.password.$el.children[0].blur();
        this.$refs.user.mergeMesh('blur');
        this.$refs.password.mergeMesh('blur');
        if (!this.$refs.user.error && !this.$refs.password.error) {
          const data = await axios.get.call(this, '/hotel/login_in', this.data);
          if (!data.r) {
            this.$msg({type: 'success', message: data.e, duration: 2000,});
            cookie.set('hotel_', this.data.username);
            const beforeUrl = cookie.get('before_url_');
            if (beforeUrl) {
              this.$router.push({
                path: beforeUrl
              })
            } else {
              this.$router.push('homeStay')
            }
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
    },
    activated() {
      this.data = {};
      this.$refs.password.error = false;
      this.$refs.user.error = false;
    }
  }
</script>

<style lang="less" scoped>
  @import "../style/global";
  @keyframes bounceInLeft {
    0% {left: 100%}
    100% {left: 0}
  }
  .login {
    position: relative;
    padding-bottom: 36px;
    animation: bounceInLeft .3s ease-out forwards;
    .logo {
      display: block;
      margin: calc(6.625rem - @topIndicator) auto 0;
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
          display: inline-block;
          height: 36px;
          line-height: 56px;
        }
      }
    }
  }
</style>
