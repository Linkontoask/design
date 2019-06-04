import Vue from 'vue';
import VueI18n from 'vue-i18n';
import zh from './zh';
import en from './en';
import af from './af';
import de from './de';
import fr from './fr';
import Storage from '../../utils/localStorage'

Vue.use(VueI18n);

const i18n = new VueI18n({
  locale: Storage.get('local-language') || 'zh',
  fallbackLocale: 'en',
  messages: {
    zh,
    en,
    af,
    de,
    fr
  },
});

export default i18n;
