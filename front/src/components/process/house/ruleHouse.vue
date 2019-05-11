<template>
  <div class="ruleHouse">
    <h1>入住规则</h1>
    <div class="titleInput new-box">
      <p>房源名称</p>
      <div class="simulation-input" @click="handleCheckType(0)">
        <i v-if="!data.cTime">入住时间</i>
        <p v-else>{{ data.cTime }}</p>
      </div>
      <div class="simulation-input" @click="handleCheckType(1)">
        <i v-if="!data.lTime">离开时间</i>
        <p v-else>{{ data.lTime }}</p>
      </div>
    </div>
    <Radio class="release-radio" :checked="data.checked" type="checkbox" @click="handleCheck">
      <p class="margin4">是否有前台服务</p>
    </Radio>
    <div class="control-next">
      <ve-button class="primary" @click="handleNext">下一步</ve-button>
    </div>
    <list :data="lists" v-if="showList" :abs="true" @change="handleChange"></list>
  </div>
</template>

<script>
  import list from '../../base/list'
  import Radio from 'components/base/radio'
  const m = new Date().getMonth() + 1;
  import Storage from '../../../utils/localStorage'
  export default {
    name: 'ruleHouse',
    components: {
      list,
      Radio
    },
    data() {
      return {
        data: {
          cTime: '',
          lTime: '',
          checked: true
        },
        now: '',
        showList: false,
        lists: [],
        listCTime: [],
        listLTime: [],
      }
    },
    methods: {
      handleNext() {
        const d = this.data;
        if (d.cTime && d.lTime) {
          this.save();
          this.$router.push({
            path: '/pop/facilityHouse',
            query: {
              direction: 'right',
            }
          })
        } else return this.$msg({
          type: 'error',
          message: '请填写完信息之后再下一步'
        })
      },
      handleCheck(value) {
        this.data.checked = value;
      },
      handleCheckType(index) {
        if (!this.data.cTime && index !== 0) {
          return this.$msg({
            type: 'error',
            message: '请先选择开始时间'
          })
        }
        this.showList = true;
        this.now = index;
      },
      handleChange(index) {
        if (this.now === 0) {
          this.data.cTime =  m + '月' + index + '日';
          if (index === 30) {
            this.next = true;
            this.pushArray(31, this.listLTime, 1)
          } else {
            this.next = false;
            this.pushArray(31, this.listLTime, index + 1)
          }
        } else {
          this.data.lTime = (this.next ? (m + 1) : m) + '月' + index + '日';
          this.pushArray(index + 1, this.listCTime, 1)
        }
        this.showList = false
      },
      pushArray(len = 31, obj, c = 1) {
        obj = [];
        for (let i = c; i < len; i++) {
          obj.push(i)
        }
        this.lists = obj;
      },
      save() {
        // TODO 存储到本地
        const houseData = Storage.get('houseData');
        Storage.set('houseData', Object.assign(houseData || {}, {
          rule: this.data
        }));
      }
    },
    mounted() {
      this.pushArray(31, this.listCTime, 1);
      const houseData = Storage.get('houseData') || {};
      if (houseData.rule) {
        this.data = houseData.rule
      }
    },
    beforeDestroy() {
      this.save();
    }
  }
</script>
