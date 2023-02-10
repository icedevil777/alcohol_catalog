from .models import ColorType, SugarAmount, Wine


def set_false_all_checkboxes(content):

    for obj in content['sugars']:
        obj.is_checked = False
        obj.save()

    for obj in content['colors']:
        obj.is_checked = False
        obj.save()


def update_colors_checkboxes(data):
    """
    Функция обновляет выбранные
    чек-боксы цвета вина
    """
    for title in data:
        color_obj = ColorType.objects.get(title=title)
        color_obj.is_checked = True
        color_obj.save()


def update_sugars_checkboxes(data):
    """
    Функция обновляет выбранные
    чек-боксы содержания сахара
    """
    for title in data:
        sugar_obj = SugarAmount.objects.get(title=title)
        sugar_obj.is_checked = True
        sugar_obj.save()


def create_color_list_id(title_list):
    """Преобразует список title в список id"""
    list_id: list = []
    for title in title_list:
        list_id.append(ColorType.objects.get(title=title).id)
    return list_id


def create_sugar_list_id(title_list):
    """Преобразует список title в список id"""
    list_id: list = []
    for title in title_list:
        list_id.append(SugarAmount.objects.get(title=title).id)
    return list_id