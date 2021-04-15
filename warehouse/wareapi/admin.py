from django.contrib import admin
from .models import warehouse

class warehouseAdmin(admin.ModelAdmin):
    list_display = ('title', 'forename', 'surname', 'deliverycompany', 'con_number')


admin.site.register(warehouse, warehouseAdmin)
