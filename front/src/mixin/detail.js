import Animocon from '../animation/animation'


export default {
  methods: {
    // 点赞动画
    heartAnimation() {
      let vm = this;
      let el16 = vm.$refs.heartBox, el16span = vm.$refs.heart;
      let opacityCurve16 = mojs.easing.path('M0,0 L25.333,0 L75.333,100 L100,0');
      let translationCurve16 = mojs.easing.path('M0,100h25.3c0,0,6.5-37.3,15-56c12.3-27,35-44,35-44v150c0,0-1.1-12.2,9.7-33.3c9.7-19,15-22.9,15-22.9');
      let squashCurve16 = mojs.easing.path('M0,100.004963 C0,100.004963 25,147.596355 25,100.004961 C25,70.7741867 32.2461944,85.3230873 58.484375,94.8579105 C68.9280825,98.6531013 83.2611815,99.9999999 100,100');
      new Animocon.Animocon(el16, {
        tweens: [
          // burst animation (circles)
          new mojs.Burst({
            parent: el16,
            count: 6,
            radius: {0: 150},
            degree: 50,
            angle: -25,
            opacity: 0.3,
            children: {
              fill: '#FF6767',
              scale: 1,
              radius: {'rand(5,15)': 0},
              duration: 1700,
              delay: 350,
              easing: mojs.easing.bezier(0.1, 1, 0.3, 1)
            }
          }),
          new mojs.Burst({
            parent: el16,
            count: 3,
            degree: 0,
            radius: {80: 250},
            angle: 180,
            children: {
              top: [45, 0, 45],
              left: [-15, 0, 15],
              shape: 'line',
              radius: {60: 0},
              scale: 1,
              stroke: '#FF6767',
              opacity: 0.4,
              duration: 650,
              delay: 200,
              easing: mojs.easing.bezier(0.1, 1, 0.3, 1)
            },
          }),
          // icon scale animation
          new mojs.Tween({
            duration: 500,
            onUpdate: (progress) => {
              let translateProgress = translationCurve16(progress),
                squashProgress = squashCurve16(progress),
                scaleX = 1 - 2 * squashProgress,
                scaleY = 1 + 2 * squashProgress;

              el16span.style.WebkitTransform = el16span.style.transform = 'translate3d(0,' + -180 * translateProgress + 'px,0) scale3d(' + scaleX + ',' + scaleY + ',1)';

              el16span.style.opacity = opacityCurve16(progress);

              el16span.style.color = progress >= 0.75 ? '#FF6767' : '#fff';
            }
          })
        ],
        onUnCheck() {
          vm.handleCollection(false);
          el16span.style.color = '#fff';
        },
        onCheck() {
          navigator.vibrate = navigator.vibrate || navigator.webkitVibrate || navigator.mozVibrate || navigator.msVibrate;
          try {
            navigator.vibrate(50);
          } catch (e) {

          }
          vm.handleCollection(true);
        }
      });
    }
  }
}
