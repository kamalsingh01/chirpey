from user_app.models import UserModel
from rest_framework_simplejwt.tokens import RefreshToken


class UserRepository:

    @staticmethod
    def create_user(attrs):
        password = attrs['password']
        attrs.pop("password", None)
        user = UserModel(**attrs)
        user.set_password(password)
        user.save()
        return {}

    @staticmethod
    def update_user(attrs, user_id):
        user = UserModel.objects.get(id=user_id)
        user.first_name = attrs.get('first_name', user.first_name)
        user.last_name = attrs.get('last_name', user.last_name)
        user.username = attrs.get('username', user.username)
        user.email = attrs.get('email', user.email)
        user.bio = attrs.get('bio', user.bio)
        user.profile_image = attrs.get('profile_image', user.profile_image)

        if 'password' in attrs:
            password = attrs['password']
            user.set_password(password)
        user.save()
        # again returning new refresh token so that user stays logged in
        refresh = RefreshToken.for_user(user)

        return {
            # "user": UserResponseSerializer(user).data,
            "token": {
                "refresh": str(refresh),
                "access": str(refresh.access_token),
            },
        }

    @staticmethod
    def get_user(email, user_id=None):
        if user_id:
            return UserModel.objects.get(email=email, id = user_id)
        else:
            return UserModel.objects.get(email=email)
