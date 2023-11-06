from django.core.management.base import BaseCommand
from app.models import Device
from app.devices import dev_baza


class Command(BaseCommand):
    help = 'Загрузка таблицы устройств в базу данных.'

    def handle(self, *args, **options):
        for device in dev_baza:
            Device.objects.create(
                sticker=device['Наклейка'] if 'Наклейка' in device.keys() else 'empty',
                building=device['Дом'] if 'Дом' in device.keys() else 'empty',
                ip=device['ip address'] if 'ip address' in device.keys() else 'empty',
                block=device['Район'] if 'Район' in device.keys() else 'empty',
                model=device['model'] if 'model' in device.keys() else 'empty',
                comment_1=device['comment'] if 'comment' in device.keys() else 'empty',
                wtf=device['wtf'] if 'wtf' in device.keys() else 'empty',
                netmask=device['netmask'] if 'netmask' in device.keys() else 'empty',
                comment_2=device['comment_2'] if 'comment_2' in device.keys() else 'empty',
                sn=device['serial number'] if 'serial number' in device.keys() else 'empty',
                mac=device['mac'] if 'mac' in device.keys() else 'empty',
                comment_3=device['comment_3'] if 'comment_3' in device.keys() else 'empty',
                street=device['Улица'] if 'Улица' in device.keys() else 'empty',
            )




