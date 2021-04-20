from django.contrib import admin

from ecoshop.models import ShopPost


@admin.register(ShopPost)
class EcoShopPostAdmin(admin.ModelAdmin):
    list_display = ['id', 'nickname', 'name', 'report']
    fields = ['nickname', 'name', 'address', 'content', 'report']
    readonly_fields = ['nickname', 'name', 'address', 'content', 'report']
