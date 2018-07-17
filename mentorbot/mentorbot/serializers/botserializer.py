from rest_framework import serializers
from bot.models import Bot


class BotSerializer(serializers.ModelSerializer):
    """Serializer to map the Model instance into JSON format."""
    class Meta:
        """Meta class to map serializer's fields with the model fields."""
        model = Bot
        fields = '__all__'  # all model fields will be included
        read_only_fields = ('date_created')
