from django.db import models


class Device(models.Model):
    """бщая модель устройства"""

    sticker = models.PositiveSmallIntegerField(
        verbose_name='Наклейка',
        blank=True,
        null=True,
        unique=True,
    )
    building = models.CharField(max_length=255)  # Дом
    ip = models.CharField(max_length=255)  # ip address
    block = models.CharField(max_length=255)  # район
    model = models.CharField(max_length=255)  # model
    comment_1 = models.CharField(max_length=255)
    wtf = models.CharField(max_length=255)  # wtf
    netmask = models.CharField(max_length=255)  # netmask
    comment_2 = models.CharField(max_length=255)
    sn = models.CharField(max_length=255)  # serial number
    mac = models.CharField(max_length=255)  # mac
    comment_3 = models.CharField(max_length=255)
    street = models.CharField(max_length=255)  # Улица

    def __str__(self):
        return self.ip

    class Meta:
        verbose_name = 'Устройство'
        verbose_name_plural = 'Устройства'


class Comment(models.Model):
    """Модель комментариев к устройству"""

    text = models.TextField()
    device = models.ForeignKey(
        Device,
        on_delete=models.CASCADE,
        related_name='comments'
    )
    published = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = 'Комментарий'
        verbose_name_plural = 'Комментарии'
