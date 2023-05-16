from rest_framework import serializers
from .models import Group


class GroupSerializer(serializers.ModelSerializer):
    class Meta:
        model = Group
        fields = ('owner', 'owner_name', 'group_name', 'login', 'password')
