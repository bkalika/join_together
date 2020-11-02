from rest_framework import serializers

from .models import UserNet


class GetUserNetSerializer(serializers.ModelSerializer):
    """Output information about a user"""

    class Meta:
        model = UserNet
        exclude = ('password', 'last_login', 'is_active', 'is_staff', 'is_superuser')
