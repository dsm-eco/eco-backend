from django.contrib import admin

from user_system.models import User


@admin.register(User)
class EventAdmin(admin.ModelAdmin):
    list_display = ['id', 'username', 'nickname']
    fields = ['nickname', 'username']
    readonly_fields = ['nickname', 'username']
