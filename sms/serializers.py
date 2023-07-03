from .models import Client, Message, Mailing
from rest_framework import serializers


class ClientListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Client
        fields = '__all__'


class MessageListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Message
        fields = '__all__'


class MailingListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Mailing
        fields = '__all__'
