from django.core.management.base import BaseCommand
from app.models import Device, Comment


class Command(BaseCommand):
    help = 'Перенос комментариев в отдельную модель.'

    def handle(self, *args, **options):
        all_devices = Device.objects.all()
        for device in all_devices:
            if device.comment_1 != 'empty':
                Comment.objects.create(text=device.comment_1, device=device.id)
            elif device.comment_2 != 'empty':
                Comment.objects.create(text=device.comment_2, device=device.id)
            elif device.comment_3 != 'empty':
                Comment.objects.create(text=device.comment_3, device=device.id)
