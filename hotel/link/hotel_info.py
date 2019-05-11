import json
from link.models import HotelRoom, UsedImage, UserAppraise, AroundRegion


def entering_hotel_info(data):
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
            'price': data['price'],
            'detail': data['desc'],
        }
        around_region_obj = AroundRegion.objects.create(**params)
        if around_region_obj.id:
            save_files_for_hotel(around_files,'AroundRegion',around_region_obj.id)
    except Exception as e:
        print(e)
        result = {'r': 1, 'e': str(e)}
    return result


def entering_story_board(data):
    return {}



def get_around_region(user):
    around_region_objs = AroundRegion.objects.filter(user=user)
    around_region_list = []
    for obj in around_region_objs:
        arround_img_obj = UsedImage.objects.get(belong_id=obj.id,belong_class='AroundRegion')
        around_region_list.append({'name':obj.name,'id':obj.id,'img':arround_img_obj.image})

    return around_region_list

def save_files_for_hotel(files,class_obj,obj_id):
    for file in files:
        img_params = {
            'belong_class': class_obj,
            'belong_id': obj_id,
            'image': file,
        }
        UsedImage.objects.create(**img_params)

def save_around_for_hotel(hotel_room_id,around_ids):
    AroundRegion.objects.filter(id__in=around_ids).update(hotel__id=hotel_room_id)