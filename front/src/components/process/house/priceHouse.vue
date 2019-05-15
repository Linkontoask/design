<template>
  <div class="priceHouse">
    <h1>您的房源价格和图片</h1>
    <div class="img-box-release">
      <p>房源图片</p>
      <upload
              ref="upload"
              @append="append"
              @change="handleFileListChange"
      ></upload>
    </div>
    <div class="titleInput new-box">
      <p>基础价格</p>
      <div class="box">
        <ve-plain-input ref="price" :target="['modify', 'blur']" placeholder="请输入入住房源需要支付的金额" type="reg" inspect="^\d+$" message="请输入正确的金额" v-model="data.priceHouse" class="input" :errorOptions="{position: 'absolute'}"></ve-plain-input>
      </div>
    </div>
    <div class="titleInput new-box">
      <p>价格规则</p>
      <div class="simulation-input" @click="handleCheckType">
        <i v-if="!dataView.type">付款方式</i>
        <p v-else>{{ dataView.type }}</p>
      </div>
    </div>
    <div class="control-next">
      <ve-button class="primary" @click="handleRelease">发布</ve-button>
    </div>
    <list :data="dataView.lists" v-if="dataView.showList" @change="handleChange"></list>
  </div>
</template>

<script>
  import list from '../../base/list'
  import upload from '../../base/upload'
  import axios from '../../../utils/axios'
  import Storage from '../../../utils/localStorage'
  export default {
    name: 'priceHouse',
    components: {
      list,
      upload
    },
    data() {
      return {
        data: {
          price: ''
        },
        dataView: {
          type: '',
          showList: false,
          lists: [{name: '支付宝', id: 0},{name: '微信', id: 1},{name: '银联', id: 2},]
        },
        releaseData: {},
        fileList: [],
        formDate: new FormData()
      }
    },
    methods: {
      append(file, name) {
        this.formDate.append('files', file, name);
      },
      handleSuccess() {
        Storage.remove('houseData');
        Storage.remove('current_hotel');
        this.$msg({
          type: 'success',
          message: '发布成功，等待收益吧'
        });
        this.$router.push({
          path: '/release'
        })
      },
      handleError(err) {
        console.log(err)
      },
      handleFileListChange(fileList) {
        this.fileList = fileList;
      },
      async handleRelease() {
        this.$refs.price.mergeMesh('blur');
        if (this.fileList.length <= 0) {
          this.$msg({
            type: 'error',
            message: '请上传房源图片'
          })
        } else if (this.dataView.type === '') {
          this.$msg({
            type: 'error',
            message: '请选择付款方式'
          })
        } else if (Number(this.data.price) >= 1000) {
          this.$msg({
            type: 'error',
            message: '房源的价格不能超过1000'
          })
        } else if (!this.$refs.price.error) {
          //TODO 发布房源，组装数据给后台
          this.formDate = new FormData();
          this.$refs.upload.$refs.upload.submit(); // 子组件upload
          this.getReleaseData();
          this.formDate.append('other', JSON.stringify(this.releaseData));
          const data = await axios.postFile.call(this, '/hotel/hotel_room/', this.formDate);
          if (data.r === 0) {
            this.handleSuccess()
          }
        }
      },
      handleCheckType() {
        this.dataView.showList = true;
      },
      handleChange(obj) {
        if (!this.dataView.type.includes(obj.name)) {
          this.dataView.type = ((this.dataView.type !== '' ? this.dataView.type + ',' : '') + obj.name);
        }
        this.dataView.showList = false;
      },
      getReleaseData() {
        const data = JSON.parse(window.localStorage.getItem('houseData'));
        delete data.rimView;
        // 图片在file KEY 下，应该有多个
        let facitityHouse = [];
        data.facitity.forEach((i, index) => {
          if (i) {
            facitityHouse.push(index)
          }
        });
        this.releaseData = {
          posHouse: data.position.city + '-' + data.position.position + ',' + data.position.id,
          around: data.rim.food || [],
          typeHouse: data.style.houseType,
          roomHouse: data.style.buildType,
          // signerHouse: JSON.stringify(data.style),
          nameHouse: data.desc.name,
          descHouse: data.desc.desc,
          rule: [data.rule.cTime, data.rule.lTime],
          facitityHouse: facitityHouse,
          priceHouse: this.data.priceHouse
        };
      }
    },
    beforeMount() {
    }
  }
</script>
