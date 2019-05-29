<template xmlns:v-hammer="http://www.w3.org/1999/xhtml">
  <div class="stay-house">
    <ul ref="houseBox">
      <li v-for="(item, index) in data" :key="index" v-hammer:tap="elm => handleView(elm, item, index)">
        <div class="img-content" :style="{backgroundImage: `url(${item.imgs[0]})`}"></div>
        <div class="house-content">
          <p class="content-1">
            <span class="medium clamp2">{{ item.name }}</span>
          </p>
          <div class="content-2 clamp1">{{ item.host_desc ? item.host_desc : '没有此房源的描述信息' }}</div>
          <div class="content-3">
            <strong>{{ item.price }}</strong>
            <p>{{ item.price + Math.floor(Math.random() * 100 + 20) }}</p>
            <span>{{ item.position.slice(0, 2) }}</span>
          </div>
        </div>
      </li>
    </ul>
  </div>
</template>

<script>
  import Storage from '../../utils/localStorage'

  export default {
    name: 'stayHouse',
    data() {
      return {
      }
    },
    props: {
      data: {
        type: Array,
        default: () => []
      }
    },
    methods: {
      handleView(elm, obj, index) {
        Storage.set('now_checked_house', this.data[index]);
        const box = document.createElement('div');
        const node = document.createElement('div');
        const rect = this.$refs.houseBox.childNodes[index].childNodes[0].getBoundingClientRect()
        node.setAttribute('style', `background-image: url(${this.data[index].imgs[0]})`);
        box.setAttribute('class', 'animation-form');
        box.setAttribute('data-id', new Date().getTime());
        box.setAttribute('style', `left: ${rect.left}px;top: ${rect.top}px;width: ${rect.width}px; height: ${rect.height}px`);
        box.appendChild(node);
        document.body.appendChild(box);
        setTimeout(() => {
          document.body.removeChild(box);
        }, 600)
        this.$router.push({
          path: '/PopHouse/houseDetail',
          query: {
            bgColor: '#fff',
            control: 'close',
            id: this.data[index].hotel_id
          }
        })
      }
    }
  }
</script>

<style lang="less" scoped>
  .stay-house {
    ul {
      display: flex;
      justify-content: space-between;
      flex-wrap: wrap;
      li {
        width: 48%;
        height: 224px;
        margin-top: 12px;
        box-shadow: 0 1px 2px #cbdad8;
        > img {
          width: 100%;
        }
        img.start {
          position: absolute;
        }
        .img-content {
          height: 120px;
          background-repeat: no-repeat;
          background-position: center;
          background-size: cover;
          border-top-left-radius: 4px;
          border-top-right-radius: 4px;
        }
        .house-content {
          font-size: 14px;
          margin-top: 12px;
          padding: 0 4px 4px;
          .content-1 {
            height: 38px;
          }
          .content-3 {
            span:last-child {
              color: #8F9895;
              font-size: 12px;
              flex-shrink: 0;
              margin-left: auto;
            }
          }
          .content-2 {
            font-size: 12px;
            margin-top: 4px;
            line-height: 1.6;
          }
          .content-3 {
            display: flex;
            justify-content: flex-start;
            align-items: center;
            margin-top: 8px;
            color: #EB0C0C;
            p {
              margin-left: 20px;
              color: #5F6564;
              font-size: 10px;
              text-decoration: line-through;
            }
          }
        }
      }
    }

  }
</style>
