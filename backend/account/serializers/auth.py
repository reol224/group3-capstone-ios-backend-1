import re
from django.contrib.auth.models import User
from rest_framework import serializers
from rest_framework.validators import UniqueValidator
from backend.account.utils.password_check import password_check


class LoginSerializer(serializers.Serializer):
    email = serializers.CharField(
        label='account', max_length=254, required=True)
    password = serializers.CharField(
        label='password', max_length=128, required=True)


class SignUpSerializer(serializers.Serializer):
    email = serializers.EmailField(
        label='account', validators=[UniqueValidator(queryset=User.objects.all())], required=True)
    password = serializers.CharField(
        label='password', max_length=128, required=True)
    first_name = serializers.CharField(
        label='first_name', max_length=30, required=True)
    last_name = serializers.CharField(
        label='last_name', max_length=20, required=False, allow_null=True, allow_blank=True)
    accept = serializers.CharField(
        label='accept', max_length=20, required=False, allow_null=True, allow_blank=True)

    def validate(self, user):
        if not password_check(user.get('password')):
            raise serializers.ValidationError(
                {"password": "密码太弱鸡，长度至少8位，至少包含1个数字，1个大写字母，1个小写字母和一个特殊符号(这些中的一个: !#$%&'()*+,-./\\^_`{|}~)"})
        return user

    def create(self, validated_data):
        username = validated_data['email']
        password = validated_data['password']
        email = validated_data['email']
        first_name = validated_data['first_name']
        last_name = validated_data['last_name']

        user = User(username=username, password=password, is_active=True,
                    email=email, first_name=first_name, last_name=last_name)
        user.set_password(password)
        user.save()

        return user
