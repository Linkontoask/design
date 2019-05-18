<template>
  <div class="descHouse">
    <h1>描述一下您的房源</h1>
    <div class="titleInput new-box">
      <p>房源名称</p>
      <ve-plain-input ref="name" :target="['modify', 'blur']" placeholder="建议：地标+特色 | 周围景点" type="reg" inspect="^.+$" message="请输入房源名称" v-model="data.name" class="input" :errorOptions="{position: 'absolute'}"></ve-plain-input>
    </div>
    <div class="titleInput new-box">
      <p>房源特色</p>
      <textarea class="textarea" v-model="data.desc" name="" id="" cols="30" rows="10" placeholder="介绍房子的特色，比如理景点多远，周围有什么美食，房屋有哪些设施，有哪些服务、早餐之类的"></textarea>
    </div>
    <div class="control-next">
      <ve-button class="primary" @click="handleNext">下一步</ve-button>
    </div>
  </div>
</template>

<script>
  import Storage from '../../../utils/localStorage'
  export default {
    name: 'descHouse',
    data() {
      return {
        data: {}
      }
    },
    methods: {
      handleNext() {
        const d = this.data;
        if (d.name) {
          this.save();
          this.$router.push({
            path: '/pop/ruleHouse',
            query: {
              direction: 'right',
            }
          })
        } else {
          this.$refs.name.error = true;
          const node = this.$refs.name.$el.children[1];
          node.classList.add('animated', 'bounce', 'faster');
          function handleAnimationEnd() {
            node.classList.remove('animated', 'bounce');
            node.removeEventListener('animationend', handleAnimationEnd)
          }

          node.addEventListener('animationend', handleAnimationEnd)
        }
      },
      save() {
        // TODO 存储到本地
        const houseData = Storage.get('houseData');
        Storage.set('houseData', Object.assign(houseData || {}, {
          desc: this.data
        }));
      }
    },
    mounted() {
      const houseData = Storage.get('houseData') || {};
      if (houseData.desc) {
        this.data = houseData.desc
      }
    },
    beforeDestroy() {
      this.save();
    }
  }
</script>
