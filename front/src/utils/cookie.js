/**
 *
 * 封装基本的cookie
 *
 */

;
/**
 *
 * @param name 必传
 * @param value 必传
 * @param domain 可传，标准url。如果此时传入数字，那么默认为过期时间
 * @param expires 可传，值为ms
 * @param path 待设计
 */
const set = function (name, value, domain, expires, path) {
  if (typeof domain === 'number') {
    expires = domain;
    domain = undefined
  }
  const t = new Date();
  t.setTime(t.getTime() + expires);

  const mainDo = (domain ? ';domain=' + domain : '');
  document.cookie = name + '=' + value + mainDo + ';expires=' + t;
};

/**
 *
 * @param name cookie key
 * @returns string or null
 */
const get = function (name) {
  const cookie = document.cookie.split('; ');
  for (let i = 0; i < cookie.length; i++) {
    const cookieArr = cookie[i].split('=');
    if (cookieArr[0] === name) {
      return cookieArr[1];
    }
  }
  return null;
};

const remove = function (name) {
  set(name, '', -1)
};

const cookie = {
  get,
  set,
  remove
};

export default cookie
