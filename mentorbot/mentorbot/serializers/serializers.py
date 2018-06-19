from rest_framework import serializers
from MenteeRequests.models import MenteeRequests
from bot.models import Bot
from MentorshipFields.models import MentorshipFields
from MentorRequests.models import MentorRequests

class BotSerializer(serializers.ModelSerializer):
     """Serializer to map the Model instance into JSON format."""
     class Meta:
         """Meta class to map serializer's fields with the model fields."""
         model = Bot
         fields = '__all__' # all model fields will be included
         read_only_fields = ('date_created')


class MentorRequestsSerializer(serializers.ModelSerializer):
    """Serializer to map the Model instance into JSON format."""
    class Meta:
        """Meta class to map serializer's fields with the model fields."""
        model = MenteeRequests
        fields = '__all__' # all model fields will be included
        read_only_fields = ('date_created', 'date_modified')


class MentorshipFieldsSerializer(serializers.ModelSerializer):
    """Serializer to map the Model instance into JSON format."""
    class Meta:
        """Meta class to map serializer's fields with the model fields."""
        model = MentorshipFields
        fields = '__all__' # all model fields will be included

class MenteeRequestsSerializer(serializers.ModelSerializer):
    """Serializer to map the Model instance into JSON format."""
    class Meta:
        """Meta class to map serializer's fields with the model fields."""
        model = MenteeRequests
        fields = '__all__' # all model fields will be included
        read_only_fields = ('date_created', 'date_modified')
