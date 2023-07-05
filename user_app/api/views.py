from django.shortcuts import render
from rest_framework import response
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework.generics import GenericAPIView
from rest_framework.parsers import MultiPartParser, FormParser
from rest_framework_simplejwt.tokens import RefreshToken

from .serializers import (UserResponseSerializer,
                          CreateUserSerializer,
                          UpdateUserSerializer,
                          UserLoginSerializer,
                          )
from .controller import UserController
from rest_framework import status


# Create your views here.

class UserView(GenericAPIView):
    parser_classes = [MultiPartParser, FormParser]

    def get_permission_class(self):
        if self.request.method == 'POST':
            return AllowAny
        elif self.request.method == 'PATCH':
            return IsAuthenticated
        # For any other request methods, deny permission by default
        return None

    def get_serializer_class(self):
        if self.request.method == 'POST':
            return CreateUserSerializer
        if self.request.method == 'PATCH':
            return UpdateUserSerializer
        if self.request.method == 'GET':
            return UserResponseSerializer

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        return response.Response(
            {
                "msg": "User Created Successfully",
                **serializer.validated_data,
            },
            status=status.HTTP_201_CREATED
        )

    def patch(self, request, *args, **kwargs):
        user_id = request.user.id
        serializer = self.get_serializer(data = request.data, context = {'user_id':user_id})
        serializer.is_valid(raise_exception=True)
        return response.Response(
            {
                "msg":" User updated successfully",
                **serializer.validated_data,
            },
            status=status.HTTP_202_ACCEPTED
        )



class UserLoginView(GenericAPIView):
    serializer_class = UserLoginSerializer

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        return response.Response(
            {
                "msg": "Login Successful",
                **serializer.validated_data,
            },
            status=status.HTTP_202_ACCEPTED
        )


class LogoutView(GenericAPIView):
    authentication_classes = [JWTAuthentication]

    def post(self, request):
        try:
            refresh_token = request.data["refresh"]
            token = RefreshToken(refresh_token)
            token.blacklist()
            return response.Response({"msg": "Logout Successful"}, status=status.HTTP_200_OK)
        except Exception as e:
            return response.Response(
                {"msg": "Invalid refresh token"}, status=status.HTTP_400_BAD_REQUEST
            )
