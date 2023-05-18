from rest_framework import serializers
from .models import Group, Test


class GroupSerializer(serializers.ModelSerializer):
    class Meta:
        model = Group
        fields = ('owner', 'owner_name', 'group_name', 'login', 'password')


class TestsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Test
        fields = '__all__'





