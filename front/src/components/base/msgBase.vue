<template xmlns:v-hammer="http://www.w3.org/1999/xhtml">
  <div class="msgBase" v-hammer:tap="handleTap" v-hammer:swipe.left.right="handleSwiper" :class="{hide: is_hide}">
    <div :class="{activeLeft: is_left}" class="list-box">
      <div class="img-box" :style="{backgroundImage: `url(${require('../../static/img/' + data.src)})`}"></div>
      <notification v-if="data.unread !== 0">{{ data.unread }}</notification>
      <div class="msgBase-box">
        <h5>{{ data.name }}</h5>
        <p>{{ data.lastMsg }}</p>
      </div>
      <div class="delete" v-hammer:tap="handleDelete">删除</div>
    </div>
  </div>
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
      }
    },
    data() {
      return {
        is_left: false,
        is_hide: false
      }
    },
    methods: {
      handleTap(ev) {
        if (ev.target.className === 'delete') {
          return false;
        }
        this.is_left = false;
        this.$emit('tap', this.data)
      },
      handleSwiper(ev) {
        this.is_left = ev.type === 'swipeleft';
        this.$emit('left', ev, this.data)
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
  height: 69px;
  padding: 24px 0 0;
  overflow: hidden;
  transition: height .3s, padding .3s;
  > .list-box {
    position: relative;
    display: flex;
    align-items: stretch;
    padding-bottom: 16px;
    border-bottom: 1px solid #E4ECE8;
    transition: transform .3s ease-out;
    > * {
      flex-shrink: 0;
    }
  }
  .img-box {
    width: 52px;
    height: 52px;
    border-radius: 50%;
    background: no-repeat center;
  }
  .msgBase-box {
    margin-left: 16px;
    font-size: 14px;
    flex: 1;
    max-width: 258px;
    h5 {
      color: #606266;
      font-weight: 400;
    }
    p {
      margin-top: 8px;
      overflow: hidden;
      white-space: nowrap;
      text-overflow: ellipsis;
    }
  }
  .delete {
    position: absolute;
    right: -@delete;
    top: 0;
    width: @delete;
    height: 68px;
    display: flex;
    align-items: center;
    justify-content: space-around;
    background: #FE5656;
    color: white;
  }
}
</style>
