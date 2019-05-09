<template>
  <div class="msg">
    <h1>信息</h1>
    <div class="msg-content">
      <msgBase v-for="(item, index) in infos" :key="item.uuid" @tap="tap" @left="onSwipe" @delete="handleDelete" :data="item"></msgBase>
      <div v-if="!infos.length" class="none-list">您还没有聊天记录，或者已经被删除了。<strong>注：手动删除不能恢复</strong></div>
    </div>
  </div>
</template>

<script>
  import msgBase from 'components/base/msgBase'
  export default {
    name: "msg",
    data() {
      return {
        infos: [{
          src: 'avatar-1.png',
          name: '逸宿好友',
          lastMsg: '昨天发现一个有趣的地方',
          unread: 0,
          uuid: 'xa2d54w3ad343',
        },{
          src: 'avatar-2.png',
          name: '逸宿好友',
          lastMsg: '您是不是落下您的贵重物品了，还有',
          unread: 3,
          uuid: 'xa2d54w3ad32143',
        },{
          src: 'infomation.png',
          name: '系统提示',
          lastMsg: '系统提示',
          unread: 1,
          uuid: 'xa2d54w332ad343',
        },]
      }
    },
    components: {
      msgBase
    },
    methods: {
      onSwipe(ev, item) {
        // console.log(ev.type, item)
      },
      tap(item) {
        console.log('tap', item)
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

    }
  }
</script>

<style scoped lang="less">
  @import "../style/global";
.msg {
  padding: 0 36px;
  h1 {
    font-size: 22px;
    font-weight: 400;
    letter-spacing: 2px;
    margin-bottom: 32px;
    margin-top: 66px - @topIndicator;
  }
  .msg-content {
    margin-top: -24px;
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
