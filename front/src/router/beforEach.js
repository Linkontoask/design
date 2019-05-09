import router from '../router/'
import cookie from '../utils/cookie'

router.beforeEach((to, from, next) => {
  if (to.name === 'login' || to.name === 'signup') {
    return next()
  }
  if (!cookie.get('hotel_')) {
    next({name: 'login'})
  }
  next()
});
