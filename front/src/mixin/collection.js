import DeleteCollection from '../components/base/deleteCollection'

export default {
  components: {
    DeleteCollection
  },
  data() {
    return {
      isShow: false,
      belong_id: []
    }
  },
  methods: {
    handleOk() {
      this.isShow = false;
      this.$parent.handleTap()
    },
    handleDelete() {
      this.isShow = true
    }
  },
}
