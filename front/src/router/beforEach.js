import router from '../router/'
import cookie from '../utils/cookie'
import Storage from '../utils/localStorage'
const homePath = ['/homeStay', '/collection', '/release', '/msg', '/user'];
router.beforeEach((to, from, next) => {
  if (!cookie.get('first') || !Storage.get('first')) {
    // console.log(to.name)
    if (to.name === 'welcome') return next();
    else return next({name: 'welcome'})
  } else {
    if (to.name === 'welcome') return next({name: 'homeStay'});
  }
  if (to.name === 'login' || to.name === 'signup') {
    return next()
  }
  if (to.path.includes('/PopHouse') && homePath.includes(from.path)) {
    Storage.set('popHouse_before', from.path)
  }
  if (!cookie.get('hotel_')) {
    cookie.set('before_url_', from.path);
    next({name: 'login'})
  }
  next()
});
