const path = require('path');

module.exports = {
  publicPath: './',
  outputDir: 'hotel',
  devServer: {
    proxy: {
      '/hotel': {
        target: 'http://172.16.6.160:9999',
        changeOrigin: true,
        pathRewrite: {
          '^/hotel': '/hotel'
        }
      },
    },
    host: "0.0.0.0"
  },
  transpileDependencies: ['v-easy-message'],
  configureWebpack: {
    resolve: {
      alias: {
        'utils': path.resolve(__dirname, './src/utils'),
        'components': '@/components',
        'views': '@/views',
      }
    },
    optimization: {
      splitChunks: {
        minSize: 10000,
        maxSize: 250000,
      }
    },

    performance: {
      maxEntrypointSize: 512000,
      maxAssetSize: 512000
    },
  },
};
