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
const houseDesc = () => import(/* webpackChunkName: "houseDesc" */ '../components/popup/house/descHouse');
const houseFacility = () => import(/* webpackChunkName: "houseFacility" */ '../components/popup/house/houseFacility');
const evaluation = () => import(/* webpackChunkName: "evaluation" */ '../components/popup/house/evaluationAll');
const newTenant = () => import(/* webpackChunkName: "newTenant" */ '../components/popup/house/newTenant');
const addTenant = () => import(/* webpackChunkName: "addTenant" */ '../components/popup/house/addTenant');
const landlord = () => import(/* webpackChunkName: "landlord" */ '../components/popup/house/landlord');
const houseBook = () => import(/* webpackChunkName: "houseBook" */ '../components/popup/house/bookHouse');
const lastBook = () => import(/* webpackChunkName: "lastBook" */ '../components/popup/house/lastBook');
const firstBook = () => import(/* webpackChunkName: "firstBook" */ '../components/popup/house/bookFrist');

const Success = () => import(/* webpackChunkName: "success" */ '../components/popup/house/success');
const Chat = () => import(/* webpackChunkName: "Chat" */ '../components/base/chat');


const FoodDetail = () => import(/* webpackChunkName: "FoodDetail" */ '../components/food/foodDetail');
const StoryDetail = () => import(/* webpackChunkName: "StoryDetail" */ '../components/story/storyDetail');


import house from '../components/process/index';
import user from '../components/popup/user/index';
import releaseFood from '../components/process/food/';
import releaseStory from '../components/process/story/';
import releaseEvaluation from '../components/evaluation/';
import collection from '../components/popup/collection/'

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
      path: '/success',
      name: 'success',
      component: Success
    },
    {
      path: '/chat',
      name: 'chat',
      component: Chat
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
        {path: 'normalSearch', name: 'normalSearch', component: normalSearch},
        {path: 'resultSearch', name: 'resultSearch', component: resultSearch},
      ]
    },
    {
      path: '/PopHouse',
      component: popHouse,
      children: [
        {path: '', redirect: 'houseList'},
        {path: 'houseList', name: 'houseList', component: houseList},
        {path: 'houseDetail', name: 'houseDetail', component: houseDetail},
        {path: 'houseDesc', name: 'houseDesc', component: houseDesc},
        {path: 'houseFacility', name: 'houseFacility', component: houseFacility},
        {path: 'evaluation', name: 'evaluation', component: evaluation},
        {path: 'newTenant', name: 'newTenant', component: newTenant},
        {path: 'addTenant', name: 'addTenant', component: addTenant},
        {path: 'landlord', name: 'landlord', component: landlord},
        {path: 'userInformation', name: 'userInformation', component: user.userInformation},
        {path: 'userEditInformation', name: 'userEditInformation', component: user.editInformation},
        {path: 'userFeedBack', name: 'userFeedBack', component: user.feedBack},
        {path: 'userOrderDetail', name: 'userOrderDetail', component: user.orderDetail},
        {path: 'userOrderList', name: 'userOrderList', component: user.orderList},
        {path: 'userPay', name: 'userPay', component: user.pay},
        {path: 'userSetting', name: 'userSetting', component: user.setting},
        {path: 'houseEvaluation', name: 'houseEvaluation', component: releaseEvaluation.houseEvaluation},
        {path: 'storyWriteEvaluation', name: 'storyWriteEvaluation', component: releaseEvaluation.storyEvaluation},
        {path: 'FoodDetail', name: 'FoodDetail', component: FoodDetail},
        {path: 'StoryDetail', name: 'StoryDetail', component: StoryDetail},
        {path: 'FoodCollection', name: 'FoodCollection', component: collection.FoodCollection},
        {path: 'HouseCollection', name: 'HouseCollection', component: collection.HouseCollection},
        {path: 'StoryCollection', name: 'StoryCollection', component: collection.StoryCollection},
        {path: 'houseBook', component: houseBook,
          children: [
            {path: '', redirect: 'firstBook'},
            {path: 'lastBook', name: 'lastBook', component: lastBook},
            {path: 'firstBook', name: 'firstBook', component: firstBook},
          ]},
      ]
    },
  ],
  scrollBehavior (to, from, savedPosition) {
    if (savedPosition) {
      return savedPosition
    } else {
      return { x: 0, y: 0 }
    }
  },
})
