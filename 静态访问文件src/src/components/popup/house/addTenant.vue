<template>
  <div class="add-tenant">
    <span class="save" @touchend="handleSave">保存</span>
    <h1>添加房客信息</h1>
    <div class="simulation-input" @click="handleCheckType">
      <i :class="{'active-input': data.type}">选择身份证件类型</i>
      <p v-if="data.type">{{ data.type }}</p>
    </div>
    <div class="box">
      <p :class="{'active-input': inputError}">{{ data.type }}</p>
      <ve-plain-input ref="price" :target="['modify', 'blur']" @status="v => inputError = v" type="reg" inspect="^\d+$" :message="'请输入正确的' + data.type + '号码'" v-model="data.car" class="input" :errorOptions="{position: 'absolute'}"></ve-plain-input>
    </div>
    <div class="box">
      <p :class="{'active-input': nameError}">中文姓名</p>
      <ve-plain-input ref="price" :target="['modify', 'blur']" @status="v => nameError = v" type="reg" inspect="^.+$" message="请输入中文姓名" v-model="data.name" class="input" :errorOptions="{position: 'absolute'}"></ve-plain-input>
    </div>
    <list :data="lists" v-if="showList" :abs="false" @change="handleChange"></list>
  </div>
</template>

<script>
  import list from '../../base/list'
  export default {
    name: "addTenant",
    components: {
      list
    },
    data() {
      return {
        data: {type: '身份证'},
        lists: [{name: '身份证', id: 0},{name: '护照', id: 1}],
        showList: false,
        inputError: false,
        nameError: false,
      }
    },
    methods: {
      handleSave() {
        this.$router.back()
      },
      handleChange(obj) {
        this.showList = false;
        this.data.type = obj.name;
      },
      handleCheckType() {
        this.showList = true
      }
    }
  }
</script>

<style scoped lang="less">
.add-tenant {
  padding: 86px 36px 0;
  .save {
    position: absolute;
    top: 23px;
    right: 36px;
    font-size: 14px;
    color: #2E312F;
  }
  h1 {
    padding-bottom: 24px;
    font-size: 20px;
    color: #2E3130;
  }
  .box {
    margin-top: 36px;
    p {
      font-size: 14px;
      color: #5f5f5f;
    }
  }
  .simulation-input {
    padding-bottom: 12px;
    border-bottom: 1px solid #E4ECE8;
    i {
      font-style: normal;
      font-size: 14px;
      color: #5f5f5f;
    }
    p {
      font-weight: 600;
      margin-top: 12px;
    }
  }
  .active-input {
    color: #8ac7b7 !important;
    font-size: 12px !important;
  }
}
</style>
