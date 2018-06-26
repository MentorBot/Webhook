from rest_framework import serializers
from MenteeRequests.models import MenteeRequests

class MenteeRequestsSerializer(serializers.ModelSerializer):
    """Serializer to map the Model instance into JSON format."""
    class Meta:
        """Meta class to map serializer's fields with the model fields."""
        model = MenteeRequests
        fields = '__all__' # all model fields will be included
        read_only_fields = ('date_created', 'date_modified')
