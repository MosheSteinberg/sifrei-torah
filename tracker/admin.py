from django.contrib import admin

from .models import SeferTorah, PhysicalLocation


class SeferAdmin(admin.ModelAdmin):
    list_display = ('__str__', 'physical_location', 'location_in_text', 'quality')
    list_filter = ('physical_location', 'location_in_text', 'quality')

# Register your models here.
admin.site.register(SeferTorah, SeferAdmin)
admin.site.register(PhysicalLocation)