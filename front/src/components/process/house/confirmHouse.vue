<template>
  <div class="newHouse">
    <h1>确认具体位置</h1>
    <div id="container"></div>
    <div class="control-next">
      <ve-button class="primary" @click="handleNext">下一步</ve-button>
    </div>
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
        const map = new AMap.Map('container', {
          resizeEnable: true,
          zoom: 15,
          center: [106.613922, 29.53832]
        });
      };
    },
    methods: {
      handleNext() {
        this.$router.push({
          path: '/pop/styleHouse',
          query: {
            direction: 'right',
          }
        })
      }
    },
    beforeMount() {

    }
  }
</script>

<style lang="less" scoped>
  #container {
    position: absolute;
    left: 0;
    top: 72px;
    width: 100%;
    height: calc(100vh - 8.8rem);
    overflow: auto;
  }
</style>
