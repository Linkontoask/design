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

import house from '../components/process/index';

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
      ]
    },
  ]
})
