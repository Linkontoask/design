<template>
  <div id="homeStay">
    <router-view/>
    <Action></Action>
  </div>
</template>

<script>
  import Action from './components/BactionBar'
  export default {
    components: {
      Action,
    }
  }
</script>

<style lang="less">
#homeStay {
  font-family: PingFangSC-Regular, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  color: #5F6564;
  font-size: 16px;
}
*{
  margin: 0;
  padding: 0
}
li {
  list-style-type: none
}
  .medium {
    font-family: PingFangSC-Medium, sans-serif;
  }
  .clamp2 {
    overflow: hidden;
    text-overflow: ellipsis;
    display: -webkit-box;
    -webkit-line-clamp: 2;
    -webkit-box-orient: vertical;
  }
</style>
