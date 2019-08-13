"""hotel URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.contrib import admin
from link import views
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
                  url(r'^admin/', admin.site.urls),
                  url(r'^hotel/register/', views.register_user),
                  url(r'^hotel/login_in/', views.login_in),
                  url(r'^hotel/login_out/', views.login_out),
                  # 录入头像集
                  url(r'^hotel/head_portrait/$', views.entering_head_portrait),
                  # 录入房源信息
                  url(r'^hotel/hotel_room/$', views.entering_hotel_room_import),
                  # 录入周边信息
                  url(r'^hotel/around_region/$', views.entering_around_region_import),
                  # 录入故事信息
                  url(r'^hotel/story_board/$', views.entering_story_board_import),

                  # 录入用户评价
                  url(r'^hotel/user_appraise/$', views.entering_user_appraise_view),
                  # 录入订单
                  url(r'^hotel/order_form/$', views.submit_order_form_view),
                  # 录入收藏
                  url(r'^hotel/user_collect/$', views.submit_user_collect_view),  # 传入 belong_class  belong_id

                  # 得到头像集
                  url(r'^hotel/head_portrait/$', views.get_head_portrait),
                  # 得到周边信息
                  url(r'^hotel/get_around/$', views.get_around_region_view),  # 传入 user_id,不传就是自己
                  # 搜索房源及周边信息
                  url(r'^hotel/search_for_all/$', views.search_for_all_view),  # 传入key search
                  # 得到所有房源信息（或者个人所有的）
                  url(r'^hotel/get_hotel/$', views.get_hotel_room_view),  # 传入key: search  self='self/all' user_id
                  # 得到单个房源信息 + 周边
                  url(r'^hotel/get_one_hotel/$', views.get_one_hotel_room_view),  # 传入key: 房源 id
                  # 得到故事
                  url(r'^hotel/get_story/$', views.get_story_view),  # 传入 user_id，is_all，hotel_id
                  # 得到用户信息
                  url(r'^hotel/user_info/$', views.get_user_info_view),  # 可传参数 user_id
                  # 修改个性签名
                  url(r'^hotel/edit_user_info/$', views.edit_user_info_view),  # 参数 signature
                  # 判断用户是否以评价(当前用户)
                  url(r'^hotel/is_appraise/$', views.is_appraise_view),  # 参数 belong_class,belong_id
                  # 得到用户评价
                  url(r'^hotel/get_appraise/$', views.get_appraise_view),  # 参数 belong_class,belong_id
                  # 得到订单
                  url(r'^hotel/get_order_form/$', views.get_order_form_view),  # order_id

                  # 得到收藏
                  url(r'^hotel/get_user_collect/$', views.get_user_collect_view),
                  # 取消收藏
                  url(r'^hotel/del_collect/$', views.del_collect_obj_view),  # 参数 belong_class,belong_id

                  # 支付
                  url(r'^hotel/pay_order/$', views.pay_order_view),  # order_id,price

                  # chat
                  url(r'^hotel/chat/$', views.get_value_from_foreign),  # msg

                  # 测试接口
                  url(r'^get_user/', views.get_users),

              ] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
