<template xmlns:v-hammer="http://www.w3.org/1999/xhtml">
  <li>
    <div class="msgBase" v-hammer:tap="handleTap" v-hammer:swipe.left.right="handleSwiper" :class="{hide: is_hide}">
      <div :class="{activeLeft: left}" class="list-box">
        <img class="img-box" :src="require('../../assets/' + data.src)" alt="">
        <notification v-if="data.unread !== 0">{{ data.unread }}</notification>
        <div class="msgBase-box">
          <h5>{{ data.name }}</h5>
          <p>{{ data.lastMsg }}</p>
        </div>
        <div class="delete" v-hammer:tap="handleDelete">删除</div>
      </div>
    </div>
  </li>
</template>

<script>
  import notification from './notification'
  export default {
    name: "msgBase",
    components: {
      notification
    },
    props: {
      data: {
        type: Object,
        default: () => {{}}
      },
      left: {
        type: Boolean
      },
    },
    data() {
      return {
        is_left: false,
        is_hide: false
      }
    },
    methods: {
      handleTap(ev) {
        if (ev.target.className === 'delete' || this.is_left) {
          if (this.is_left) {
            this.is_left = false;
            this.$emit('left', this.is_left);
          }
          return false;
        }
        this.is_left = false;
        this.$emit('tap', this.data)
      },
      handleSwiper(ev) {
        this.is_left = ev.type === 'swipeleft';
        this.$emit('left', this.is_left)
      },
      handleDelete() {
        this.is_hide = true;
        this.$emit('delete', this.data.uuid)
      }
    },
    mounted() {
    }
  }
</script>

<style scoped lang="less">
@delete: 100px;
.activeLeft {
  transform: translateX(-@delete);
}
div.hide {
  height: 0;
  padding: 0;
}
.msgBase {
  width: 100%;
  height: 80px;
  overflow: hidden;
  transition: height .3s, padding .3s;
  display: flex;
  align-items: center;
  > .list-box {
    position: relative;
    display: flex;
    align-items: stretch;
    width: 100%;
    transition: transform .3s ease-out;
    > * {
      flex-shrink: 0;
    }
  }
  .img-box {
    height: 52px;
    border-radius: 50%;
  }
  .msgBase-box {
    margin-left: 24px;
    font-size: 14px;
    max-width: calc(100% - 86px);
    flex-shrink: 0;
    h5 {
      color: #606266;
      font-weight: 400;
    }
    p {
      margin-top: 16px;
      overflow: hidden;
      white-space: nowrap;
      text-overflow: ellipsis;
    }
  }
  .delete {
    width: @delete;
    display: flex;
    align-items: center;
    justify-content: space-around;
    background: #FE5656;
    color: white;
    margin-left: auto;
    margin-right: -100px;
  }
}
</style>
