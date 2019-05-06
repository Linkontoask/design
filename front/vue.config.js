const path = require('path');

module.exports = {
  devServer: {
    proxy: {
      '/hotel': {
        target: 'http://172.16.5.119',
        changeOrigin: true,
        pathRewrite: {
          '^/hotel': '/hotel'
        }
      },
    },
  },
  transpileDependencies: ['v-easy-message'],
  configureWebpack: {
    resolve: {
      alias: {
        'utils': path.resolve(__dirname, './src/utils'),
        'components': '@/components',
        'views': '@/views',
      }
    }
  },
}
