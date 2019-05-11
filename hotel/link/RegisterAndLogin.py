from django.contrib.auth.models import User
from django.contrib import auth

class Register(object):
    '''
    注册相关
    '''
    @staticmethod
    def reg_user(username,pwd):
        user = User.objects.filter(username=username).first()
        if not user:
            User.objects.create(username=username,password=pwd)
        else:
            raise Exception('账号已存在')




class LoginAbout(object):
    '''
    登录退出相关
    '''

    @staticmethod
    def login_in(request,username,pwd):
        user = User.objects.filter(username=username,password=pwd).first()
        if user:
            auth.login(request,user)
        else:
            raise Exception('账号或密码错误')
