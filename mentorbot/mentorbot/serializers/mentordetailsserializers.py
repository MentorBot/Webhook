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

    email = serializers.EmailField(
        required=True,
        validators=[UniqueValidator(queryset=MentorUser.objects.all())]
    )
    first_name = serializers.CharField(required=True)
    last_name = serializers.CharField(required=True)
    password = serializers.CharField(min_length=8, write_only=True)

    def create(self, validated_data):
        user = MentorUser.objects.create_user(validated_data['email'])
        user.set_password(validated_data['password'])
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
        fields = '__all__'  # all model fields will be included
        write_only_fields = ('password',)
        read_only_fields = ('last_login', 'is_active',
                            ' date_created', 'date_modified')
