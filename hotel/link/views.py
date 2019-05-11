import json
from django.http import HttpResponse
from link.RegisterAndLogin import Register, LoginAbout
from django.contrib.auth.models import User
from django.apps import apps

from link.hotel_info import entering_hotel_info, entering_story_board, entering_around_region, get_around_region, \
    save_files_for_hotel, save_around_for_hotel


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


def entering_hotel_room_import(request):
    '''
    录入房源信息
    :param request:
    :return:
    '''
    result = {'r': 0, 'e': 'ok'}
    user = request.user
    web_data = request.POST
    try:
        around_ids = json.loads(web_data.get('around', '[]'))
        files = web_data.get('file', '')
        data = {
            'user': user,
            'position': web_data.get('posHouse', ''),  # 地址, 重庆 - 鹅岭
            'hose_type': web_data.get('typeHouse', ''),  # 房源类型
            'room_type': web_data.get('roomHouse', ''),  # 房源房型
            'host_signer': web_data.get('signerHouse', '{}'),  # 房源户型
            'name': web_data.get('nameHouse', ''),  # 房源名字
            'host_desc': web_data.get('descHouse', ''),  # 房源描述
            'rim': web_data.get('rim', '[]'),  # 入住规则
            'facility': web_data.get('facitityHouse', '[]'),  # 房源设施
            'price': web_data.get('priceHouse', 0),  # 房源
        }
        hotel_room_id = entering_hotel_info(data)
        save_files_for_hotel(files, 'HotelRoom', hotel_room_id)
        save_around_for_hotel(hotel_room_id,around_ids)
    except Exception as e:
        result = {'r': 1, 'e': str(e)}
        print('entering_hotel_room_import:', e)

    return HttpResponse(json.dumps(result))


def entering_story_board_import(request):
    '''
    录入故事信息
    :param request:
    :return:
    '''
    web_data = request.POST
    data = {

    }
    result = entering_story_board(data)
    return HttpResponse(json.dumps(result))


def entering_around_region_import(request):
    '''
    录入周边信息
    :param request:
    :return:
    '''
    user = request.user
    web_data = request.POST
    print('entering_around_region_import:', web_data, type(web_data))
    around_file = request.FILES.get('files')
    print('around_file:', around_file, type(around_file))
    around_type = web_data['type']
    data = {
        'image': around_file,
        'around_type': around_type,
        'name': web_data['name'],
        'price': web_data['price'],
        'desc': web_data['desc'],
    }
    result = entering_around_region(user, data)
    return HttpResponse(json.dumps(result))


def get_around_region_view(request):
    result = {'r': 0, 'e': 'ok'}
    user = request.user
    try:
        result_info = get_around_region(user)
        result['data'] = result_info
    except Exception as e:
        print(e)
        result = {'r': 1, 'e': str(e)}

    return HttpResponse(json.dumps(result))


def get_users(request):
    users = User.objects.all()
    u_name = [u.username for u in users]
    a = apps.get_model('link', 'HotelRoom')

    print('aaaa', a)

    return HttpResponse(json.dumps(u_name))
