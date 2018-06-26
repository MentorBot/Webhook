from rest_framework import serializers
from MentorDetails.models import MentorProfile, MentorUser


class MentorProfileSerializer(serializers.ModelSerializer):
    """Serializer to map the Model instance into JSON format."""

    class Meta:
        """Meta class to map serializer's fields with the model fields."""
        model = MentorProfile
        fields = '__all__' # all model fields will be included
        read_only_fields = ('date_created', 'date_modified')

class MentorUserSerializer(serializers.ModelSerializer):
    """Serializer to map the Model instance into JSON format."""

    def create(self, validated_data):
            user = MentorUser(
                username=validated_data.get('username', None)
            )
            user.set_password(validated_data.get('password', None))
            user.save()
            return user

    def update(self, instance, validated_data):
            for field in validated_data:
                if field == 'password':
                    instance.set_password(validated_data.get(field))
                else:
                    instance.__setattr__(field, validated_data.get(field))
            instance.save()
            return instance

    class Meta:
        """Meta class to map serializer's fields with the model fields."""
        model = MentorUser
        fields = '__all__' # all model fields will be included
        read_only_fields = ('date_created', 'date_modified')
