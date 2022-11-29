from django.contrib.auth.password_validation import validate_password
from rest_framework.exceptions import ValidationError
from rest_framework.fields import EmailField, CharField
from rest_framework.serializers import ModelSerializer, Serializer
from rest_framework.validators import UniqueValidator
from rest_framework_simplejwt.serializers import (
    TokenObtainPairSerializer as TokenObtainPairSerializerJWT,
)
from apps.accounts.models import User


class UserSerializer(ModelSerializer):
    class Meta:
        model = User
        fields = ["email", "name"]


class TokenObtainPairSerializer(TokenObtainPairSerializerJWT):
    @classmethod
    def get_token(cls, user):
        token = super().get_token(user)

        token["email"] = user.email
        return token


class RegisterSerializer(ModelSerializer):
    email = EmailField(
        required=True, validators=[UniqueValidator(
            queryset=User.objects.all())]
    )

    password = CharField(write_only=True, required=True,
                         validators=[validate_password])
    password2 = CharField(write_only=True, required=True)

    class Meta:
        model = User
        fields = (
            "password",
            "password2",
            "email",
            "name",
        )
        extra_kwargs = {
            "name": {"required": True},
        }

    def validate(self, attrs):
        if attrs["password"] != attrs["password2"]:
            raise ValidationError(
                {"password": "Password fields didn't match."}
            )

        return attrs

    def create(self, validated_data):
        user = User.objects.create(
            email=validated_data["email"],
            name=validated_data["name"],
        )

        user.set_password(validated_data["password"])
        user.save()

        return user


class LogoutSerializer(Serializer):
    refresh_token = CharField(write_only=True, required=True)
