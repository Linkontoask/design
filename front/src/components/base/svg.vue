<template>
  <svg :class="[className, 'svg-icon']" aria-hidden="true">
    <use :xlink:href="svgId"/>
  </svg>
</template>

<script>
  export default {
    name: 'SvgIcon',
    props: {
      svg: {
        type: String,
        required: true,
      },
      className: {
        type: String,
        default: '',
      },
    },
    computed: {
      svgId() {
        return `#${this.svg}`
      },
    },
  }
</script>

<style scoped>
  .svg-icon {
    width: 10rem;
    height: 10rem;
    vertical-align: -0.15em;
    fill: currentColor;
    overflow: hidden;
  }
</style>