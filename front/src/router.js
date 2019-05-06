import Vue from 'vue'
import Router from 'vue-router'

const Base = () => import(/* webpackChunkName: "base" */ './components/base');
const Login = () => import(/* webpackChunkName: "login" */ './components/login');
const Signup = () => import(/* webpackChunkName: "registered" */ './components/registered');
const HomeStay = () => import(/* webpackChunkName: "registered" */ './views/homeStay');

Vue.use(Router);

export default new Router({
  routes: [
    {
      path: '/',
      redirect: '/homeStay'
    },
    {
      path: '/homeStay',
      name: 'homeStay',
      component: HomeStay
    },
    {
      path: '/login',
      name: 'login',
      component: Login
    },
    {
      path: '/signup',
      name: 'signup',
      component: Signup
    },
  ]
})
