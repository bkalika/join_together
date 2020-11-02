from rest_framework import serializers

from .models import UserNet


class GetUserNetSerializer(serializers.ModelSerializer):
    """Output information about a user"""
    avatar = serializers.ImageField(read_only=True)

    class Meta:
        model = UserNet
        exclude = ('password',
                   'last_login',
                   'is_active',
                   'is_staff',
                   'is_superuser',
                   'groups',
                   'user_permissions'
                   )


class GetUserNetPublicSerializer(serializers.ModelSerializer):
    """Output information about a public user"""

    class Meta:
        model = UserNet
        exclude = ('email',
                   'password',
                   'phone',
                   'last_login',
                   'is_active',
                   'is_staff',
                   'is_superuser',
                   'groups',
                   'user_permissions'
                   )
