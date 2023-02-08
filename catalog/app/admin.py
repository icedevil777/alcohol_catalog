from django.contrib import admin
from import_export.admin import ImportExportModelAdmin
from import_export import resources

from .models import Wine


@admin.register(Wine)
class WineAdmin(ImportExportModelAdmin):
    class WineResource(resources.ModelResource):
        class Meta:
            model = Wine

    list_display = ["go_text", 'id', 'title_rus', 'title', 'COLOR_TYPE',
                    'SUGAR_AMOUNT', 'price']
    list_filter = ('created_date', 'updated_date')
    resource_class = WineResource
    search_fields = ['id', 'title_rus', 'title']

    def go_text(self, *args, **kwargs):
        return "GO"
