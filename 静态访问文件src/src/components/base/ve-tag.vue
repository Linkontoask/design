<template>
  <div class="ve-tag" :style="{backgroundColor: bgColor}">
    <slot></slot>
  </div>
</template>

<script>
  export default {
    props: {
      bgColor: {
        type: String,
        default: '#F29341'
      }
    }
  }
</script>

<style lang="less" scoped>
.ve-tag {
  display: inline-block;
  padding: 2px 4px;
  color: white;
  font-size: 12px;
  border-radius: 4px;
  & + .ve-tag {
    margin-left: 10px;
  }
}
</style>
