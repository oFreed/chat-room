from .models import Message
from .serializers import MessageCreateSerializer, MessageDetailSerializer, MessagesListSerializer
from rest_framework import viewsets
from django_filters.rest_framework import DjangoFilterBackend
from .service import MessageFilter, PaginationMessages


class MessageViesSet(viewsets.ReadOnlyModelViewSet):
    """Method to get list of message and information about message"""
    filter_backends = (DjangoFilterBackend,)
    filterset_class = MessageFilter
    pagination_class = PaginationMessages

    def get_queryset(self):
        message = Message.objects.all()
        return message
    """Function to choose Serializer(which API methods to use)"""
    def get_serializer_class(self):
        if self.action == 'list':
            return MessagesListSerializer
        elif self.action == 'retrieve':
            return MessageDetailSerializer


class MessageCreateViewSet(viewsets.ModelViewSet):
    """Method to create new message"""
    serializer_class = MessageCreateSerializer
