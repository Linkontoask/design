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

const Pop = () => import(/* webpackChunkName: "pop" */ '../components/popup/popBase');
const PopSearch = () => import(/* webpackChunkName: "PopSearch" */ '../components/popup/popSearch');
const popHouse = () => import(/* webpackChunkName: "popHouse" */ '../components/popup/popHouse');


const normalSearch = () => import(/* webpackChunkName: "normalSearch" */ '../components/normalSearch');
const resultSearch = () => import(/* webpackChunkName: "resultSearch" */ '../components/resultSearch');
const houseList = () => import(/* webpackChunkName: "houseList" */ '../components/popup/house/houseList');
const houseDetail = () => import(/* webpackChunkName: "houseDetail" */ '../components/popup/house/detailHouse');

import house from '../components/process/index';
import releaseFood from '../components/process/food/'
import releaseStory from '../components/process/story/'

Vue.use(Router);

export default new Router({
  routes: [
    {
      path: '',
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
      component: Release,
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
    {
      path: '/pop',
      component: Pop,
      children: [
        {path: '', redirect: 'type'},
        {path: 'type', meta: {name: 'type', keepAlive: false}, name: 'popType', component: house.type},
        {path: 'newHouse', meta: {name: 'newHouse', keepAlive: true}, name: 'popNewHouse', component: house.newHouse},
        {path: 'confirmHouse', meta: {name: 'confirmHouse', keepAlive: true}, name: 'popConfirmHouse', component: house.confirmHouse},
        {path: 'styleHouse', meta: {name: 'styleHouse', keepAlive: true}, name: 'popStyleHouse', component: house.styleHouse},
        {path: 'descHouse', meta: {name: 'descHouse', keepAlive: true}, name: 'popDescHouse', component: house.descHouse},
        {path: 'ruleHouse', meta: {name: 'ruleHouse', keepAlive: true}, name: 'popRuleHouse', component: house.ruleHouse},
        {path: 'facilityHouse', meta: {name: 'facilityHouse', keepAlive: true}, name: 'popFacilityHouse', component: house.facilityHouse},
        {path: 'rimHouse', meta: {name: 'rimHouse', keepAlive: true}, name: 'popRimHouse', component: house.rimHouse},
        {path: 'priceHouse', meta: {name: 'priceHouse', keepAlive: true}, name: 'popPriceHouse', component: house.priceHouse},
        {path: 'releaseFood', meta: {name: 'releaseFood', keepAlive: true}, name: 'popReleaseFood', component: releaseFood},
        {path: 'releaseStory', meta: {name: 'releaseStory', keepAlive: true}, name: 'popReleaseStory', component: releaseStory},
      ]
    },
    {
      path: '/PopSearch',
      component: PopSearch,
      children: [
        {path: '', redirect: 'normalSearch'},
        {path: 'normalSearch', component: normalSearch},
        {path: 'resultSearch', component: resultSearch},
      ]
    },
    {
      path: '/PopHouse',
      component: popHouse,
      children: [
        {path: '', redirect: 'houseList'},
        {path: 'houseList', name: 'houseList', component: houseList},
        {path: 'houseDetail', name: 'houseDetail', component: houseDetail},
      ]
    },
  ]
})
