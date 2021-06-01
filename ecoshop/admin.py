from django.contrib import admin

from ecoshop.models import Shop, ShopImage


@admin.register(Shop)
class EcoShopAdmin(admin.ModelAdmin):
    list_display = ['id', 'name']
    fields = ['name', 'address', 'content']


@admin.register(ShopImage)
class ShopImageAdmin(admin.ModelAdmin):
    list_display = ['id', 'shop_id']
    fields = ['shop_id', 'image']
