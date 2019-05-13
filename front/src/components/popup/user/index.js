const userInformation = () => import(/* webpackChunkName: "userInformation" */ './userInformation');
const editInformation = () => import(/* webpackChunkName: "editInformation" */ './editInformation');
const feedBack = () => import(/* webpackChunkName: "feedBack" */ './feedBack');
const orderDetail = () => import(/* webpackChunkName: "orderDetail" */ './orderDetail');
const orderList = () => import(/* webpackChunkName: "orderList" */ './orderList');
const pay = () => import(/* webpackChunkName: "pay" */ './pay');
const setting = () => import(/* webpackChunkName: "userInformation" */ './setting');

export default {
  userInformation,
  editInformation,
  feedBack,
  orderDetail,
  orderList,
  setting,
  pay,
}