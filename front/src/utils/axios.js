import axios from 'axios'
import cookie from "./cookie";
const qs = require('qs');
export default {
  async get (url, data) {
    try {
      let res = await axios.get(url, {params: data});
      res = res.data;
      return new Promise((resolve) => {
        if (res.code === 0) {
          resolve(res)
        } else {
          resolve(res)
        }
      })
    } catch (err) {
      console.log(err)
    }
  },
  async post (url, data, config = {}) {
    try {
      config['x-csrf-token'] = cookie.get('csrftoken') || 'mock';
      let res = await axios.post(url, qs.stringify(data), {});
      res = res.data;
      return new Promise((resolve, reject) => {
        if (res.code === 0) {
          resolve(res)
        } else {
          reject(res)
        }
      })
    } catch (err) {
      console.log(err)
    }
  },
};
