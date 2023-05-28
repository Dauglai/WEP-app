from rest_framework import serializers

from student.models import AccountStatistics, Hero, Protagonist


class StatisticsSerializer(serializers.ModelSerializer):
    class Meta:
        model = AccountStatistics
        fields = '__all__'


class HeroSerializer(serializers.ModelSerializer):
    class Meta:
        model = Hero
        fields = '__all__'


class ProtagonistSerializer(serializers.ModelSerializer):
    class Meta:
        model = Protagonist
        fields = '__all__'

