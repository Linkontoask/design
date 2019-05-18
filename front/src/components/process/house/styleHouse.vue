<template>
  <div class="styleHouse">
    <h1>您的房源是什么样子的</h1>
    <div class="styleHouse-box new-box">
      <div class="titleInput">
        <p ref="buildType">房源类型</p>
        <div class="simulation-input" @click="handleCheckType(0)">
          <i v-if="!data.buildType">房源的建筑类型</i>
          <p v-else>{{ data.buildType }}</p>
        </div>
      </div>
      <div class="titleInput">
        <p ref="houseType">房源的房型</p>
        <div class="simulation-input" @click="handleCheckType(1)">
          <i v-if="!data.houseType">整个房源、独立房间、合住房间</i>
          <p v-else>{{ data.houseType }}</p>
        </div>
      </div>
      <div class="titleInput">
        <p>房源户型</p>
        <strong>默认都为1，可自己更改，上限为3</strong>
        <div class="simulation-input" @click="handleCheckType(2)">
          <i :class="{'active-input': data.f}">卧室</i>
          <p>{{ data.f }}</p>
        </div>
        <div class="simulation-input" @click="handleCheckType(3)">
          <i :class="{'active-input': data.a}">客厅</i>
          <p>{{ data.a }}</p>
        </div>
        <div class="simulation-input" @click="handleCheckType(4)">
          <i :class="{'active-input': data.c}">卫生间</i>
          <p>{{ data.c }}</p>
        </div>
        <div class="simulation-input" @click="handleCheckType(5)">
          <i :class="{'active-input': data.s}">厨房</i>
          <p>{{ data.s }}</p>
        </div>
        <div class="simulation-input" @click="handleCheckType(6)">
          <i :class="{'active-input': data.q}">书房</i>
          <p>{{ data.q }}</p>
        </div>
        <div class="simulation-input" @click="handleCheckType(7)">
          <i :class="{'active-input': data.h}">阳台</i>
          <p>{{ data.h }}</p>
        </div>
      </div>
    </div>
    <div class="control-next">
      <ve-button class="primary" @click="handleNext">下一步</ve-button>
    </div>
    <list :data="lists" v-if="showList" @change="handleChange"></list>
  </div>
</template>

<script>
  import list from '../../base/list'
  const buildType = ['公寓', '普通住宅', '特色房源', '精品酒店'];
  const houseType = ['整个房源', '独立房间', '合住房间'];
  const num = [1, 2, 3];
  import Storage from '../../../utils/localStorage'
  export default {
    name: 'styleHouse',
    components: {
      list
    },
    data() {
      return {
        showList: false,
        data: {
          buildType: '',
          houseType: '',
          f: '1',
          a: '1',
          c: '1',
          s: '1',
          q: '1',
          h: '1'
        },
        cu: '',
        oi: '',
        lists: [],
      }
    },
    methods: {
      animation(name) {
        const node = this.$refs[name];
        node.classList.add('animated', 'shake', 'faster', 'red');
        function handleAnimationEnd() {
          node.classList.remove('animated', 'shake', 'red');
          node.removeEventListener('animationend', handleAnimationEnd)
        }
        node.addEventListener('animationend', handleAnimationEnd)
      },
      handleNext() {
        const d = this.data;
        if (!d.buildType) {
          this.animation('buildType')
        }
        if (!d.houseType) {
          this.animation('houseType')
        }
        if (d.buildType && d.houseType) {
          this.save();
          this.$router.push({
            path: '/pop/descHouse',
            query: {
              direction: 'right',
            }
          })
        }
      },
      handleChange(index) {
        this.showList = false;
        if (this.cu) {
          this.data[this.cu.n] = index
        } else {
          console.log(this.oi)
          this.data[this.oi] = index;
        }
      },
      handleCheckType(index) {
        const rot = [{n: 'f', i: 2},{n: 'a', i: 3},{n: 'c', i: 4},{n: 's', i: 5},{n: 'q', i: 6},{n: 'h', i: 7},];
        this.cu = rot.find(i => i.i === index);
        switch (index) {
          case 0: this.lists = buildType; this.oi = 'buildType'; break;
          case 1: this.lists = houseType; this.oi = 'houseType'; break;
          default: this.lists = num;
        }
        this.showList = true
      },
      save() {
        // TODO 存储到本地
        const houseData = Storage.get('houseData');
        Storage.set('houseData', Object.assign(houseData || {}, {
          style: this.data
        }));
      }
    },
    mounted() {
      this.lists = buildType;
      const houseData = Storage.get('houseData') || {};
      if (houseData.style) {
        this.data = houseData.style
      }
    },
    beforeDestroy() {
      this.save();
    }
  }
</script>
