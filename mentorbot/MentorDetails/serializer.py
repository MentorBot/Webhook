from rest_framework import serializers
from .models import MentorDetails


class MentorDetailsSerializer(serializers.ModelSerializer):
    """Serializer to map the Model instance into JSON format."""

    class Meta:
        """Meta class to map serializer's fields with the model fields."""
        model = MentorDetails
        fields = ('name', 'phone_number', 'email', 'linkdin', 'github',
                  'facebook', 'twitter', 'mentor_status', 'mentorship_field',
                  'mentorship_details', 'date_created', 'date_modified')
        read_only_fields = ('date_created', 'date_modified')
