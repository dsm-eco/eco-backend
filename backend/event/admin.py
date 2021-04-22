from django.contrib import admin

from event.models import Event


@admin.register(Event)
class EventAdmin(admin.ModelAdmin):
    list_display = ['id', 'nickname']
    fields = ['nickname', 'content', 'event_date']
    readonly_fields = ['nickname', 'content', 'event_date']
