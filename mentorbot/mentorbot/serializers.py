from rest_framework import serializers
from .models import MentorshipFields, MentorDetails, MenteeRequestNewMentorshipField, NewMentorshipFieldRequest
class MentorDetailsSerializer(serializers.ModelSerializer):
    """Serializer to map the Model instance into JSON format."""

    class Meta:
        """Meta class to map serializer's fields with the model fields."""
        model = MentorDetails
        fields = ('name', 'phone_number', 'email', 'linkdin', 'github', 'facebook', 'twitter', 'mentor_status', 'mentorship_field', 'mentorship_details', 'date_created', 'date_modified')
        read_only_fields = ('date_created', 'date_modified')

class MentorshipFieldsSerializer(serializers.ModelSerializer):
    """Serializer to map the Model instance into JSON format."""
    class Meta:
        """Meta class to map serializer's fields with the model fields."""
        model = MentorshipFields
        fields = ('name')

class NewMentorshipFieldRequestSerializer(serializers.ModelSerializer):
    """Serializer to map the Model instance into JSON format."""
    class Meta:
        """Meta class to map serializer's fields with the model fields."""
        model = NewMentorshipFieldRequest
        fields = ('requester_name', 'requester_approved', 'requested_mentorship_field', 'request_status', 'date_created', 'date_modified')
        read_only_fields = ('date_created', 'date_modified')

class MenteeRequestNewMentorshipFieldSerializer(serializers.ModelSerializer):
    """Serializer to map the Model instance into JSON format."""
    class Meta:
        """Meta class to map serializer's fields with the model fields."""
        model = MenteeRequestNewMentorshipField
        fields = ('mentee_name', 'requested_mentorship_field', 'request_status','date_created', 'date_modified')
        read_only_fields = ('date_created', 'date_modified')
