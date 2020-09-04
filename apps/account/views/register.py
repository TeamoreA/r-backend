from apps.account.serializers import RegistrationSerializer
from rest_framework.generics import GenericAPIView
from rest_framework.permissions import AllowAny
from helpers.renderers import DefaultJSONRenderer
from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework import status

class RegisterAPIView(GenericAPIView):
    """View to register a new user"""
    permission_classes =  (AllowAny,)
    renderer_classes = (DefaultJSONRenderer,)
    serializer_class = RegistrationSerializer
    operation = "Register"

    def post(self, request: Request, **kwargs) -> Response:
        """Post method to register a user"""
        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()

        return Response(
            {
                "message": "Hello {}, You have ben successfully registered".format(request.data.get('username'))
            },
            status=status.HTTP_201_CREATED,
        )


