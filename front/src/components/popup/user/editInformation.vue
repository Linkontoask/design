<template>
  <div class="edit-information">
    <img :src="user.avatar" alt="服务器错误">
    <div class="titleInput new-box">
      <p>名字</p>
      <ve-plain-input ref="name" :target="['modify', 'blur']" type="reg" inspect="^.+$" message="取一个好听的名字吧" v-model="user.name" class="input" :errorOptions="{position: 'absolute'}"></ve-plain-input>
    </div>
    <div class="titleInput new-box">
      <p>个性签名</p>
      <ve-plain-input ref="name" :target="['modify', 'blur']" type="reg" inspect="^.+$" message="描述您的心情或心灵感触" v-model="user.desc" class="input" :errorOptions="{position: 'absolute'}"></ve-plain-input>
    </div>
  </div>
</template>

<script>
  import axios from '../../../utils/axios'
  export default {
    name: 'editInformation',
    data() {
      return {
        user: {}
      }
    },
    methods: {

    },
    mounted() {

    },
    beforeMount() {

    }
  }
</script>

<style scoped lang="less">
.edit-information {
  position: relative;
  padding: 0 36px;
  img {
    max-height: 230px;
    max-width: 100%;
  }
  .new-box {
    margin-top: 36px;
  }
}
</style>
