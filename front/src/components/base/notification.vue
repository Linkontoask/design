<template>
  <div class="notification">
    <slot></slot>
  </div>
</template>

<script>
  export default {
    name: "notification"
  }
</script>

<style scoped lang="less">
.notification {
  width: 1rem;
  height: 1rem;
  display: flex;
  align-items: center;
  justify-content: space-around;
  color: white;
  font-size: 10px;
  background-color: #FE5656;
  border-radius: 50%;
  margin-right: -12px;
  margin-left: -4px;
}
</style>
