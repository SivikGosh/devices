from django.contrib import admin

from .models import Device, Comment


class CommentInline(admin.TabularInline):
    model = Comment
    extra = 0


@admin.register(Device)
class DeviceAdmin(admin.ModelAdmin):
    list_display = (
        'id', 'sticker', 'building', 'ip', 'block', 'model', 'wtf', 'netmask',
        'sn', 'mac', 'street'
    )
    search_fields = (
        'id', 'sticker', 'building', 'ip', 'block', 'model', 'wtf', 'netmask',
        'sn', 'mac', 'street'
    )
    inlines = (CommentInline,)


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = (
        'id', 'text', 'device', 'published'
    )
    search_fields = (
        'id', 'text', 'device', 'published'
    )
