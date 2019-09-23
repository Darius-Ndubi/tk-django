from rest_framework import status
from rest_framework.generics import CreateAPIView
from rest_framework.permissions import AllowAny
from rest_framework.response import Response

from .serializers import (
    UserSignUpSerializer, UserSignInSerializer
)

"""
 View to signup users
"""


class SignUpAPIView(CreateAPIView):
    # Set up permissions for this view
    permission_classes = [AllowAny]
    serializer_class = UserSignUpSerializer

    def post(self, request):
        # new_user = request.data
        serializer = self.serializer_class(data=request.data)

        # Validate date or raise exceptions
        serializer.is_valid(raise_exception=True)
        serializer.save()

        # User response upon successful registration
        response_message = {
            "message": " You have been successfully Registered, Proceed to login"
        }

        return Response(response_message, status=status.HTTP_201_CREATED)

"""
 View to signin users
"""


class SignInAPIView(CreateAPIView):
    # Set up permissions for this view
    permission_classes = [AllowAny]
    serializer_class = UserSignInSerializer

    def post(self, request):
        # login_user = request.data
        serializer = self.serializer_class(data=request.data)

        # Validate date or raise exceptions
        serializer.is_valid(raise_exception=True)

        return Response(serializer.data, status=status.HTTP_200_OK)
