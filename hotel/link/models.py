from django.db import models
from django.contrib.auth.models import User


class UserProfile(models.Model):
    # 对应用户
    user = models.OneToOneField(User, on_delete=models.PROTECT, related_name='user_profile')
    show_name = models.CharField(max_length=10,default='')



class HotelRoom(models.Model):
    '''
    房源信息
    '''
    # 对应用户
    user = models.ForeignKey(User, on_delete=models.PROTECT, related_name='user_hotel')
    # 房源名
    name = models.CharField(max_length=100, default='')
    # 房源标签（关键信息）'明亮;临海;电梯'
    tag = models.CharField(default='', max_length=100)
    # 价格
    price = models.FloatField(default=0)
    # 房源信息
    # {
    #   'base_facility':'空调;电视;',
    #   'special':'特别说明'
    # }
    hotel_info = models.TextField(default='{}')
    # 总评分
    total_score = models.FloatField(default=0)



class UserAppraise(models.Model):
    '''
    用户评价
    '''
    # 对应用户
    user = models.ForeignKey(User, on_delete=models.PROTECT, related_name='user_appraise')
    # 对应房源（HotelRoom）
    hotel = models.ForeignKey(HotelRoom, on_delete=models.PROTECT, related_name='hotel_appraise')
    # 评价
    appraise = models.TextField(default='')
    about_time = models.DateTimeField(auto_now_add=True)
    # 用户评分
    user_score = models.FloatField(default=0)


class AroundRegion(models.Model):
    '''
    房源周边
    '''
    CATE = 1
    SCENERY = 2
    AROUND_TYPE = (
        (CATE, '美食'),
        (SCENERY,'风景'),
    )

    # 对应房源（HotelRoom）
    hotel = models.ForeignKey(HotelRoom, on_delete=models.PROTECT, related_name='hotel_around')
    around_type = models.SmallIntegerField(choices=AROUND_TYPE,default=CATE)
    # 详情、说明
    detail = models.TextField(default='{}')


class UsedImage(models.Model):
    '''
    图片（user与hotel只同时存在一个）
    '''
    t_user = 'User'
    t_hotelroom = 'HotelRoom'
    t_aroundregion = 'AroundRegion'
    BELONG_CLASS_TYPE = (
        (t_user,'用户图片'),
        (t_hotelroom, '房源图片'),
        (t_aroundregion, '周边图片'),
    )

    # 类型 属于那个class
    belong_class = models.CharField(choices=BELONG_CLASS_TYPE,max_length=20)
    # 对应类型对象的id
    belong_id = models.IntegerField()
    # image
    image = models.ImageField(upload_to='image')
    # 优先级  0,1,2...  小在先
    priority = models.SmallIntegerField(default=0)




class RoomTag(models.Model):
    TAG_CHOICES = (
        (1, '明亮'),
        (2, '临海'),
    )
    hotel = models.ForeignKey(HotelRoom, on_delete=models.PROTECT, related_name='hotel_tags')
    tag = models.SmallIntegerField(choices=TAG_CHOICES)
