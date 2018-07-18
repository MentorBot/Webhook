from rest_framework import serializers
from MentorRequests.models import MentorRequests


class MentorRequestsSerializer(serializers.ModelSerializer):
    """Serializer to map the Model instance into JSON format."""
    class Meta:
        """Meta class to map serializer's fields with the model fields."""
        model = MentorRequests
        fields = '__all__'  # all model fields will be included
        read_only_fields = ('date_created', 'date_modified')
