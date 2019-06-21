<template>
  <div class="MapGd">
    <!--<a href="https://uri.amap.com/marker?position=116.473195,39.993253">-->
      <div class="container" id="container" :style="{height: height}"></div>
    <!--</a>-->
  </div>
</template>

<script>
  export default {
    name: "MapGd",
    props: {
      height: {
        type: String,
        default: '246px'
      }
    },
    mounted() {
      const a = document.createElement('script');
      a.src = 'https://webapi.amap.com/maps?v=1.4.14&key=d4123dab1e07c48600ba7a2e3ea143f7';
      document.body.appendChild(a);
      a.onload = () => {
        const map = new AMap.Map('container', {
          resizeEnable: true,
          zoom: 15,
          center: [106.613922, 29.53832]
        });
      };
    }
  }
</script>

<style scoped lang="less">
.MapGd {
  #container {
    left: 0;
    top: 0;
    width: 100%;
    height: 246px;
    overflow: hidden;
  }
}
</style>
