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
    print('data', data)
    print('all_obj', color_obj)
    for item in color_obj:
        print('item', item)
        for title in data:
            print(' title', title)
            if title == item.title:
                item.is_checked = True
                print(item, 'True')
                item.save()
                break
            else:
                item.is_checked = False
                print(item, 'False')
                item.save()


def update_sugars_checkboxes(data):
    """
    Функция устанавливает True только у
    выбранных чек-боксов содержания сахара
    и False у не чекнутых.
    """
    sugar_obj = SugarAmount.objects.all()
    print('data', data)
    print('all_obj', sugar_obj)
    for item in sugar_obj:
        print('item', item)
        for title in data:
            print(' title', title)
            if title == item.title:
                item.is_checked = True
                print(item, 'True')
                item.save()
                break
            else:
                item.is_checked = False
                print(item, 'False')
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