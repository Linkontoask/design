import json
from django.http import HttpResponse
from link.RegisterAndLogin import Register, LoginAbout
from django.contrib.auth.models import User
from django.apps import apps

from link.hotel_info import entering_hotel_info


def register_user(request):
    result = {'r': 0, 'e': '注册成功', 'data': ''}
    u_name = request.GET.get('username')
    u_pwd = request.GET.get('password')
    try:
        Register.reg_user(u_name, u_pwd)
    except Exception as e:
        result['r'] = 1
        result['e'] = str(e)

    return HttpResponse(json.dumps(result, ensure_ascii=False))


def login_in(request):
    result = {'r': 0, 'e': '登录成功', 'data': ''}
    u_name = request.GET.get('username')
    u_pwd = request.GET.get('password')

    try:
        LoginAbout.login_in(request, u_name, u_pwd)
    except Exception as e:
        result['r'] = 1
        result['e'] = str(e)

    return HttpResponse(json.dumps(result, ensure_ascii=False))

def entering_hotel_info_import(request):
    web_data = request.POST
    data = {

    }
    result = entering_hotel_info(data)
    return HttpResponse(json.dumps(result))



def get_users(request):
    users = User.objects.all()
    u_name = [u.username for u in users]
    a = apps.get_model('link', 'HotelRoom')

    print('aaaa', a)

    return HttpResponse(json.dumps(u_name))
