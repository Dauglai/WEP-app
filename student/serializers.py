from rest_framework import serializers

from student.models import Account_Statistics


class StatisticsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Account_Statistics
        fields = '__all__'
