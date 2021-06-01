from django.contrib import admin

from ecoshop.models import Shop, ShopImage


class ShopImageAdmin(admin.StackedInline):
    model = ShopImage


class EcoShopAdmin(admin.ModelAdmin):
    list_display = ['id', 'name']
    fields = ['name', 'address', 'content']
    inlines = [ShopImageAdmin]


admin.site.register(Shop, EcoShopAdmin)
