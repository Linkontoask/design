import Vue from 'vue'
import Router from 'vue-router'

const Base = () => import(/* webpackChunkName: "base" */ './components/base');
const Login = () => import(/* webpackChunkName: "login" */ './components/login');
const Signup = () => import(/* webpackChunkName: "registered" */ './components/registered');

Vue.use(Router);

export default new Router({
  routes: [
    {
      path: '/',
      name: 'home',
      component: Base
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
