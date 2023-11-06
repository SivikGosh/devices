from django.contrib import admin

from .models import Device


@admin.register(Device)
class DeviceAdmin(admin.ModelAdmin):
    list_display = (
        'sticker',
        'building',
        'ip',
        'block',
        'model',
        'comment_1',
        'wtf',
        'netmask',
        'comment_2',
        'sn',
        'mac',
        'comment_3',
        'street'
    )
    search_fields = (
        'sticker',
        'building',
        'ip',
        'block',
        'model',
        'comment_1',
        'wtf',
        'netmask',
        'comment_2',
        'sn',
        'mac',
        'comment_3',
        'street'
    )
