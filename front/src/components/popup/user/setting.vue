<template>
  <div class="setting">
    <h1>{{$i18n.t('base.setting')}}</h1>
    <div>
      <ul>
        <li v-for="(item, index) in list" :key="index" @touchend="handleViewList(index)" v-show="isReading || index !== 4">
          <p>{{ item.name }}</p>
          <span class="clamp1">{{ item.result }}</span>
        </li>
      </ul>
    </div>
    <ve-button class="primary" @click="handleOut">{{$i18n.t('base.out')}}</ve-button>
    <List :data="listView.lists" v-if="listView.showList" @change="handleChange"></List>
  </div>
</template>

<script>
  import axios from '../../../utils/axios'
  import cookie from '../../../utils/cookie'
  import Storage from '../../../utils/localStorage'
  import List from '../../base/list'
  export default {
    name: 'setting',
    components: {
      List
    },
    data() {
      return {
        list: [
          {name: this.$i18n.t('setting.notice'), result: this.$i18n.t('base.close'), id: 0},
          {name: this.$i18n.t('setting.lang'), result: this.$i18n.t('lang.zh'), id: 1},
          {name: this.$i18n.t('setting.font', ['']), result: this.$i18n.t('setting.font', [this.$i18n.t('leave.normal')]), id: 2},
          {name: this.$i18n.t('setting.reading'), result: this.$i18n.t('base.close'), id: 3},
          {name: this.$i18n.t('setting.readingSetting'), result: 'Microsoft Huihui Desktop - Chinese (Simplified)', id: 4}
        ],
        notice: [{name: this.$i18n.t('base.open')},{name: this.$i18n.t('base.close')},],
        reading: [{name: this.$i18n.t('base.open'), s: '1'},{name: this.$i18n.t('base.close'), s: '2'},],
        language: [{name: this.$i18n.t('lang.zh'), class: 'zh'},
          {name: this.$i18n.t('lang.en'), class: 'en'},
          {name: this.$i18n.t('lang.fr'), class: 'fr'},
          {name: this.$i18n.t('lang.de'), class: 'de'},
          {name: this.$i18n.t('lang.af'), class: 'af'},],
        fontSize: [{name: this.$i18n.t('setting.font', [this.$i18n.t('leave.normal')]), size: 16},
          {name: this.$i18n.t('setting.font', [this.$i18n.t('leave.general')]), size: 18},
          {name: this.$i18n.t('setting.font', [this.$i18n.t('leave.big')]), size: 24}],
        check: 0,
        listView: {
          lists: [],
          showList: false
        },
        voiceData: [],
        queryParams: {},
        isReading: false
      }
    },
    watch: {
    },
    methods: {

      onSpeak (voice) {
        this.speechInstance = new SpeechSynthesisUtterance('设置成功');
        this.speechInstance.voiceURI = voice;
        speechSynthesis.speak(this.speechInstance);
      },

      handleViewList(index) {
        this.check = index;
        if (index === 0) {
          this.listView.lists = this.notice
        } else if (index === 1) {
          this.listView.lists = this.language
        } else if (index === 2){
          this.listView.lists = this.fontSize
        } else if (index === 3) {
          this.listView.lists = this.reading
        } else if (index === 4){
          this.listView.lists = this.voiceData
        }
        this.listView.showList = true
      },
      handleChange(value) {
        this.listView.showList = false;
        this.list[this.check].result = value.name;
        if (value.class) {
          const lang = Storage.get('local-language');
          if (lang === value.class) return
          Storage.set('local-language', value.class);
          // this.$i18n.locale = value.class; // 更改语言
          document.documentElement.setAttribute('lang', value.class);
          document.location.reload();
        }
        if (value.size) {
          const size = value.size / 16 + 'rem';
          Storage.set('fontSize', size);
          document.documentElement.style.fontSize = size
        }
        if (value.s) {
          this.isReading = value.s === '1';
          Storage.set('reading', value.s); // 1 = 开 / 2 = 关
        }
        if (value.lang) {
          this.onSpeak(value.voiceURI)
        }
      },
      async handleOut() {
        cookie.remove('hotel_');
        Storage.remove('houseData');
        Storage.remove('now_checked_house');
        Storage.remove('before_url_house_');
        Storage.remove('popHouse_before');
        Storage.remove('user_info_');
        this.$router.push({name: 'login'});
        const data = await axios.get.call(this, '/hotel/login_out/', {});
        this.$msg({
          type: 'success',
          message: data.e
        });
      }
    },
    mounted() {
      const reading = Storage.get('reading');
      this.isReading = reading === '1';
      if (reading === '1') {
        this.list[3].result = this.$i18n.t('base.open');
      } else {
        this.list[3].result = this.$i18n.t('base.close');
      }
      const lang = Storage.get('local-language');
      switch (lang) {
        case 'zh': this.list[1].result =  this.$i18n.t('lang.zh'); break;
        case 'af': this.list[1].result =  this.$i18n.t('lang.af'); break;
        case 'de': this.list[1].result =  this.$i18n.t('lang.de'); break;
        case 'en': this.list[1].result =  this.$i18n.t('lang.en'); break;
        case 'fr': this.list[1].result =  this.$i18n.t('lang.fr'); break;
      }
      const size = Storage.get('fontSize');
      switch (size) {
        case '1rem': this.list[2].result = this.$i18n.t('setting.font', [this.$i18n.t('leave.normal')]); break;
        case '1.125rem': this.list[2].result = this.$i18n.t('setting.font', [this.$i18n.t('leave.general')]); break;
        case '1.5rem': this.list[2].result = this.$i18n.t('setting.font', [this.$i18n.t('leave.big')]); break;
      }
      let timer = setInterval(() => {
        if(!this.voiceData.length) {
          //获取语言包
          this.voiceData = speechSynthesis.getVoices();
        } else {
          this.list[4].result = this.voiceData[0].name;
          clearInterval(timer);
        }
      }, 500);
    },
    beforeMount() {

    }
  }
</script>

<style scoped lang="less">
.setting {
  position: relative;
  padding: 86px 24px 24px;
  h1 {
    font-size: 20px;
    color: #2E312F;
    margin-bottom: 55px;
  }
  .primary {
    float: none;
    width: 100%;
  }
  ul {
    padding-bottom: 36px;
    li {
      display: flex;
      align-items: center;
      justify-content: space-between;
      padding-bottom: 12px;
      border-bottom: 1px solid #E4ECE8;
      span {
        color: #A0ABA9;
        font-weight: lighter;
        margin-left: 10px;
        word-break: break-all;
      }
      p {
        flex-shrink: 0;
      }
      & + li {
        margin-top: 24px;
      }
    }
  }
}
</style>
