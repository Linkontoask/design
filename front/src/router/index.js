import Vue from 'vue'
import Router from 'vue-router'

const Base = () => import(/* webpackChunkName: "base" */ '../components/base');
const Login = () => import(/* webpackChunkName: "login" */ '../components/login');
const Signup = () => import(/* webpackChunkName: "registered" */ '../components/registered');
const HomeStay = () => import(/* webpackChunkName: "registered" */ '../views/homeStay');
const Collection = () => import(/* webpackChunkName: "collection" */ '../views/collection');
const Release = () => import(/* webpackChunkName: "release" */ '../views/release');
const User = () => import(/* webpackChunkName: "user" */ '../views/user');
const Msg = () => import(/* webpackChunkName: "msg" */ '../views/msg');

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
    {
      path: '/collection',
      name: 'collection',
      component: Collection
    },
    {
      path: '/release',
      name: 'release',
      component: Release
    },
    {
      path: '/msg',
      name: 'msg',
      component: Msg
    },
    {
      path: '/user',
      name: 'user',
      component: User
    },
  ]
})
