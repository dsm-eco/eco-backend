from django.contrib import admin

from ecoshop.models import Shop


@admin.register(Shop)
class EcoShopAdmin(admin.ModelAdmin):
    list_display = ['id', 'name']
    fields = ['name', 'address', 'content']
