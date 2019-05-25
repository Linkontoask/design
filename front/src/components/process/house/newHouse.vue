<template>
  <div class="newHouse">
    <h1>发布新的房源</h1>
    <div class="new-box">
      <div class="title">
        <p>房源所在位置</p>
        <div @touchend="handleGetPosition">
          <img src="../../../assets/locat.png" alt="not find img">
          <span ref="btn">我的位置</span>
        </div>
      </div>
      <div class="box">
        <ve-plain-input ref="g" @focus="getInputFocusScrollY" @blur="setWindowScrollY" :target="['modify', 'blur']" placeholder="地区" type="reg" inspect="^.+$" message="请输入正确的地区" v-model="data.g" class="input" :errorOptions="{position: 'absolute'}"></ve-plain-input>
        <ve-plain-input ref="city" @focus="getInputFocusScrollY" @blur="setWindowScrollY" :target="['modify', 'blur']" placeholder="城市" type="reg" inspect="^.+$" message="请输入正确的城市" v-model="data.city" class="input" :errorOptions="{position: 'absolute'}"></ve-plain-input>
        <ve-plain-input ref="position" @focus="getInputFocusScrollY" @blur="setWindowScrollY" :target="['modify', 'blur']" placeholder="地址" type="reg" inspect="^.+$" message="请输入正确的地址" v-model="data.position" class="input" :errorOptions="{position: 'absolute'}"></ve-plain-input>
        <ve-plain-input ref="id" @focus="getInputFocusScrollY" @blur="setWindowScrollY" :target="['modify', 'blur']" placeholder="门牌号" type="reg" inspect="^.+$" message="请输入正确的门牌号" v-model="data.id" class="input" :errorOptions="{position: 'absolute'}"></ve-plain-input>
      </div>
    </div>
    <div class="control-next">
      <ve-button class="primary" @click="handleNext">下一步</ve-button>
    </div>
  </div>
</template>

<script>
  import Storage from '../../../utils/localStorage'
  export default {
    name: 'newHouse',
    data() {
      return {
        data: {
          g: '',
          city: '',
          position: '',
          id: ''
        }
      }
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
        let ok = true;
        Object.keys(this.data).forEach(item => {
          if (!this.data[item]) {
            ok = false;
            this.$refs[item].error = true;
            const node = this.$refs[item].$el.children[1];
            const btn = this.$refs.btn;
            node.classList.add('animated', 'bounce', 'faster');
            btn.classList.add('animated', 'flash', 'faster');
            function handleAnimationEnd() {
              node.classList.remove('animated', 'bounce');
              btn.classList.remove('animated', 'flash');
              node.removeEventListener('animationend', handleAnimationEnd)
              btn.removeEventListener('animationend', handleAnimationEnd)
            }

            node.addEventListener('animationend', handleAnimationEnd)
            btn.addEventListener('animationend', handleAnimationEnd)
          }
        })
        console.log(ok, this.data)
        if (!ok) return;
        this.save();
        this.$router.push({
          path: '/pop/confirmHouse',
          query: {
            direction: 'right',
          }
        })
      },
      save() {
        //TODO 存储数据到本地
        const houseData = Storage.get('houseData');
        Storage.set('houseData', Object.assign(houseData || {}, {
          position: this.data
        }));
      }
    },
    mounted() {
      const houseData = Storage.get('houseData') || {};
      if (houseData.position) {
        this.data = houseData.position
      }
    },
    beforeDestroy() {
      this.save();
    }
  }
</script>
