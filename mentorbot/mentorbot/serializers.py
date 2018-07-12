from rest_framework import serializers
from MenteeRequests.models import MenteeRequests
from MentorDetails.models import MentorDetails
from bot.models import Bot
from MentorshipFields.models import MentorshipFields


class BotSerializer(serializers.ModelSerializer):
    """Serializer to map the Model instance into JSON format."""
    class Meta:
        """Meta class to map serializer's fields with the model fields."""
        model = Bot
        fields = ('field_name')
        read_only_fields = ('date_created')


class MentorDetailsSerializer(serializers.ModelSerializer):
    """Serializer to map the Model instance into JSON format."""

    class Meta:
        """Meta class to map serializer's fields with the model fields."""
        model = MentorDetails
        fields = ('name', 'phone_number', 'email', 'linkdin', 'github',
                  'facebook', 'twitter', 'mentor_status', 'mentorship_field',
                  'short_bio', 'date_created', 'date_modified')
        read_only_fields = ('date_created', 'date_modified')


class MentorRequestsSerializer(serializers.ModelSerializer):
    """Serializer to map the Model instance into JSON format."""
    class Meta:
        """Meta class to map serializer's fields with the model fields."""
        model = MenteeRequests
        fields = ('mentor_name', 'mentor_approved',
                  'requested_mentorship_field', 'request_status',
                  'date_created', 'date_modified')
        read_only_fields = ('date_created', 'date_modified')


class MentorshipFieldsSerializer(serializers.ModelSerializer):
    """Serializer to map the Model instance into JSON format."""
    class Meta:
        """Meta class to map serializer's fields with the model fields."""
        model = MentorshipFields
        fields = ('name')


class MenteeRequestsSerializer(serializers.ModelSerializer):
    """Serializer to map the Model instance into JSON format."""
    class Meta:
        """Meta class to map serializer's fields with the model fields."""
        model = MenteeRequests
        fields = ('mentee_name', 'requested_mentorship_field',
                  'request_status', 'date_created', 'date_modified')
        read_only_fields = ('date_created', 'date_modified')
