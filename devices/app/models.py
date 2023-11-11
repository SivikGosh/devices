from django.db import models


class Location(models.Model):
    """Модель адреса местонахождения оборудования"""

    # Район: 'Склад', 'empty', 'Красногорск', 'Лобня', 'Москва', 'Октябрьский', 'Котельники', 'Люберцы'
    block = models.CharField(
        verbose_name='Район',
        max_length=255,
        null=True
    )
    street = models.CharField(
        verbose_name='Улица / Проезд',
        max_length=255,
        null=True
    )
    building = models.CharField(
        verbose_name='Дом',
        max_length=255,
        null=True
    )

    def __str__(self):
        return f'{self.block}, {self.street}, дом {self.building}'

    class Meta:
        verbose_name = 'Локация'
        verbose_name_plural = 'Локации'


class Device(models.Model):
    """"Общая модель устройства"""

    STATES = [
        ('И', 'Используется'),
        ('У', 'Установлен'),
        ('Д', 'Демонтирован'),
        ('З', 'В запасе'),
        ('С', 'Вышел из строя'),
    ]

    sticker = models.PositiveSmallIntegerField(
        verbose_name='Наклейка',
        blank=True,
        null=True,
        unique=True,
    )
    state = models.CharField(
        verbose_name='Текущий статус',
        max_length=1,
        choices=STATES,
        default=STATES[3],
        blank=True,
        null=True
    )
    location = models.ForeignKey(
        Location,
        verbose_name='Локация',
        max_length=255,
        null=True,
        on_delete=models.SET_NULL
    )

    ip = models.CharField(max_length=255)  # ip address
    model = models.CharField(max_length=255)  # model
    netmask = models.CharField(max_length=255)  # netmask
    sn = models.CharField(max_length=255)  # serial number
    mac = models.CharField(max_length=255)  # mac

    def __str__(self):
        return self.ip

    class Meta:
        verbose_name = 'Устройство'
        verbose_name_plural = 'Устройства'


class Comment(models.Model):
    """Модель комментариев к устройству"""

    text = models.TextField(
        verbose_name='Сообщение',
        max_length=1000
    )
    device = models.ForeignKey(
        Device,
        verbose_name='Оборудование',
        on_delete=models.CASCADE,
        related_name='comments'
    )
    published = models.DateTimeField(
        auto_now_add=True
    )

    def __str__(self):
        return self.text

    class Meta:
        verbose_name = 'Комментарий'
        verbose_name_plural = 'Комментарии'
