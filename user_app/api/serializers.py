from rest_framework import serializers
from user_app.models import UserModel
from .controller import UserController


class UserResponseSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserModel
        fields = ['id', 'first_name', 'last_name', 'username', 'email', 'bio', 'profile_image']


class CreateUserSerializer(serializers.Serializer):
    first_name = serializers.CharField(max_length=50, required=True)
    last_name = serializers.CharField(max_length=50, required=True)
    username = serializers.CharField(max_length=20, required=True)
    email = serializers.CharField(max_length=20, required=True)
    bio = serializers.CharField(max_length=100, required=False)
    password = serializers.CharField(
        style={
            "input_type": "password"
        }, write_only=True, required=True
    )
    password2 = serializers.CharField(
        style={
            "input_type": "password"
        }, write_only=True, required=True
    )

    def validate(self, attrs):
        if attrs['password'] != attrs['password2']:
            raise serializers.ValidationError({"error": "Password and password2 must match"})
        else:
            attrs.pop("password2", None)
            response = UserController.create_user(attrs=attrs)
        return response


class UpdateUserSerializer(serializers.Serializer):

    first_name = serializers.CharField(max_length=50, required = False)
    last_name = serializers.CharField(max_length=50, required = False)
    username = serializers.CharField(max_length=20, required=False)
    email = serializers.CharField(max_length=20, required=False)
    bio = serializers.CharField(max_length=100, required=False)
    profile_image = serializers.ImageField(required=False)
    password = serializers.CharField(
        style={
            "input_type": "password"
        }, write_only=True, required=False
    )

    def validate(self, attrs):
        user_id = self.context.get('user_id')
        response = UserController.update_user(attrs,user_id)
        return response


class UserLoginSerializer(serializers.Serializer):
    email = serializers.EmailField(required=True)
    password = serializers.CharField(
        style={
            "input_type": "password"
        }, write_only=True
    )

    def validate(self, attrs):
        response = UserController.user_login(attrs=attrs)
        return response
