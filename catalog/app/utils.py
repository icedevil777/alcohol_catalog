from .models import ColorType, SugarAmount, Wine


def set_false_all_checkboxes(content):
    """
    Сбрасывает все невыбранные чек-боксы
    """
    set_false_colors_checkboxes(content)
    set_false_sugars_checkboxes(content)


def set_false_colors_checkboxes(content):
    """
    Функция сбрасывает все чек-боксы
    цвета вина, когда они все не чекнуты
    """
    for obj in content['colors']:
        obj.is_checked = False
        obj.save()


def set_false_sugars_checkboxes(content):
    """
    Функция сбрасывает все чек-боксы
    содержания сахара, когда они все не чекнуты
    """
    for obj in content['sugars']:
        obj.is_checked = False
        obj.save()


def update_colors_checkboxes(data):
    """
    Функция устанавливает True только
    у выбранных чек-боксов цвета вина
    и False у не чекнутых.
    """
    color_obj = ColorType.objects.all()
    for item in color_obj:
        for title in data:
            if title == item.title:
                item.is_checked = True
                item.save()
                break
            else:
                item.is_checked = False
                item.save()


def update_sugars_checkboxes(data):
    """
    Функция устанавливает True только у
    выбранных чек-боксов содержания сахара
    и False у не чекнутых.
    """
    sugar_obj = SugarAmount.objects.all()
    for item in sugar_obj:
        for title in data:
            if title == item.title:
                item.is_checked = True
                item.save()
                break
            else:
                item.is_checked = False
                item.save()


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


def get_str_order_by_id(param):
    """Принимает id и формирует строку"""
    if int(param) == 1:
        return 'price'
    if int(param) == 2:
        return '-price'
    return 'title'
