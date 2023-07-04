from rest_framework.decorators import action
from rest_framework.generics import get_object_or_404
from rest_framework.response import Response
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

    @action(methods=['get'], detail=False)
    def stats(self, request):
        total = Mailing.objects.count()
        mailings = Mailing.objects.values('id')
        context = {
            'Кол-во рассылок': total,
        }
        detail_info = {}
        for mailing in mailings:
            messages = Message.objects.filter(mailing_id=mailing['id']).all()
            sent_messages = messages.filter(status='Отправлено').count()
            dont_sent_messages = messages.filter(status='Не отправлено').count()
            mailing_info = {
                'id рассылки': mailing['id'],
                'Всего сообщений по рассылке': len(messages),
                'Отправленных': sent_messages,
                'Не отправленных': dont_sent_messages
            }
            detail_info[mailing['id']] = mailing_info
        context['Детальная информация'] = detail_info
        return Response(context)

    @action(methods=['get'], detail=True)
    def detstats(self, request, pk=None):
        mailing = Mailing.objects.all()
        get_object_or_404(mailing, pk=pk)
        queryset = Message.objects.filter(mailing_id=pk).all()
        serializer = MessageListSerializer(queryset, many=True)
        return Response(serializer.data)
