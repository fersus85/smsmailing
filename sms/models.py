from django.utils import timezone
from django.db import models
import zoneinfo
from phonenumber_field.modelfields import PhoneNumberField

TIMEZONES = tuple(zip(zoneinfo.available_timezones(), zoneinfo.available_timezones()))


class Client(models.Model):
    tag = models.CharField(verbose_name='Тэг-метка', max_length=20, blank=True)
    phone_number = PhoneNumberField(verbose_name='Номер телефона', region='RU', blank=True, unique=True)
    code = models.CharField(verbose_name='Код оператора', max_length=3, editable=False)
    timezone = models.CharField(verbose_name='Часовой пояс', max_length=50, choices=TIMEZONES, default='Europe/Moscow')

    def save(self, *args, **kwargs):
        self.code = str(self.phone_number)[2:5]
        return super(Client, self).save(*args, **kwargs)

    def __str__(self):
        return f'client id: {self.id}, {self.phone_number}, code:{self.code}'


class Mailing(models.Model):
    start_date = models.DateTimeField(verbose_name='Время начала рассылки')
    end_date = models.DateTimeField(verbose_name='Время конца рассылки')
    message = models.TextField(verbose_name='Сообщение', max_length=255)
    tag = models.CharField(verbose_name='Тэг-метка', max_length=20, blank=True)
    code = models.CharField(verbose_name='Код оператора', max_length=3, blank=True)

    def __str__(self):
        return f'id: {self.id}, starting {self.start_date}'

    @property
    def is_send(self):
        return bool(self.start_date <= timezone.now() <= self.end_date)


class Message(models.Model):
    cr_date_time = models.DateTimeField(verbose_name='Время создания', auto_now=True)
    status = models.CharField(verbose_name='Статус отправки', max_length=30,
                              choices=[('Отправлено', 'Отправлено'), ('Не отправлено', 'Не отправлено')])
    mailing = models.ForeignKey(Mailing, on_delete=models.CASCADE, related_name='messages')
    client = models.ForeignKey(Client, on_delete=models.CASCADE, related_name='messages')

    def __str__(self):
        return f'mes id: {self.id}, mailing: {self.mailing}, client: {self.client}, status: {self.status}'
