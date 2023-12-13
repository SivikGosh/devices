from django.contrib import admin

from .models import Device, Comment, Location


class CommentInline(admin.TabularInline):
    model = Comment
    extra = 0


@admin.register(Device)
class DeviceAdmin(admin.ModelAdmin):
    list_display = ('id', 'sticker', 'ip', 'model', 'netmask', 'sn', 'mac', 'state', 'location')
    search_fields = ('id', 'sticker', 'ip', 'model', 'netmask', 'sn', 'mac', 'state', 'location')
    inlines = (CommentInline,)
    list_per_page = 10


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ('id', 'text', 'device', 'published')
    search_fields = ('id', 'text', 'device', 'published')


@admin.register(Location)
class LocationAdmin(admin.ModelAdmin):
    list_display = ('id', 'block', 'street', 'building')
    search_fields = ('id', 'block', 'street', 'building')
