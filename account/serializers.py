from rest_framework import serializers
from .models import User, Account


# class UserRegistrSerializer(serializers.ModelSerializer):
#     password2 = serializers.CharField()
#     class Meta:
#         model = Account
#         fields = ['email', 'username', 'password', 'password2']


class AccountSerializer(serializers.ModelSerializer):
    password2 = serializers.CharField()

    class Meta:
        model = Account
        # fields = ('id', 'last_name', 'first_name', 'patronymic', 'location', 'school_number', 'password',
        #           'password2', 'email', 'is_teacher', 'gender', 'is_staff', 'is_admin', 'is_superuser')
        fields = ['email', 'password', 'password2']

    def save(self, *args, **kwargs):
        user = Account(
            # last_name=self.validated_data['last_name'],
            # first_name=self.validated_data['first_name'],
            # patronymic=self.validated_data['patronymic'],
            # location=self.validated_data['location'],
            # school_number=self.validated_data['school_number'],
            email=self.validated_data['email'],
            # is_teacher=self.validated_data['is_teacher'],
            # gender=self.validated_data['gender'],
            # username=self.validated_data['username'],
        )
        password = self.validated_data['password']
        password2 = self.validated_data['password2']
        if password != password2:
            raise serializers.ValidationError({password: "Пароль не совпадает"})
        user.set_password(password)
        user.save()
        return user
