<template>
  <div class="msg">
    <h1>信息</h1>
    <div class="msg-content" ref="msgContent">
      <ul>
        <msgBase v-for="(item, index) in infos" :key="item.uuid"
                 @tap="value => tap(value, index)"
                 @left="value => onSwipe(value, index)"
                 @delete="handleDelete"
                 :left="haveLeft[index]"
                 :data="item"></msgBase>
      </ul>
      <div v-if="!infos.length" class="none-list">您还没有聊天记录，或者已经被删除了。<strong>注：手动删除不能恢复</strong></div>
    </div>
    <Chat :showChat="showChat" :name="name" @close="close"></Chat>
  </div>
</template>

<script>
  import BScroll from 'better-scroll'
  import msgBase from 'components/base/msgBase'
  import Chat from '../components/base/chat'
  import list from '../static/chatList'
  import { mapMutations} from 'vuex'
  export default {
    name: "msg",
    data() {
      return {
        showChat: false,
        name: '',
        haveLeft: [false, false, false],
        activeIndex: 0,
        infos: list
      }
    },
    components: {
      msgBase,
      Chat
    },
    methods: {
      ...mapMutations([
        'IS_SHOW_NATION',
      ]),
      close() {
        this.showChat = false;
        this.IS_SHOW_NATION(true);
      },
      onSwipe(is_left, index) {
        this.haveLeft = [false, false, false];
        this.$set(this.haveLeft, index, is_left)
      },
      tap(item ,index) {
        this.showChat = true;
        this.IS_SHOW_NATION(false);
        this.infos[index].unread = 0;
        // IS_SHOW_NATION
        this.$nextTick(() => {
          this.name = item.name;
        })
      },
      handleDelete(uuid) {
        setTimeout(() => {
          this.infos.splice(this.infos.findIndex(d => d.uuid === uuid), 1);
        }, 300);
      }
    },
    activated() {
      console.log('msg', 'keep-alive');
    },
    mounted() {
      this.$nextTick(() => {
        this.scroll = new BScroll(this.$refs.msgContent, {
          scrollX: false,
          scrollY: true,
        });
      })
    }
  }
</script>

<style scoped lang="less">
  @import "../style/global";
.msg {
  padding: 0 24px;
  h1 {
    font-size: 22px;
    font-weight: 400;
    letter-spacing: 2px;
    margin-bottom: 32px;
    margin-top: 66px - @topIndicator;
  }
  .msg-content {
    max-height: calc(100vh - 9.5rem);
    overflow: hidden;
    .none-list {
      color: #C5D1CD;
      margin-top: 310px;
      line-height: 2;
      strong {
        display: block;
      }
    }
  }
}
</style>
