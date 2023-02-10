from django.http import HttpResponse
from django.views import View
from django.views.decorators.csrf import csrf_exempt
from django.views.generic import ListView
from .models import Wine, Beer, ColorType, SugarAmount
from django.shortcuts import render

from .utils import update_colors_checkboxes, update_sugar_checkboxes, \
    set_false_all_checkboxes


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

        if data.get('color'):
            queryset = Wine.objects.filter(
                title__icontains=str(data['wine_search']))
            update_colors_checkboxes(data.getlist('color'))

        if data.get('sugar'):
            update_sugar_checkboxes(data.getlist('sugar'))

        if data['wine_search']:
            queryset = Wine.objects.filter(
                title__icontains=str(data['wine_search']))
            content['wines'] = queryset

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

# class WinesView(ListView):
#     """Wine objects"""
#     template_name = 'app/wines.html'
#     context_object_name = 'wines'
#     # queryset = Wine.objects.all()
#     title = None
#
#     def get_context_data(self, **kwargs):
#         context = super().get_context_data(**kwargs)
#         context['sugars'] = Wine.SUGAR_AMOUNT
#         context['colors'] = Wine.COLOR_TYPE
#         return context
#
#     def get_queryset(self, **kwargs):
#         title1 = self.title
#         print('title1', title1)
#         queryset = Wine.objects.all()
#         return queryset
#
#     @csrf_exempt
#     def post(self, request):
#         self.title = request.body.decode('utf-8')
#         return HttpResponse(self.queryset)
