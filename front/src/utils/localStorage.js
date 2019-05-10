export default {
  set: (name, value) => {
    window.localStorage.setItem(name, JSON.stringify(value));
  },

  get: (name) => {
    const value = window.localStorage.getItem(name);
    return value ? JSON.parse(value) : null
  }
}
