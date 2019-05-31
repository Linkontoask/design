<template>
	<transition name="collection">
		<div class="story-collection">
			<div class="more">
        <div @click="handleDelete">
          <span></span>
          <span></span>
          <span></span>
        </div>
			</div>
			<h1>收藏的故事</h1>
			<Story :data="story"></Story>
			<DeleteCollection :vis="isShow" @status="handleOk" @show="value => isShow = value" belong_class="StoryBoard" :belong_id="belong_id"></DeleteCollection>
		</div>
	</transition>
</template>

<script>
	import Story from '../../base/story'
  import Storage from '../../../utils/localStorage'
  import mixin from '../../../mixin/collection'
	export default {
		name: 'houseCollection',
		components: {
      Story,
		},
    mixins: [mixin],
		data() {
			return {
				story: [],
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
        this.story.push(item.belong_info[0])
      })
		}
	}
</script>

<style scoped lang="less">
	.story-collection {
		height: calc(100vh - 110px);
		padding: 0 36px 36px;
		margin-top: 74px;
		overflow-y: auto;
		h1 {
			margin-top: 24px;
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
