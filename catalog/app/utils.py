from .models import ColorType, SugarAmount


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


def update_sugar_checkboxes(data):
    """
    Функция обновляет выбранные
    чек-боксы содержания сахара
    """
    for title in data:
        color_obj = SugarAmount.objects.get(title=title)
        color_obj.is_checked = True
        color_obj.save()
