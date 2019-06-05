import Vue from 'vue';
import VueI18n from 'vue-i18n';
import zh from './zh-CN';
import en from './en-US';
import af from './af';
import de from './de';
import fr from './fr';
import Storage from '../../utils/localStorage'

const lang = Storage.get('local-language') || navigator.language || 'zh-CN';

Vue.use(VueI18n);

document.documentElement.setAttribute('lang', lang);
const i18n = new VueI18n({
  locale: lang,
  fallbackLocale: 'en-US',
  messages: {
    'zh-CN': zh,
    'en-US': en,
    af,
    de,
    fr
  },
});

export default i18n;
