from django.apps import AppConfig


class SmsConfig(AppConfig):
    name = 'sms'
    default_auto_field = "django.db.models.BigAutoField"

    def ready(self):
        from sms import signals
