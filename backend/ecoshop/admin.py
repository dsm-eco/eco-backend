from django.contrib import admin

from ecoshop.models import ShopPost


@admin.register(ShopPost)
class EcoShopPostAdmin(admin.ModelAdmin):
    list_display = ['id', 'nickname', 'name', 'content', 'heart_cnt', 'report']
