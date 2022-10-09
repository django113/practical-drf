from django.db.models import Q
from rest_framework import serializers, status

from accounts.models import accountUserProfile
from django.contrib.auth import get_user_model

User = get_user_model()
"""
user existing user send to user_slug is matching in 
userprofile then get otherwise create userprofile and return user.
"""


class accountsAdminUserProfileSerializer(serializers.Serializer):
    user_slug = serializers.CharField(max_length=100, required=True)

    def validate(self, data):
        user_slug = data.get("user_slug", None)
        instance_user = User.objects.filter(slug=user_slug)
        if instance_user.exists():
            raise serializers.ValidationError(
                {f"errors": "This" + str(instance_user) + "+ already exists", 'status': status.HTTP_400_BAD_REQUEST})
        else:
            return data

    class Meta:
        fields = "__all__"

    def create(self, validated_data):
        user_slug = validated_data['user_slug']
        user = User.objects.get(slug=user_slug)
        print(user)
        user_profile = accountUserProfile.objects.filter(user_id=user)
        if not user_profile.exists():
            user_profile_create = accountUserProfile.objects.create(user=user)
            print(user_profile_create)

        return validated_data
