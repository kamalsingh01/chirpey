from django.db import IntegrityError
from rest_framework import serializers
from user_app.models import UserModel
from .repository import UserRepository
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework import status


class UserController:

    @staticmethod
    def create_user(attrs):
        try:
            response = UserRepository.create_user(attrs=attrs)
        except IntegrityError:
            raise serializers.ValidationError({"msg": "User already Exist"})
        return response

    @staticmethod
    def update_user(attrs,user_id):
        try:
            user = UserModel.objects.get(id = user_id)
            response = UserRepository.update_user(attrs,user_id)
            return response
        except UserModel.DoesNotExist:
            raise serializers.ValidationError({"error": "Not a Valid user request"})
        except IntegrityError:
            raise serializers.ValidationError({"error": "User already Exists"})

    @staticmethod
    def get_user(email, user_id = None):
        try:
            if user_id:
                response = UserRepository.get_user(email, user_id)
            else:
                try:
                    response = UserRepository.get_user(email, user_id)
                except Exception as e:
                    raise serializers.ValidationError({"error": "User not authorised"})
            return response
        except UserModel.DoesNotExist:
            raise serializers.ValidationError({"error": "User Doesn't Exist"})

    @staticmethod
    def user_login(attrs):
        try:
            user = UserRepository.get_user(email=attrs['email'])
            if user.check_password(attrs['password']):
                refresh = RefreshToken.for_user(user)
                return {
                    "token": {
                        "refresh": str(refresh),
                        "access": str(refresh.access_token)
                    }
                }
            else:
                raise serializers.ValidationError({"error": "Incorrect Password"})
        except UserModel.DoesNotExist:
            raise serializers.ValidationError({"error": "User Doesn't Exist"})
