from django.db import models
from django.contrib.auth.models import User


class UsedImage(models.Model):
    '''
    图片（user与hotel只同时存在一个）
    '''
    t_user = 'UserProfile'
    t_hotelroom = 'HotelRoom'
    t_aroundregion = 'AroundRegion'
    t_storyboard = 'StoryBoard'
    BELONG_CLASS_TYPE = (
        (t_user, '用户图片'),
        (t_hotelroom, '房源图片'),
        (t_aroundregion, '周边图片'),
        (t_storyboard, '故事图片'),
    )

    # 类型 属于那个class
    belong_class = models.CharField(choices=BELONG_CLASS_TYPE, max_length=20)
    # 对应类型对象的id
    belong_id = models.IntegerField(null=True, default=None)
    # image
    image = models.ImageField(upload_to='image')
    # 优先级  0,1,2...  小在先
    priority = models.SmallIntegerField(default=0)


class UserProfile(models.Model):
    # 对应用户
    user = models.OneToOneField(User, on_delete=models.PROTECT, related_name='user_profile')
    show_name = models.CharField(max_length=10, default='')
    # 用户财产
    property = models.FloatField(default=1000)
    # 用户积分
    score = models.IntegerField(default=0)
    # 注册时间
    register_time = models.DateTimeField(auto_now_add=True)
    # 头像
    portrait = models.ForeignKey(UsedImage, on_delete=models.SET_NULL, null=True, default=None)
    # 头像只有文件名
    avatar = models.CharField(max_length=20, default='')


class HotelRoom(models.Model):
    '''
    房源信息
    '''

    TAGS = ['性价比高', '近地铁', '有洗衣机', '有空调', '可以做饭', '免费停车', '自助入住', '可存行李', '有烘干机']
    SCORE_RULE = {''}

    # 对应用户
    user = models.ForeignKey(User, on_delete=models.PROTECT, related_name='user_hotel')
    # 房源名
    name = models.CharField(max_length=100, default='')
    # 地址 , 重庆-鹅岭
    position = models.TextField(default='')
    # 房源类型
    hose_type = models.CharField(max_length=20, default='')
    # 房源房型
    room_type = models.CharField(max_length=20, default='')
    # 房源户型
    host_signer = models.TextField(default='{}')
    # 房源描述
    host_desc = models.TextField(default='')
    # 入住规则
    rim = models.CharField(max_length=20, default='[]')
    # 房源设施
    facility = models.TextField(default='{}')
    # 房源标签（关键信息）'明亮|临海|电梯'
    tag = models.CharField(default='', max_length=100)
    # 价格
    price = models.FloatField(default=0)
    # 房源信息
    # {
    #   'base_facility':'空调;电视;',
    #   'special':'特别说明'
    # }
    hotel_info = models.TextField(default='{}')
    # 评价总人数
    score_num = models.IntegerField(default=0)
    # 总评分
    total_score = models.SmallIntegerField(default=0)
    # 说明
    score_info = models.TextField(default='[]')


class UserAppraise(models.Model):
    '''
    用户评价
    '''
    a_user = 'UserProfile'
    a_hotelroom = 'HotelRoom'
    a_aroundregion = 'AroundRegion'
    a_storyboard = 'StoryBoard'
    BELONG_CLASS_TYPE = (
        (a_user, '对用户的评价'),
        (a_hotelroom, '对房源的评价'),
        (a_aroundregion, '对周边的评价'),
        (a_storyboard, '对故事的评价'),
    )
    # 评价的用户
    user = models.ForeignKey(User, on_delete=models.PROTECT, related_name='user_appraise')
    # 类型 属于那个class
    belong_class = models.CharField(choices=BELONG_CLASS_TYPE, max_length=20)
    # 对应类型对象的id
    belong_id = models.IntegerField(null=True, default=None)
    # 评价
    appraise = models.TextField(default='')
    # 评价时间
    about_time = models.DateTimeField(auto_now_add=True)
    # 评价详情
    detail = models.TextField(default='{}')

    # # 对应用户
    # user = models.ForeignKey(User, on_delete=models.PROTECT, related_name='user_appraise')
    # # 对应房源（HotelRoom）
    # hotel = models.ForeignKey(HotelRoom, on_delete=models.PROTECT, related_name='hotel_appraise')
    # # 评价
    # appraise = models.TextField(default='')
    # about_time = models.DateTimeField(auto_now_add=True)


class UserFavorite(models.Model):
    '''
    用户收藏
    '''
    # 对应用户
    user = models.ForeignKey(User, on_delete=models.PROTECT, related_name='user_favorite')
    # 收藏对象的 class 类
    favorite_class = models.CharField(max_length=20)
    # 对应对象的 id
    favorite_id = models.IntegerField()


class AroundRegion(models.Model):
    '''
    房源周边
    '''
    CATE = 1
    SCENERY = 2
    AROUND_TYPE = (
        (CATE, '美食'),
        (SCENERY, '风景'),
    )
    # 对应用户
    user = models.ForeignKey(User, on_delete=models.PROTECT, related_name='user_around')
    # 对应房源（HotelRoom）
    hotel = models.ForeignKey(HotelRoom, on_delete=models.PROTECT, related_name='hotel_around', null=True, default=None)
    # 名称
    name = models.CharField(max_length=100, default='')
    # 价格
    price = models.FloatField(default=0)
    around_type = models.SmallIntegerField(choices=AROUND_TYPE, default=CATE)
    # 详情、说明
    detail = models.TextField(default='')


class StoryBoard(models.Model):
    '''
    故事
    '''
    # 对应用户(发布者)
    user = models.ForeignKey(User, on_delete=models.PROTECT, related_name='user_story')
    # 对应房源
    hotel = models.ForeignKey(HotelRoom, on_delete=models.PROTECT, related_name='hotel_story', null=True, default=None)
    # 主题
    theme = models.CharField(max_length=200, default='')
    # 内容
    content = models.TextField(default='')
    # 评价总人数
    score_num = models.IntegerField(default=0)
    # 总评分
    total_score = models.SmallIntegerField(default=0)
    # 说明
    score_info = models.TextField(default='[]')


class OrderForm(models.Model):
    '''订单'''
    # 订单创建人
    create = models.ForeignKey(User, null=True, on_delete=models.SET_NULL, related_name='user_order')
    # 对应的房源
    hotel = models.ForeignKey(HotelRoom, null=True, on_delete=models.SET_NULL, related_name='hotel_order')
    # 创建时间
    order_time = models.TimeField(auto_now_add=True)
    # 状态 1 侍支付  2.支付成功
    order_status = models.SmallIntegerField(default=1)
    # 详情
    detail = models.TextField(default='{}')


class RoomTag(models.Model):
    TAG_CHOICES = (
        (1, '明亮'),
        (2, '临海'),
    )
    hotel = models.ForeignKey(HotelRoom, on_delete=models.PROTECT, related_name='hotel_tags')
    tag = models.SmallIntegerField(choices=TAG_CHOICES)
