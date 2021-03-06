import axios from 'axios'
import cookie from "./cookie";

const qs = require('qs');
export default {
  async get (url, data) {
    try {
      let res = await axios.get(url, {params: data});
      res = res.data;
      if (res.e === "'AnonymousUser' object is not iterable") {
        cookie.remove('hotel_');
        this.$router.push({name: 'login'});
      }
      return new Promise((resolve, reject) => {
        if (res.r === 0 || res.result === 0) {
          resolve(res)
        } else {
          this.$msg({
            type: 'error',
            message: res.e
          });
          reject(res)
        }
      })
    } catch (err) {
      this.$msg({
        type: 'error',
        message: `服务器错误，请刷新页面`
      });
    }
  },
  async post (url, data, config = {}) {
    try {
      config['X-CSRFToken'] = cookie.get('csrftoken') || 'mock';
      let dataLast = {};
      for (let [key, value] of Object.entries(data)) {
        dataLast[key] = JSON.stringify(value)
      }
      // console.log(dataLast)
      let res = await axios.post(url, qs.stringify(dataLast), {headers: config});
      res = res.data;
      return new Promise((resolve, reject) => {
        if (res.r === 0) {
          resolve(res)
        } else {
          this.$msg({
            type: 'error',
            message: res.e
          });
          // reject(res)
        }
      })
    } catch (err) {
      // console.log(err)
    }
  },

  async postFile (url, data) {
    try {
      const headers = {headers: {'X-CSRFToken': cookie.get('csrftoken') || 'mock'}};
      let instance = axios.create({
        baseURL: '/',
        timeout: 4000,
        headers: {'Content-Type':'multipart/form-data'}
      });
      let res = await instance.post(url, data, headers);
      res = res.data;
      return new Promise((resolve, reject) => {
        if (res.r === 0) {
          resolve(res)
        } else {
          this.$msg({
            type: 'error',
            message: res.e
          });
          // reject(res)
        }
      })
    } catch (e) {

    }
  }
};
