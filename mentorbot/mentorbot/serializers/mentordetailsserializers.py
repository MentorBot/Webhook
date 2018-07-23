from rest_framework import serializers
from rest_framework.validators import UniqueValidator
from MentorDetails.models import MentorProfile, MentorUser


class MentorProfileSerializer(serializers.ModelSerializer):
    """Serializer to map the Model instance into JSON format."""

    class Meta:
        """Meta class to map serializer's fields with the model fields."""
        model = MentorProfile
        fields = '__all__'  # all model fields will be included
        read_only_fields = ('date_created', 'date_modified')


class MentorUserSerializer(serializers.ModelSerializer):
    """Serializer to map the Model instance into JSON format."""

    class Meta:
        """Meta class to map serializer's fields with the model fields."""
        model = MentorUser
        fields = '__all__'  # all model fields will be included
        write_only_fields = ('password',)
        read_only_fields = ('last_login', 'is_active',
                            ' date_created', 'date_modified')

class TokenSerializer(serializers.Serializer):
        """This serializer serializes the token data"""
        token = serializers.CharField(max_length=255)
