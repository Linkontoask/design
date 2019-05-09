<template>
  <div class="newHouse">
    <h1>确认具体位置</h1>
    <div id="container"></div>
  </div>
</template>

<script>
  export default {
    name: 'confirmHouse',
    mounted() {
      var a = document.createElement('script');
      a.src = 'https://webapi.amap.com/maps?v=1.4.14&key=d4123dab1e07c48600ba7a2e3ea143f7';
      document.body.appendChild(a);
      a.onload = () => {
        console.log('aa')
        const map = new AMap.Map('container', {
          resizeEnable: true,
          zoom:11,
          center: [116.397428, 39.90923]
        });
      };

    },
    beforeMount() {

    }
  }
</script>

<style lang="less" scoped>
  #container {
    position: absolute;
    left: 0;
    top: 0;
    width: 100%;
    height: calc(100vh - 108px);
  }
</style>
