const path = require('path');

module.exports = {
  publicPath: './',
  outputDir: 'hotel',
  devServer: {
    proxy: {
      '/hotel': {
        target: 'http://112.74.169.178',
        changeOrigin: true,
        pathRewrite: {
          '^/hotel': '/hotel'
        }
      },
      '/media': {
        target: 'http://112.74.169.178',
        changeOrigin: true,
        pathRewrite: {
          '^/media': '/media'
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
