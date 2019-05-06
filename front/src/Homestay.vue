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
  font-family: 'Avenir', Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  color: #2c3e50;
}
*{margin: 0;padding: 0}
</style>
