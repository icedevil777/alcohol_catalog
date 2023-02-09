from django.http import HttpResponse
from django.views import View
from django.views.decorators.csrf import csrf_exempt
from django.views.generic import ListView
from .models import Wine
from django.shortcuts import render


def home(request):
    return render(request, 'app/home.html')


class WinesView(View):
    """Wine objects"""

    def get_content(self):
        queryset = Wine.objects.all()
        sugars = Wine.SUGAR_AMOUNT
        colors = Wine.COLOR_TYPE
        return {
            'wines': queryset,
            'colors': colors,
            'sugars': sugars
        }

    def get(self, request):
        return render(request, 'app/wines.html', self.get_content())

    @csrf_exempt
    def post(self, request):
        content = self.get_content()
        request_title = request.POST.get('wine_search')
        if request_title:
            queryset = Wine.objects.filter(title__icontains=str(request_title))
            content['wines'] = queryset
        return render(request, 'app/wines.html', content)


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
