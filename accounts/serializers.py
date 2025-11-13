from rest_framework import serializers
from django.contrib.auth.models import User
from django.contrib.auth.hashers import make_password

class RegisterSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)
    confirm_password = serializers.CharField(write_only=True)
    class Meta:
        model = User
        fields = ['username', 'email', 'password', 'confirm_password']

    def validate(self, data):
        confirm = data.pop("confirm_password")
        password = data.pop("password")
        if confirm != password:
            raise serializers.ValidationError("passwords don't match")
        data["password"] = make_password(password)
        return super().validate(data)

class LoginSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = "__all__"

