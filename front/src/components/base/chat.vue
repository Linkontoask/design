<template>
  <div class="chat">
    <div class="top">
      <div class="control close" @touchend="handleClose"><p></p><p></p></div>
      <h3>{{ user.name }}</h3>
    </div>
    <div class="chat-content">
      <ul>
        <li v-for="(item, index, key) in chatRecord" :key="index" :class="item.own ? 'own' : 'other'">
          <img class="avatar" :src="require('../../assets/'+item.avatar)" alt="">
          <div class="content">{{ item.content }}</div>
        </li>
      </ul>
    </div>
  </div>
</template>

<script>
  export default {
    name: "chat",
    data() {
      return {
        user: {
          name: 'Link'
        },
        chatRecord: [{content: '你好', avatar: 'avatar-1.png'}, {content: '你好，这使得flexbox成为这在响应式页面的最佳工具。目前，在许多“移动优先”的设计方案中，都包含了许多排序规则，来创建各种不同的内容阅读顺序', avatar: 'avatar-3.png', own: true}]
      }
    },
    methods: {
      handleClose() {
        this.$router.back()
      }
    },
    beforeMount() {
      this.user.name = this.$route.query.name
    }

  }
</script>

<style scoped lang="less">
.chat {
  width: 100%;
  height: 100vh;
  overflow: auto;
  background-color: #F5F5F5;
  .chat-content {
    ul {
      padding: 24px 24px;
      li {
        display: flex;
        img.avatar {
          width: 42px;
          height: 42px;
          border-radius: 50%;
          margin-right: 12px;
        }
        div.content {
          position: relative;
          border-radius: 4px;
          padding: 10px;
          background-color: white;
          border: 1px solid #E3E9E6;
          font-size: 14px;
        }
        div.content::before, div.content::after {
          content: '';
          position: absolute;
          left: -24px;
          top: 8px;
          width: 0;
          height: 0;
          border: 12px solid transparent;
          border-right: 12px solid #E3E9E6;
        }
        div.content::after {
          left: -23px;
          border-right-color: #fff;
        }
      }
      li.own {
        direction: rtl;
        div.content {
        }
        div.content::before, div.content::after {
          left: auto;
          right: -24px;
          border: 12px solid transparent;
          border-left: 12px solid #E3E9E6;
        }
        div.content::after {
          right: -23px;
          border-left-color: #fff;
        }
        img.avatar {
          margin-left: 12px;
          margin-right: 0;
        }
      }
      li + li {
        margin-top: 24px;
      }
    }
  }
  .top {
    height: 60px;
    background-color: white;
    display: flex;
    align-items: center;
    border-bottom: 1px solid #E4ECE8;
    h3 {
      flex: 1;
      text-align: center;
      font-size: 16px;
    }
  }
  .control {
    position: absolute;
    top: 14px;
    left: 8px;
    height: 36px;
    width: 46px;
  }
  .close, .left {
    display: flex;
    justify-content: space-between;
    align-items: center;
    z-index: 2;
    p {
      position: absolute;
      left: 0;
      top: 0;
      right: 0;
      bottom: 0;
      margin: auto;
      width: 22px;
      height: 2px;
      transition: transform .2s;
      transform: rotate(45deg);
      background-color: #333;
    }
    p + p {
      transform: rotate(-45deg);
    }
  }
}
</style>
