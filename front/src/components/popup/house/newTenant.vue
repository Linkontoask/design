<template>
  <div class="new-tenant">
    <span class="save" @touchend="handleSave">保存</span>
    <h1>房客信息</h1>
    <div class="info">根据有关部门规定，所有前往国内的旅客都必须提供以下信息。</div>
    <ul>
      <Radio class="li" v-for="(item, index) in tenant" :i="index" :key="index" :checked="checkedList[index]" @click="value => handleCheck(index, value)" type="checkbox">
        <h5>{{ item.name }}</h5>
        <p>身份证：{{ item.id }}</p>
      </Radio>
    </ul>
    <div class="add">
      <h3 @touchend="handleAdd">
        <span>添加房客信息</span>
        <div class="add-icon">
          <p></p>
          <p></p>
        </div>
      </h3>
    </div>
  </div>
</template>

<script>
  import Radio from '../../base/radio'
  import Storage from '../../../utils/localStorage'
  export default {
    name: "newTenant",
    components: {
      Radio
    },
    data() {
      return {
        checkedList: [true, false],
        result: [true,false],
        tenant: [{name: 'Link', id: '430723xxxxxxxx0124'},{name: 'Join', id: '562413xxxxxxxx1224'}]
      }
    },
    methods: {
      handleAdd() {
        this.$router.push({
          name: 'addTenant'
        })
      },
      handleCheck(index, value) {
        this.$set(this.result, index, value);
      },
      handleSave() {
        if (this.result.includes(true)) {
          let ids = [];
          this.tenant.filter((i, index) => this.result[index]).forEach(item => {
            ids.push(item.id)
          });
          this.$parent.handleTap(null, {is_check: ids.join('|')});
        } else {
          this.$msg({
            type: 'error',
            message: '至少选择一个房客信息'
          })
        }

      }
    }
  }
</script>

<style scoped lang="less">
.new-tenant {
  padding: 28px 36px 0;
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
  .info {
    font-size: 14px;
  }
  ul {
    margin-top: 36px;
    padding-bottom: 24px;
    border-bottom: 1px solid #E4ECE8;
    .li {
      h5 {
        margin-bottom: 4px;
      }
      p {
        font-size: 14px;
      }
      & + .li {
        margin-top: 24px;
      }
    }
  }
  .add {
    margin-top: 24px;
    h3 {
      font-size: 16px;
      justify-content: space-between;
      display: flex;
    }
    .add-icon {
      width: 24px;
      height: 24px;
      border-radius: 50%;
      border: 1px solid #25A3A8;
      display: flex;
      align-items: center;
      justify-content: space-around;
      p {
        width: 16px;
        height: 2px;
        background-color: #25A3A8;
      }
      p:last-child {
        transform: rotate(90deg);
        margin-left: -24px;
      }
    }
  }
}
</style>
