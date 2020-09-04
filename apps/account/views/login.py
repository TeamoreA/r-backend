from django.utils.timezone import now
from rest_framework import status
from rest_framework.generics import GenericAPIView
from rest_framework.permissions import AllowAny
from rest_framework.request import Request
from rest_framework.response import Response

from apps.account.backends import JWTAuthentication
# from apps.account.models import User
from django.contrib.auth.models import User
from helpers.renderers import DefaultJSONRenderer
from apps.account.serializers import LoginSerializer


class LoginAPIView(GenericAPIView):
    permission_classes = (AllowAny,)
    serializer_class = LoginSerializer
    operation = "Login"
    renderer_classes = (DefaultJSONRenderer,)

    def post(self, request: Request) -> Response:
        """Login a user"""
        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)

        user_data = serializer.data
        username = request.data.get('username', None)
        user = User.objects.get(username=username)
        userdata = {
            "id": user.id,
            "email": user.email,
            "username": user.username,
        }
        token = JWTAuthentication.generate_token(userdata=userdata)
        username = user.username
        # update user last login
        user.last_login = now()
        user.save()

        return Response(
            {
                "message": "Welcome {}".format(username),
                "meta": {"token": token, "username": username},
            },
            status=status.HTTP_200_OK,
        )
