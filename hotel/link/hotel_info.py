import json
import random
from django.db.models import Q, F
from django.apps import apps
from django.db import transaction
from link.models import HotelRoom, UsedImage, UserAppraise, AroundRegion, StoryBoard, UserProfile, OrderForm, \
    UserFavorite


def generate_random(source_list, extract_num):
    '''
    生成随机内容
    :param source_list: 要随机的list
    :param extract_num: 随机次数
    :return: str (用‘|’分隔)
    '''
    result = []
    for i in range(extract_num):
        choice = random.choice(source_list)
        if choice not in result:
            result.append(choice)

    return '|'.join(result)


def entering_hotel_info(data):
    extract_num = random.choice([2, 3, 4])
    result = generate_random(HotelRoom.TAGS, extract_num)
    data['tag'] = result
    hotel_room_obj = HotelRoom.objects.create(**data)
    return hotel_room_obj.id


def entering_around_region(user, data):
    result = {'r': 0, 'e': 'ok'}
    try:
        around_files = data['image']
        params = {
            'user': user,
            'around_type': data['around_type'],
            'name': data['name'],
            'price': float(data['price']),
            'detail': data['desc'],
        }
        around_region_obj = AroundRegion.objects.create(**params)
        if around_region_obj.id:
            save_files_for_class(around_files, 'AroundRegion', around_region_obj.id)
    except Exception as e:
        print(e)
        result = {'r': 1, 'e': str(e)}
    return result


def entering_story_board(data, files):
    result = {'r': 0, 'e': 'ok'}
    try:
        story_board = StoryBoard.objects.create(**data)
        if story_board.id:
            save_files_for_class(files, 'StoryBoard', story_board.id)
    except Exception as e:
        result = {'r': 1, 'e': str(e)}

    return result


def entering_user_appraise(data, files, avg_score, score_info, order_id):
    class_model = apps.get_model('link', data['belong_class'])
    class_obj = class_model.objects.get(id=data['belong_id'])
    exc_info = class_obj.score_info.split(',')
    score_num = class_obj.score_num
    total_score = (class_obj.total_score * score_num + int(avg_score)) / (score_num + 1)
    class_obj.score_num = score_num + 1
    class_obj.total_score = int(total_score)
    new_exc_info = []
    ss = score_info.split(',')
    for i, v in enumerate(ss):
        new_exc_info.append(
            int((int(exc_info[i]) * score_num + int(v)) / (score_num + 1))
        )
    score_info_str = ''
    for i, v in enumerate(new_exc_info):
        score_info_str += str(v) + (',' if i < len(new_exc_info) - 1 else '')
    class_obj.score_info = score_info_str
    class_obj.save()
    appraise = UserAppraise.objects.create(**data)
    print('555eee55', order_id)
    order_form_status(order_id)
    save_files_for_class(files, 'UserAppraise', appraise.id)


def is_appraise(user_id, belong_class, belong_id):
    obj = UserAppraise.objects.filter(belong_class=belong_class, user_id=int(user_id), belong_id=int(belong_id)).first()
    if obj:
        return True
    else:
        return False


def get_appraise_of_object(belong_class, belong_id, len_max=None):
    appraise = UserAppraise.objects.filter(belong_class=belong_class, belong_id=belong_id)
    class_model = apps.get_model('link', belong_class)
    class_obj = class_model.objects.get(id=belong_id)
    user_list = [{
        'user_name': ap.user.username,
        'user_info': get_user_info(ap.user.id),
        'appraise': ap.appraise,
        'about_time': ap.about_time.strftime('%Y-%m-%d'),
        'img': get_img_for_obj(ap.id, 'UserAppraise'),
    } for ap in appraise]
    total_appraise = {'score_info': class_obj.score_info, 'total_score': class_obj.total_score}
    result_data = {'user_list': user_list[0:len_max] if len_max else user_list, 'total_appraise': total_appraise,
                   'appraise_num': len(user_list)}
    return result_data


def get_around_region(user, user_id, is_all):
    if user_id:
        around_region_objs = AroundRegion.objects.filter(user__id=user_id)
    else:
        around_region_objs = AroundRegion.objects.filter(user=user)
    if is_all:
        around_region_objs = AroundRegion.objects.all()
    around_region_list = []
    for obj in around_region_objs:
        around_img_objs = UsedImage.objects.filter(belong_id=obj.id, belong_class='AroundRegion')
        imgs = []
        for arr_img in around_img_objs:
            imgs.append(arr_img.image.url)
        around_region_list.append(
            {'name': obj.name, 'id': obj.id, 'imgs': imgs, 'around_type': obj.around_type, 'obj_class': 'AroundRegion',
             'price': obj.price, 'detail': obj.detail})

    return around_region_list


def get_hotel_room_info(user_id=None, search=None, hotel_id=None, belong_user_id=None):
    if not user_id:
        hotel_rooms = HotelRoom.objects.filter()
    else:
        hotel_rooms = HotelRoom.objects.filter(user_id=user_id)
    if hotel_id:
        hotel_rooms = hotel_rooms.filter(id=hotel_id)

    if search:
        hotel_rooms = hotel_rooms.filter(Q(position__contains=search) | Q(name__contains=search))
    result_hotels = [{'user_id': hotel.user.id,
                      'hotel_id': hotel.id,
                      'name': hotel.name,
                      'position': hotel.position,
                      'hose_type': hotel.hose_type,
                      'room_type': hotel.room_type,
                      'host_signer': json.loads(hotel.host_signer),
                      'host_desc': hotel.host_desc,
                      'rim': json.loads(hotel.rim),
                      'facility': json.loads(hotel.facility),
                      'price': hotel.price,
                      'tag': hotel.tag,
                      'obj_class': 'HotelRoom',
                      'is_collect': get_is_collect(belong_user_id, 'HotelRoom', hotel.id),
                      'imgs': get_img_for_obj(hotel.id, 'HotelRoom'),
                      'total_score': hotel.total_score} for hotel in hotel_rooms]
    return result_hotels


def get_one_hotel_and_around(hotel_id, belong_user_id=None):
    result = dict()
    hotel_obj = HotelRoom.objects.get(id=hotel_id)
    hotel_user_obj = hotel_obj.user
    hotel_dict = get_hotel_room_info(hotel_id=hotel_id, belong_user_id=belong_user_id)
    around_list = get_around_info(hotel_id=hotel_id)
    hotel_user = get_user_info(hotel_user_obj.id)
    similar_hotel = get_similar_hotel(hotel_obj.tag.split('|'))
    result['hotel_dict'] = hotel_dict
    result['around_list'] = around_list
    result['hotel_user'] = hotel_user
    result['similar_hotel'] = similar_hotel
    result['hotel_Appraise'] = get_appraise_of_object('HotelRoom', hotel_id, len_max=1)

    return result


def get_similar_hotel(tags):
    tag_len = len(tags)
    _filter = ""
    for i in range(tag_len):
        _filter += "tag LIKE '%{}%'".format(tags[i]) + (" or " if (i < tag_len - 1) else "")

    hotels = HotelRoom.objects.extra(where=[_filter])
    hostel_list = []
    for h in hotels:
        tag_num = 0
        h_tags = h.tag.split('|')
        for t in tags:
            if t in h_tags:
                tag_num += 1
        hostel_list.append({'hotel_obj': h, 'similar': tag_num})

    hostel_list.sort(key=sort_key_for_dict, reverse=True)

    list_similar = [{'user_id': one['hotel_obj'].user.id,
                     'hotel_id': one['hotel_obj'].id,
                     'name': one['hotel_obj'].name,
                     'position': one['hotel_obj'].position,
                     'hose_type': one['hotel_obj'].hose_type,
                     'room_type': one['hotel_obj'].room_type,
                     'host_signer': json.loads(one['hotel_obj'].host_signer),
                     'host_desc': one['hotel_obj'].host_desc,
                     'rim': json.loads(one['hotel_obj'].rim),
                     'facility': json.loads(one['hotel_obj'].facility),
                     'price': one['hotel_obj'].price,
                     'tag': one['hotel_obj'].tag,
                     'obj_class': 'HotelRoom',
                     'imgs': get_img_for_obj(one['hotel_obj'].id, 'HotelRoom'),
                     'total_score': one['hotel_obj'].total_score} for one in hostel_list[1:2]]
    return list_similar


def sort_key_for_dict(item):
    return item['similar']


def get_around_info(user_obj=None, search=None, hotel_id=None):
    around_list = AroundRegion.objects.filter()
    if user_obj:
        around_list = around_list.filter(user=user_obj)
    if search:
        around_list = around_list.filter(name__contains=search)
    if hotel_id:
        around_list = around_list.filter(hotel_id=hotel_id)
    result = [{'user_id': around.user.id,
               'around_id': around.id,
               'hotel_id': around.hotel.id if around.hotel else '',
               'name': around.name,
               'price': around.price,
               'around_type': around.around_type,
               'obj_class': 'AroundRegion',
               'imgs': get_img_for_obj(around.id, 'AroundRegion'),
               'detail': around.detail} for around in around_list]
    print('result:', result)
    return result


def get_img_for_obj(obj_id, obj_class):
    img_list = []
    img_objs = UsedImage.objects.filter(belong_id=obj_id, belong_class=obj_class)
    for img in img_objs:
        img_list.append(img.image.url)
    return img_list


def get_all_portrait():
    imgs = UsedImage.objects.filter(belong_class='UserProfile')
    img_list = [
        {'img': img.image.url, 'img_id': img.id} for img in imgs
    ]
    return img_list


def get_story_info(user=None, user_id=None, hotel_id=None, is_all=None, story_id=None):
    if user_id:
        storyboard = StoryBoard.objects.filter(user_id=user_id)
    else:
        storyboard = StoryBoard.objects.filter(user=user)
    if hotel_id:
        storyboard = StoryBoard.objects.filter(hotel_id=hotel_id)
    if is_all:
        storyboard = StoryBoard.objects.all()
    if story_id:
        storyboard = StoryBoard.objects.filter(id=story_id)
    result_list = [{
        'user_id': story.user_id,
        'hotel_id': story.hotel_id,
        'story_id': story.id,
        'name': story.theme,
        'content': story.content,
        'create_time': story.create_time.strftime('%Y-%m-%d'),
        'obj_class': 'StoryBoard',
        'user_info': get_user_info(story.user_id),
        'imgs': get_img_for_obj(story.id, 'StoryBoard')
    } for story in storyboard]
    return result_list


def save_files_for_class(files, _class, obj_id):
    for file in files:
        img_params = {
            'belong_class': _class,
            'belong_id': obj_id,
            'image': file,
        }
        UsedImage.objects.create(**img_params)


def save_around_for_hotel(hotel_room_id, around_ids):
    AroundRegion.objects.filter(id__in=around_ids).update(hotel_id=hotel_room_id)


# -------------------user 相关---------------------------------

def get_user_info(user_id):
    user_obj = UserProfile.objects.get(id=user_id)
    user_info = {
        'user_name': user_obj.user.username,
        'show_name': user_obj.show_name,
        'property': user_obj.property,
        'score': user_obj.score,
        'register_time': user_obj.register_time.strftime('%Y-%m-%d'),
        'avatar': user_obj.avatar,
        'signature': user_obj.signature,
    }

    return user_info


def edit_user_info(user_id, _info):
    UserProfile.objects.filter(user_id=user_id).update(signature=_info)


# ------------------订单 相关-----------------------------------

def submit_order_form(user_id, hotel_id, submit_data):
    params = {
        'create_id': user_id,
        'hotel_id': hotel_id,
        'detail': json.dumps(submit_data),
    }
    order = OrderForm.objects.create(**params)
    return order.id


def get_order_form(order_id, user):
    print('55555', order_id, user.id)
    if order_id:
        orders = OrderForm.objects.filter(id=order_id)
    else:
        orders = OrderForm.objects.filter(create_id=user.id)

    re = [{
        'order_id': o.id,
        'create': o.create.username,
        'hotel_id': o.hotel.id,
        'order_status': o.order_status,
        'belong_class': 'OrderForm',
        'order_info': json.loads(o.detail),
        'hotel_info': get_hotel_room_info(hotel_id=o.hotel.id)
    } for o in orders]
    return re


def pay_order(order_id, price, user_id):
    OrderForm.objects.filter(id=order_id).update(order_status=2)
    with transaction.atomic():
        hotel_user = OrderForm.objects.get(id=order_id).hotel.user.user_profile
        hotel_user.property = F('property') + int(price)
        hotel_user.save()
        u = UserProfile.objects.get(user_id=user_id)
        u.score = F('score') + int(price)
        u.property = F('property') - int(price)
        u.save()


def order_form_status(order_id):
    OrderForm.objects.filter(id=order_id).update(order_status=3)


# ------------------收藏-----------------
def user_collect(collect_class, collect_id, user_id):
    params = {
        'user_id': user_id,
        'favorite_class': collect_class,
        'favorite_id': collect_id,
    }
    UserFavorite.objects.create(**params)


def get_user_collect(user_id):
    collects = UserFavorite.objects.filter(user_id=user_id)
    re = []
    for collect in collects:
        belong_class = collect.favorite_class
        belong_id = collect.favorite_id
        belong_info = 'not this class function'
        if belong_class == 'HotelRoom':
            belong_info = get_hotel_room_info(hotel_id=belong_id)
        if belong_class == 'StoryBoard':
            belong_info = get_story_info(story_id=belong_id)
        re.append({
            'belong_class': belong_class,
            'belong_id': belong_id,
            'belong_info': belong_info,
        })

    return re


def get_is_collect(user_id, belong_class, belong_id):
    params = {
        'user_id': user_id,
        'favorite_class': belong_class,
        'favorite_id': belong_id
    }
    obj = UserFavorite.objects.filter(**params).first()
    if obj:
        return True
    else:
        return False


def del_collect_obj(user_id, belong_class, belong_id):
    params = {
        'user_id': user_id,
        'favorite_class': belong_class,
        'favorite_id': belong_id
    }
    UserFavorite.objects.filter(**params).delete()
