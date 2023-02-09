from django.views.generic import ListView
from .models import Wine
from django.shortcuts import render


def home(request):
    return render(request, 'app/home.html')


class WinesView(ListView):
    """Wine objects"""
    model = Wine
    template_name = 'app/wines.html'
    context_object_name = 'wines'
    queryset = Wine.objects.all()

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['sugars'] = Wine.SUGAR_AMOUNT
        context['colors'] = Wine.COLOR_TYPE
        return context


