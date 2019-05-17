<template>
	<transition name="collection">
		<div class="house-collection">
			<div class="more">
				<span></span>
				<span></span>
				<span></span>
			</div>
			<h1>地点-{{ house.position }}</h1>
			<houseListBase :houseList="houseList"></houseListBase>
		</div>
	</transition>
</template>

<script>
	import houseListBase from '../../base/houseListBase'
	export default {
		name: 'houseCollection',
		components: {
      houseListBase
		},
		data() {
			return {
        houseList: [],
				house: {
          position: '成都市',
				}
			}
		},
		methods: {

		},
		beforeMount() {

		},
		activated() {

		}
	}
</script>

<style scoped lang="less">
	.house-collection {
		padding: 0 36px;
		h1 {
			font-size: 20px;
			margin-top: 96px;
			padding-bottom: 24px;
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