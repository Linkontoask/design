<template>
  <div class="delete-collection" v-if="vis">
    <div class="mask"></div>
    <transition appear name="bottom">
      <ul>
        <li @click="handleDelete">删除收藏</li>
        <li @click="handleCancel">取消</li>
      </ul>
    </transition>
  </div>
</template>

<script>
  import axios from '../../utils/axios'
  export default {
    name: "deleteCollection",
    props: {
      vis: {
        type: Boolean,
        default: false
      },
      belong_class: {
        type: String,
        default: ''
      },
      belong_id: {
        type: Array,
        default: () => []
      }
    },
    methods: {
      handleCancel() {
        this.$emit('show', false)
      },
      async handleDelete() {
        this.belong_id.forEach(async item => {
          await axios.get.call(this, '/hotel/del_collect/', {
            belong_class: this.belong_class,
            belong_id: item,
          })
        })
        this.$msg({type: 'success', message: '操作成功'});
        this.$emit('status');
      }
    }
  }
</script>

<style scoped lang="less">
  .bottom-enter-active, .bottom-leave-active {
    transition: opacity .3s, margin .3s;
  }
  .bottom-enter-active {
    opacity: 0;
    margin-bottom: -177px;
  }
  .bottom-leave-active {
    margin-bottom: 0;
    opacity: 1;
  }
  .bottom-leave-to {
    margin-bottom: -177px;
    opacity: 0;
  }
  .bottom-enter-to {
    margin-bottom: 0;
    opacity: 1;
  }
.delete-collection {
  position: fixed;
  width: 100vw;
  height: 100vh;
  left: 0;
  top: 0;
  z-index: 9;
  .mask {
    position: absolute;
    left: 0;
    top: 0;
    width: 100%;
    height: 100%;
    z-index: 2;
    background-color: #333333ab;
    color: white;
    display: flex;
    align-items: center;
    justify-content: space-around;
  }
  ul {
    position: fixed;
    left: 0;
    bottom: 12px;
    width: 100%;
    z-index: 10;
    li {
      margin: 0 auto;
      width: 94%;
      padding: 12px 0;
      text-align: center;
      background-color: white;
      border-radius: 12px;
      font-size: 18px;
      font-weight: bold;
      & + li {
        margin-top: 10px;
      }
    }
    li:first-child {
      color: #EB0C0C;
    }
    li:last-child {
      color: #1D8FF2;
    }
  }
}
</style>