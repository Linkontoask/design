<template>
  <div class="msg">
    <h1>信息</h1>
    <div class="msg-content">
      <msgBase v-for="(item, index) in infos" :key="item.uuid" @tap="tap" @left="onSwipe" @delete="handleDelete" :data="item"></msgBase>
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
    }
  }
</script>

<style scoped lang="less">
.msg {
  padding: 0 36px;
  h1 {
    font-size: 22px;
    font-weight: 400;
    letter-spacing: 2px;
    margin-bottom: 32px;
    margin-top: 66px;
  }
  .msg-content {
    margin-top: -24px;
  }
}
</style>
