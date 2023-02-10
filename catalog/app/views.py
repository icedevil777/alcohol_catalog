from django.http import HttpResponse
from django.views import View
from django.views.decorators.csrf import csrf_exempt
from django.views.generic import ListView
from .models import Wine, Beer, ColorType, SugarAmount
from django.shortcuts import render

from .utils import update_colors_checkboxes, update_sugars_checkboxes, \
    set_false_all_checkboxes, create_color_list_id, create_sugar_list_id


def home(request):
    return render(request, 'app/home.html')


class WinesView(View):
    """Wine objects"""

    def get_content(self):
        queryset = Wine.objects.all()
        colors = ColorType.objects.all()
        sugars = SugarAmount.objects.all()
        return {
            'wines': queryset,
            'colors': colors,
            'sugars': sugars,
        }

    def get(self, request):
        content = self.get_content()
        set_false_all_checkboxes(content)
        return render(request, 'app/wines.html', content)

    @csrf_exempt
    def post(self, request):
        data = request.POST
        content = self.get_content()
        print("data.getlist('color')", data)

        # if data['wine_search']:
        if data.get('wine_search'):
            queryset = content['wines'].filter(
                title__icontains=str(data['wine_search']))
            content['wines'] = queryset

        if data.get('color'):
            list_color_id = create_color_list_id(data.getlist('color'))
            content['wines'] = content['wines'].filter(
                color_id__in=list_color_id)
            update_colors_checkboxes(data.getlist('color'))

        if data.get('sugar'):
            list_sugar_id = create_sugar_list_id(data.getlist('sugar'))
            content['wines'] = content['wines'].filter(
                sugar_id__in=list_sugar_id)
            update_sugars_checkboxes(data.getlist('sugar'))

        # if data['sort_by']:
        #     if data['sort_by'] == 'first_new':
        #         content['wines'] = content['wines'].order_by('-created_at')
        #     if data['sort_by'] == 'first_old':
        #         content['wines'] = content['wines'].order_by('created_at')

        return render(request, 'app/wines.html', content)


class BeersView(ListView):
    """Wine objects"""
    template_name = 'app/beers.html'
    context_object_name = 'beers'
    queryset = Beer.objects.all()

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['types'] = Beer.TYPE
        return context
