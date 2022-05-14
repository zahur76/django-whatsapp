from rest_framework import serializers
from .models import User, UserMessage

class MessageSerializer(serializers.ModelSerializer):
    faction_name = serializers.ReadOnlyField(source='faction.name')
    class Meta:
        model = UserMessage
        fields = ('id', 'created_at', 'user', 'user_two', 'sender', 'message', 'message_read')
