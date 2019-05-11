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

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^hotel/register/', views.register_user),
    url(r'^hotel/login_in/',views.login_in),
    # 录入房源信息
    url(r'^hotel/hotel_room/$',views.entering_hotel_room_import),
    # 录入周边信息
    url(r'^hotel/around_region/$',views.entering_around_region_import),
    # 录入故事信息
    url(r'^hotel/story_board/$',views.entering_story_board_import),

    # 得到周边信息
    url(r'^hotel/get_around/$',views.get_around_region_view),



    # 测试接口
    url(r'^get_user/',views.get_users),

]
