from rest_framework import serializers

from student.models import AccountStatistics
from .models import Group, Test, Question, Boss


class GroupSerializer(serializers.ModelSerializer):
    class Meta:
        model = Group
        fields = ('id', 'owner', 'owner_name', 'group_name', 'login', 'password')

class ParticipantSerializer(serializers.ModelSerializer):
    class Meta:
        model = AccountStatistics
        fields = ('balance', 'score', 'experience', 'lvl')


class TestSerializer(serializers.ModelSerializer):
    class Meta:
        model = Test
        fields = '__all__'


class QuestionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Question
        fields = '__all__'


class BossSerializer(serializers.ModelSerializer):
    class Meta:
        model = Boss
        fields = '__all__'
