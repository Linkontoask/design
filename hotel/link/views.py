import json
from django.http import HttpResponse
from link.RegisterAndLogin import Register, LoginAbout
from django.contrib.auth.models import User
from django.apps import apps

from link.hotel_info import entering_hotel_info, entering_story_board, entering_around_region, get_around_region, \
    save_files_for_class, save_around_for_hotel, get_hotel_room_info, get_around_info, get_all_portrait, \
    get_one_hotel_and_around, get_user_info, entering_user_appraise, get_appraise_of_object, \
    submit_order_form, get_order_form, pay_order, user_collect, get_user_collect, get_story_info, is_appraise, \
    del_collect_obj, edit_user_info

from django.core.files.uploadedfile import InMemoryUploadedFile

from link.models import OrderForm


def entering_head_portrait(request):
    result = {'r': 0, 'e': 'ok'}
    files = request.FILES.getlist('files')
    try:
        save_files_for_class(files, 'UserProfile', None)
    except Exception as e:
        result = {'r': 0, 'e': str(e)}
    return HttpResponse(json.dumps(result))


def register_user(request):
    result = {'r': 0, 'e': '注册成功', 'data': ''}
    u_name = request.GET.get('username')
    u_pwd = request.GET.get('password')
    avatar = request.GET.get('avatar', '')
    Register.reg_user(u_name, u_pwd, avatar)

    return HttpResponse(json.dumps(result, ensure_ascii=False))


def login_in(request):
    result = {'r': 0, 'e': '登录成功', 'data': ''}
    u_name = request.GET.get('username')
    u_pwd = request.GET.get('password')

    try:
        user_id = LoginAbout.login_in(request, u_name, u_pwd)
        result['user_id'] = user_id
    except Exception as e:
        result['r'] = 1
        result['e'] = str(e)

    return HttpResponse(json.dumps(result, ensure_ascii=False))


def login_out(request):
    result = {'r': 0, 'e': '成功退出', 'data': ''}
    try:
        LoginAbout.login_out(request)
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
    web_data = json.loads(request.POST.get('other'))
    try:
        around_ids = web_data.get('around', [])
        files = request.FILES.getlist('files')
        data = {
            'user': user,
            'position': web_data.get('posHouse', ''),  # 地址, 重庆 - 鹅岭
            'hose_type': web_data.get('typeHouse', ''),  # 房源类型
            'room_type': web_data.get('roomHouse', ''),  # 房源房型
            'host_signer': json.dumps(web_data.get('signerHouse', {})),  # 房源户型
            'name': web_data.get('nameHouse', ''),  # 房源名字
            'host_desc': web_data.get('descHouse', ''),  # 房源描述
            'rim': json.dumps(web_data.get('rule', [])),  # 入住规则
            'facility': json.dumps(web_data.get('facitityHouse', [])),  # 房源设施
            'price': float(web_data.get('priceHouse', 0)),  # 房源
        }
        hotel_room_id = entering_hotel_info(data)
        save_files_for_class(files, 'HotelRoom', hotel_room_id)
        save_around_for_hotel(hotel_room_id, around_ids)
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
    user = request.user
    web_data = request.POST
    files = request.FILES.getlist('files')
    hotel_id = web_data.get('hotel_id', None)
    content = web_data.get('content', '')
    name = web_data.get('name', '')

    data = {
        'user': user,
        'content': content,
        'theme': name,
    }
    if hotel_id:
        data['hotel__id'] = hotel_id

    print('entering_story_board_import:', data)
    result = entering_story_board(data, files)
    return HttpResponse(json.dumps(result))


def entering_around_region_import(request):
    '''
    录入周边信息
    :param request:
    :return:
    '''
    user = request.user
    web_data = request.POST
    around_files = request.FILES.getlist('files')
    # 对于单个文件接收 文件名字
    # around_files = request.FILES.get('files')
    around_type = web_data['type']
    data = {
        'image': around_files,
        'around_type': around_type,
        'name': web_data['name'],
        'price': web_data['price'],
        'desc': web_data.get('desc', ''),
    }
    result = entering_around_region(user, data)
    return HttpResponse(json.dumps(result))


def entering_user_appraise_view(request):
    result = {'r': 0, 'e': '评价成功'}
    # 图片
    files = request.FILES.getlist('files', None)
    # 方法里有回传这两个key  现在带回来
    belong_class = request.POST.get('obj_class')
    belong_id = request.POST.get('belong_id')
    # 非特殊要求，这个user_id  可以不传
    user_id = request.POST.get('user_id') if request.POST.get('user_id') else request.user.id
    appraise = request.POST.get('content', '')
    # 平均分
    avg_score = request.POST.get('avg_score', 0)
    # 评价的细则，可以没有
    score_info = request.POST.get('score_info', '0,0,0,0')
    # 订单号
    order_id = int(request.POST.get('order_id', 0))

    data = {
        'belong_class': belong_class,
        'belong_id': int(belong_id),
        'user_id': int(user_id),
        'appraise': appraise,
        'detail': score_info,
    }
    entering_user_appraise(data, files, avg_score, score_info, order_id)


    return HttpResponse(json.dumps(result))


def is_appraise_view(request):
    user = request.user
    belong_class = request.POST.get('obj_class')
    belong_id = request.POST.get('belong_id')
    re = is_appraise(user.id, belong_class, belong_id)
    if re:
        result = {'r': 0, 'e': 'ok', 'data': re}
    else:
        result = {'r': 1, 'e': '请求失败', 'data': re}

    return HttpResponse(json.dumps(result))


def get_appraise_view(request):
    result = {'r': 0, 'e': 'ok'}
    # 方法里有回传这两个key  现在带回来
    belong_class = request.GET.get('belong_class')
    belong_id = request.GET.get('belong_id')
    res = get_appraise_of_object(belong_class, belong_id)
    result['data'] = res

    return HttpResponse(json.dumps(result))


def get_around_region_view(request):
    '''
    得到周边信息
    :param request:
    :return:
    '''
    result = {'r': 0, 'e': 'ok'}
    user = request.user
    user_id = request.GET.get('user_id', None)
    is_all = request.GET.get('is_all', None)
    result_info = get_around_region(user=user, user_id=user_id, is_all=is_all,belong_user_id=user.id)
    result['data'] = result_info

    return HttpResponse(json.dumps(result))


def get_hotel_room_view(request):
    '''
    得到房源信息
    :param request:
    :return:
    '''
    result = {'r': 0, 'e': 'ok'}
    user_id = None
    search = request.GET.get('search', None)
    seek_id = request.GET.get('user_id', 0)  # 权重 高
    is_all = request.GET.get('is_all', 'yes') == 'yes'  # 不传则 为所有的  权重 低
    if not is_all:
        user_id = request.user.id
    if seek_id:
        user_id = seek_id

    result_hotels = get_hotel_room_info(user_id=user_id, search=search,belong_user_id=request.user.id)
    result['data'] = result_hotels
    return HttpResponse(json.dumps(result))


def get_one_hotel_room_view(request):
    result = {'r': 0, 'e': 'ok'}
    hotel_id = int(request.GET.get('hotel_id', '0'))
    user = request.user
    re = get_one_hotel_and_around(hotel_id, user.id)
    result['data'] = re
    return HttpResponse(json.dumps(result))


def get_user_info_view(request):
    result = {'r': 0, 'e': 'ok'}
    user = request.user
    user_id = request.GET['user_id'] if request.GET.get('user_id', None) else user.id
    try:
        u_info = get_user_info(user_id)
        result['data'] = u_info
    except Exception as e:
        result = {'r': 1, 'e': str(e)}

    return HttpResponse(json.dumps(result, ensure_ascii=False))


def search_for_all_view(request):
    re = {'r': 0, 'e': 'ok'}
    search = request.GET.get('search', None)
    try:
        hotel_list = get_hotel_room_info(search=search)
        around_list = get_around_info(search=search)
        re['data'] = {'hotel_list': hotel_list, 'around_list': around_list}
    except Exception as e:
        re = {'r': 1, 'e': str(e)}

    return HttpResponse(json.dumps(re, ensure_ascii=False))


def get_head_portrait(request):
    result = get_all_portrait()
    return HttpResponse(json.dumps({'r': 0, 'e': 'ok', 'data': result}))


def get_story_view(request):
    result = {'r': 0, 'e': 'ok'}
    user_id = request.GET.get('user_id', None)
    is_all = request.GET.get('is_all', 'yes') == 'yes'
    hotel_id = request.GET.get('hotel_id', None)
    user = request.user

    re_story = get_story_info(user=user, user_id=user_id, hotel_id=hotel_id, is_all=is_all,belong_user_id=user.id)
    result['data'] = re_story

    return HttpResponse(json.dumps(result))


# --------------用户相关---------------------

def get_users(request):
    users = User.objects.all()
    u_name = [u.username for u in users]
    a = apps.get_model('link', 'HotelRoom')

    print('aaaa', a)

    return HttpResponse(json.dumps(u_name))


def edit_user_info_view(request):
    signature = request.GET.get('signature','')
    user = request.user
    print('111111:',signature)
    edit_user_info(user.id, signature)

    return HttpResponse(json.dumps({'r': 0, 'e': 'ok'}))


# ------------------订单 相关-----------------------------------

def submit_order_form_view(request):
    result = {'r': 0, 'e': 'ok'}
    web_data = request.POST
    user = request.user
    hotel_id = web_data.get('hotel_id')
    submit_data = {
        'tenant': json.loads(web_data.get('tenant')),
        'time': json.loads(web_data.get('time')),
        'price': web_data.get('price', ''),
    }
    try:
        order_id = submit_order_form(user.id, hotel_id, submit_data)
        result['order_id'] = order_id
    except Exception as e:
        result = {'r': 1, 'e': str(e)}
    return HttpResponse(json.dumps(result))


def get_order_form_view(request):
    result = {'r': 0, 'e': 'ok'}
    order_id = request.GET.get('order_id')
    user = request.user
    re = get_order_form(order_id, user)
    result['data'] = re

    return HttpResponse(json.dumps(result))


def pay_order_view(request):
    result = {'r': 0, 'e': 'ok'}
    web_data = request.POST
    order_id = web_data.get('order_id')
    price = web_data.get('price')
    user_id = request.user.id
    try:
        pay_order(order_id, price, user_id)
    except Exception as e:
        result = {'r': 1, 'e': str(e)}

    return HttpResponse(json.dumps(result))


# -------------收藏------------------------

def submit_user_collect_view(request):
    result = {'r': 0, 'e': 'ok'}
    web_data = request.GET
    user = request.user
    collect_class = web_data.get('belong_class')
    collect_id = web_data.get('belong_id')
    re = user_collect(collect_class, collect_id, user.id)
    if not re:
        result = {'r': 1, 'e': '已收藏'}

    return HttpResponse(json.dumps(result))


def get_user_collect_view(request):
    result = {'r': 0, 'e': 'ok'}
    user = request.user
    re = get_user_collect(user.id)
    result['data'] = re
    return HttpResponse(json.dumps(result))


def del_collect_obj_view(request):
    user = request.user
    web_data = request.GET
    belong_class = web_data.get('belong_class')
    belong_id = web_data.get('belong_id')
    del_collect_obj(user.id, belong_class, belong_id)
    return HttpResponse(json.dumps({'r': 0, 'e': 'ok'}))
