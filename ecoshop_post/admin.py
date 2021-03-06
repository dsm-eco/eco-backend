from django.contrib import admin

from ecoshop_post.models import ShopPost


@admin.register(ShopPost)
class EcoShopPostAdmin(admin.ModelAdmin):
    list_display = ['id', 'nickname', 'name', 'report', 'permission', 'heart_cnt']
    fields = ['nickname', 'name', 'address', 'content', 'report']
    readonly_fields = ['nickname', 'name', 'address', 'content', 'report']
    list_editable = ('permission', )
    list_filter = ('permission', )
    ordering = ('-report', 'id')

    def heart_cnt(self, obj):
        return obj.shop_post_likes_user.count()
