from django.contrib import admin
from import_export.admin import ImportExportModelAdmin
from import_export import resources

from .models import Wine, Category, Beer, SugarAmount, ColorType

admin.site.register(SugarAmount)
admin.site.register(ColorType)
admin.site.register(Category)


@admin.register(Wine)
class WineAdmin(ImportExportModelAdmin):
    class WineResource(resources.ModelResource):
        class Meta:
            model = Wine

    list_display = ["go_text", 'id', 'title_rus', 'title', 'color',
                    'sugar', 'price']
    list_filter = ('created_date', 'updated_date')
    resource_class = WineResource
    search_fields = ['id', 'title_rus', 'title']

    def go_text(self, *args, **kwargs):
        return "GO"


@admin.register(Beer)
class BeerAdmin(ImportExportModelAdmin):
    class BeerResource(resources.ModelResource):
        class Meta:
            model = Beer

    list_display = ["go_text", 'id', 'title_rus', 'title', 'type']
    list_filter = ('created_date', 'updated_date')
    resource_class = BeerResource
    search_fields = ['id', 'title_rus', 'title']

    def go_text(self, *args, **kwargs):
        return "GO"