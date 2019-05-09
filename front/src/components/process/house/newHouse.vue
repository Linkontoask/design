<template>
  <div class="newHouse">
    <h1>发布新的房源</h1>
    <div class="new-box">
      <div class="title">
        <p>房源所在位置</p>
        <div @touchend="handleGetPosition">
          <img src="../../../assets/locat.png" alt="not find img">
          <span>我的位置</span>
        </div>
      </div>
      <div class="box">
        <ve-plain-input ref="g" :target="['modify', 'blur']" placeholder="地区" type="reg" inspect="^.+$" message="请输入正确的地区" v-model="data.g" class="input" :errorOptions="{position: 'absolute'}"></ve-plain-input>
        <ve-plain-input ref="city" :target="['modify', 'blur']" placeholder="城市" type="reg" inspect="^.+$" message="请输入正确的城市" v-model="data.city" class="input" :errorOptions="{position: 'absolute'}"></ve-plain-input>
        <ve-plain-input ref="position" :target="['modify', 'blur']" placeholder="地址" type="reg" inspect="^.+$" message="请输入正确的地址" v-model="data.position" class="input" :errorOptions="{position: 'absolute'}"></ve-plain-input>
        <ve-plain-input ref="id" :target="['modify', 'blur']" placeholder="门牌号" type="reg" inspect="^.+$" message="请输入正确的门牌号" v-model="data.id" class="input" :errorOptions="{position: 'absolute'}"></ve-plain-input>
      </div>
    </div>
    <div class="control-next">
      <ve-button class="primary" @click="handleNext">下一步</ve-button>
    </div>
  </div>
</template>

<script>
  export default {
    name: 'newHouse',
    data() {
      return {
        data: {}
      }
    },
    mounted() {
      // window.localStorage.setItem('current_hotel', this.$route.path);
    },
    methods: {
      handleGetPosition() {
        this.data = {
          g: '中国大陆',
          city: '重庆市',
          position: '南岸区崇文路口2号',
          id: '重庆邮电大学'
        }
      },
      handleNext() {
        const ref = this.$refs;
        ref.g.mergeMesh('blur');
        ref.city.mergeMesh('blur');
        ref.position.mergeMesh('blur');
        ref.id.mergeMesh('blur');
        if (ref.g.error || ref.city.error || ref.position.error || ref.id.error) {
          return this.$msg({
            type: 'error',
            message: '请填写完信息之后再下一步'
          })
        }
        this.$router.push({
          path: '/pop/confirmHouse',
          query: {
            direction: 'right',
          }
        })
      }
    }
  }
</script>
