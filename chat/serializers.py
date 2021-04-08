from .models import Message
from rest_framework import serializers


class MessagesListSerializer(serializers.ModelSerializer):

    class Meta:
        model = Message
        fields = "__all__"


class MessageDetailSerializer(serializers.ModelSerializer):

    class Meta:
        model = Message
        fields = '__all__'


class MessageCreateSerializer(serializers.ModelSerializer):

    class Meta:
        model = Message
        fields = '__all__'
