const path = require('path');
function resolve(dir) {
  return path.join(__dirname, '.', dir)
}
module.exports = {
  publicPath: './',
  outputDir: 'hotel',
  css: {
    loaderOptions: {
      postcss: {
        plugins: [
          require('postcss-pxtorem')({
            selectorBlackList  : ['weui','mu'], // 忽略转换正则匹配项
            propList   : ['*'],
          }),
        ]
      }
    }
  },
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
  chainWebpack: config => {
    config.module.rules.delete("svg");
    config.module
      .rule('svg-sprite-loader')
      .test(/\.svg$/)
      .include
      .add(resolve('src/static/svg')) //处理svg目录
      .end()
      .use('svg-sprite-loader')
      .loader('svg-sprite-loader')
      .options({
        symbolId: 'icon-[name]'
      })
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
