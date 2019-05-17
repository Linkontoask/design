<template>
  <div class="desc-house">
    <h3>房源描述</h3>
    <h5>概述</h5>
    <div>
      限名女（男）性，有正当职业，租住半年以上。
      无不良嗜好，作息健康，不经常带异性、朋友、
      同学回来过夜。性格平易近人，爱干净的女（男）
      生。房租为元／月（诚心租住的朋友，价格可以
      商谈），其他费用平摊（水电煤气电视费）。
    </div>
    <h5>注意事项</h5>
    <ul>
      <li>请勿穿鞋在地毯上走动（太难清洁）</li>
      <li>请爱护房间内的所有物品，如有损坏照价赔偿，一定 要注意哦</li>
    </ul>
  </div>
</template>

<script>
  export default {
    name: "descHouse",

  }
</script>

<style scoped lang="less">
.desc-house {
  padding: 84px 36px 0;
  h3 {
    color: #2E3130;
  }
  h5 {
    margin: 36px 0 24px 0;
  }
  div {
    font-size: 14px;
  }
  ul {
    padding-left: 20px;
    li {
      font-size: 14px;
      list-style-type: disc;
    }
    li + li {
      margin-top: 12px;
    }
  }
}
</style>
