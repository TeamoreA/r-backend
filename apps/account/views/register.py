from rest_framework import status
from rest_framework.generics import GenericAPIView
from rest_framework.permissions import AllowAny
from rest_framework.request import Request
from rest_framework.response import Response

from apps.account.serializers import RegistrationSerializer
from helpers.renderers import UserJSONRenderer


class RegisterAPIView(GenericAPIView):
    """View to register a new user"""

    permission_classes = (AllowAny,)
    renderer_classes = (UserJSONRenderer,)
    serializer_class = RegistrationSerializer
    operation = "Register"

    def post(self, request: Request, **kwargs) -> Response:
        """Post method to register a user"""
        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()

        return Response(
            {
                "message": "Hello {}, You have been successfully registered".format(
                    request.data.get("username")
                ),
                "status": "success",
                "data": {
                    "username": request.data.get("username"),
                    "email": request.data.get("email"),
                },
            },
            status=status.HTTP_201_CREATED,
        )
