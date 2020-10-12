from collections import OrderedDict
from typing import Dict

from django.contrib.auth import authenticate
from rest_framework import serializers

from ..backends import JWTAuthentication


class LoginSerializer(serializers.Serializer):
    """The class to serialize login details"""

    username = serializers.CharField(max_length=255)
    password = serializers.CharField(max_length=128, write_only=True)

    def validate(self, data: OrderedDict) -> Dict[str, str]:
        """
        validate details
        """
        username = data.get("username", None)
        password = data.get("password", None)

        if not password:
            raise serializers.ValidationError("Kindly enter your password to log in.")
        elif not username:
            raise serializers.ValidationError("Kindly enter your username to login")
        auth_user = authenticate(username=username, password=password)

        if auth_user is None:
            raise serializers.ValidationError(
                {"error": "Kindly enter the correct username and password"}
            )
        token = JWTAuthentication.generate_token(username)

        return {"username": auth_user.username, "token": token}
