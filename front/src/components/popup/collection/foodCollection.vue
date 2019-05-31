<template>
	<transition name="collection">
		<div class="food-collection">
			<div class="more">
        <div @click="isShow = true">
          <span></span>
          <span></span>
          <span></span>
        </div>
			</div>
			<h1>收藏的美食</h1>
			<Food :data="food"></Food>
			<DeleteCollection :vis="isShow" @status="handleOk" @show="value => isShow = value" belong_class="AroundRegion" :belong_id="belong_id"></DeleteCollection>
		</div>
	</transition>
</template>

<script>
	import Food from '../../base/food'
  import Storage from '../../../utils/localStorage'
  import DeleteCollection from '../../base/deleteCollection'
	export default {
		name: 'houseCollection',
		components: {
      Food,
      DeleteCollection
		},
		data() {
			return {
        food: [],
        isShow: false,
        belong_id: []
			}
		},
		methods: {
      handleOk() {
        this.isShow = false;
        this.$parent.handleTap()
			}
		},
		beforeMount() {

		},
		activated() {
			let data = Storage.get('noe_check_collection');
			data.forEach(item => {
			  this.belong_id.push(item.belong_id)
			})
      data.forEach(item => {
        this.food.push(item.belong_info[0])
			})
		}
	}
</script>

<style scoped lang="less">
	.food-collection {
		height: calc(100vh - 110px);
		padding: 0 36px 36px;
		margin-top: 74px;
		overflow-y: auto;
		h1 {
			margin-top: 24px;
			margin-bottom: 36px;
			font-size: 20px;
			color: #2E312F;
		}
		.more {
			position: fixed;
			left: 0;
			top: 0;
			width: 100%;
			height: 74px;
			border-bottom: 1px solid #DCDFE6;
			span {
				display: inline-block;
				float: right;
				width: 6px;
				height: 6px;
				background-color: #2E3130;
				border-radius: 50%;
				margin-top: 34px;
				&:first-child {
					margin-right: 36px;
				}
				& + span {
					margin-right: 4px;
				}
			}
		}
	}
</style>
