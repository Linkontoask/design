/**
 * 解决微信input失去焦点后下方空白问题
 * @param Vue
 * @param option
 */
const userAgent = navigator.userAgent;
exports.install = (Vue, option) => {
  let y = 0;
  Vue.prototype.getInputFocusScrollY = () => {
    y = window.scrollY;
  };
  Vue.prototype.setWindowScrollY = (behaver, force = false) => {
    let scrollY = y;
    if (/\d+/.test(behaver)) {
      scrollY = behaver
    }
    if (userAgent.indexOf('MicroMessenger') !== -1 || force) {
      window.scrollTo({top: scrollY, left: 0, behavior: "smooth"});
    }
  };
  Vue.prototype.speak = (voice, char) => {
    this.speechInstance = new SpeechSynthesisUtterance(char);
    this.speechInstance.voiceURI = voice;
    speechSynthesis.speak(this.speechInstance);
  }
};