import requests
from zoneinfo import ZoneInfo
import datetime
from celery.utils.log import get_task_logger

from .models import Message, Client, Mailing
from config.celery import app

logger = get_task_logger(__name__)


API = 'https://probe.fbrq.cloud/docs'
TOKEN = 'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJleHAiOjE3MTkzMTQ0MzcsImlzcyI6ImZhYnJpcXVlIiwibmFtZSI6Imh0dHBzOi8vdC5tZS9EZXJpYWJpbl84NSJ9.D93J6vq6KJgloETPCwujLFk8h4aXvU-ls5KwztXsirY'


@app.task(bind=True, retry_backoff=True)
def send_message(self, data, client_id, mailing_id, url=API, token=TOKEN):
    mail = Mailing.objects.get(pk=mailing_id)
    client = Client.objects.get(pk=client_id)
    timezone = ZoneInfo(client.timezone)
    now = datetime.datetime.now(timezone)

    if mail.start_date.time() <= now.time() <= mail.end_date.time():
        header = {
            "Authorization": f"Bearer {token}",
            "Content-Type": "application/json",
        }
        try:
            requests.post(url=url + str(data["id"]), headers=header, json=data)
        except requests.exceptions.RequestException as exc:
            logger.error(f"Message if: {data['id']} is error")
            raise self.retry(exc=exc)
        else:
            logger.info(f"Message id: {data['id']}, Sending status: 'Отправлено'")
            Message.objects.filter(pk=data["id"]).update(sending_status="Отправлено")
    else:
        time = 24 - (
            int(now.time().strftime("%H:%M:%S")[:2])
            - int(mail.start_date.time().strftime("%H:%M:%S")[:2])
        )
        logger.info(
            f"Message id: {data['id']}, "
            f"The current time is not for sending the message,"
            f"restarting task after {60*60*time} seconds"
        )
        return self.retry(countdown=60 * 60 * time)
