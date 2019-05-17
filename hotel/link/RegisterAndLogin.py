from django.contrib.auth.models import User
from django.contrib import auth

from link.models import UserProfile, UsedImage


class Register(object):
    '''
    注册相关
    '''

    @staticmethod
    def reg_user(username, pwd, avatar):
        user = User.objects.filter(username=username).first()
        if not user:
            user = User.objects.create(username=username, password=pwd)
            portrait_obj = UsedImage.objects.filter(belong_class='UserProfile').first()
            UserProfile.objects.create(user=user, portrait=portrait_obj, avatar=avatar)
        else:
            raise Exception('账号已存在')


class LoginAbout(object):
    '''
    登录退出相关
    '''

    @staticmethod
    def login_in(request, username, pwd):
        user = User.objects.filter(username=username, password=pwd).first()
        if user:
            auth.login(request, user)
            return user.id
        else:
            raise Exception('账号或密码错误')

    @staticmethod
    def login_out(request):
        try:
            auth.logout(request)
        except Exception as e:
            raise Exception(str(e))
