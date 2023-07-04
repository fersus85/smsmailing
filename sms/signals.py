from django.db.models.signals import post_save
from django.dispatch import receiver
from django.db.models import Q

from .models import Mailing, Client, Message
from .tasks import send_message


@receiver(post_save, sender=Mailing, dispatch_uid="create_message")
def create_message(sender, instance, created, **kwargs):
    if created:
        mailing = Mailing.objects.filter(id=instance.id).first()
        clients = Client.objects.filter(
            Q(code=mailing.code) | Q(tag=mailing.tag)
        ).all()

        for client in clients:
            Message.objects.create(
                status="Не отправлено", client_id=client.id, mailing_id=instance.id
            )
            message = Message.objects.filter(
                mailing_id=instance.id, client_id=client.id
            ).first()
            data = {
                "id": message.id,
                "phone": client.phone_number.as_e164,
                "text": mailing.message,
            }
            client_id = client.id
            mailing_id = mailing.id

            if instance.is_send:
                send_message.apply_async(
                    (data, client_id, mailing_id), expires=mailing.date_end
                )
            else:
                send_message.apply_async(
                    (data, client_id, mailing_id),
                    eta=mailing.start_date,
                    expires=mailing.end_date,
                )
