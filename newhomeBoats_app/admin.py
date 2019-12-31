from django.contrib import admin
from .models import City, State, IBGECityCodes
# Register your models here.

class CityAdmin(admin.ModelAdmin):
    search_fields = ['city']
    list_display = ['city', 'state']
    pass
admin.site.register(City, CityAdmin)

admin.site.register(State)


class IBGECityCodesAdmin(admin.ModelAdmin):
    search_fields = ['ibge_id', 'name']
    list_display = ['ibge_id', 'name']
    pass
admin.site.register(IBGECityCodes, IBGECityCodesAdmin)