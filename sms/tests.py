from django.urls import reverse
from django.utils.timezone import now
from rest_framework.test import APITestCase
from .models import Mailing, Client, Message
from rest_framework import status
import json


class SMSAPITest(APITestCase):

    @classmethod
    def setUpTestData(cls):
        Mailing.objects.create(
            start_date=now(),
            end_date=now(),
            message="Hello, friend!",
            tag="test"
        )
        Client.objects.create(
            tag='newone',
            phone_number='+79180111111'
        )
        Message.objects.create(
            cr_date_time=now(),
            status='Не отправлено',
            mailing=Mailing.objects.get(pk=1),
            client=Client.objects.get(pk=1)
        )

    def test_mailing_create(self):
        mail = Mailing.objects.get(pk=1)
        self.assertIsInstance(mail, Mailing)
        self.assertEqual(mail.tag, "test")

    def test_get_mailings(self):
        url = reverse('mailings-list')
        response = self.client.get(url, format='json')
        message = response.data[0]['message']
        tag = response.data[0]['tag']
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(tag, 'test')
        self.assertEqual(message, 'Hello, friend!')

    def test_update_mailings(self):
        url = reverse('mailings-detail', args=[1])
        data = {
            'start_date': now(),
            'end_date': now(),
            'message': "By!",
            'tag': "no",
            'code': 918,
        }
        response = self.client.put(url, data=data, format='json')
        updated_message = response.data['message']
        updated_tag = response.data['tag']
        self.assertEqual(updated_message, 'By!')
        self.assertEqual(updated_tag, 'no')

    def test_get_messages(self):
        url = reverse('messages-list')
        response = self.client.get(url, format='json')
        status_m = response.data[0]['status']
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(status_m, 'Не отправлено')

    def test_get_clients(self):
        url = reverse('clients-list')
        response = self.client.get(url, format='json')
        tag = response.data[0]['tag']
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(tag, 'newone')

    def test_stats(self):
        url = reverse("mailings-stats")
        response = self.client.get(url, format=json)
        data = {'Кол-во рассылок': 1,
                'Детальная информация': {1: {'id рассылки': 1, 'Всего сообщений по рассылке': 1,
                                             'Отправленных': 0, 'Не отправленных': 1}}}

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data, data)
