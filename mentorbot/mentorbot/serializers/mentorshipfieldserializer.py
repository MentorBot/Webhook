from rest_framework import serializers
from MentorshipFields.models import MentorshipFields


class MentorshipFieldsSerializer(serializers.ModelSerializer):
    """Serializer to map the Model instance into JSON format."""
    class Meta:
        """Meta class to map serializer's fields with the model fields."""
        model = MentorshipFields
        fields = '__all__' # all model fields will be included
