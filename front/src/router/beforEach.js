import router from '../router/'
import cookie from '../utils/cookie'

router.beforeEach((to, from, next) => {
  if (to.name === 'login' || to.name === 'signup') {
    return next()
  }
  /*if (!cookie.get('hotel_')) {
    cookie.set('before_url_', from.path);
    next({name: 'login'})
  }*/
  next()
});
