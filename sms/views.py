from rest_framework.viewsets import ModelViewSet
from .models import Client, Message, Mailing
from .serializers import ClientListSerializer, MessageListSerializer, MailingListSerializer


class ClientViewSet(ModelViewSet):
    serializer_class = ClientListSerializer
    queryset = Client.objects.all()


class MessageViewSet(ModelViewSet):
    serializer_class = MessageListSerializer
    queryset = Message.objects.all()


class MailingViewSet(ModelViewSet):
    serializer_class = MailingListSerializer
    queryset = Mailing.objects.all()
