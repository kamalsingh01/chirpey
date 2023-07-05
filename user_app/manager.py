from django.contrib.auth.base_user import BaseUserManager

class UserManager(BaseUserManager):

    def create_user(self,
                    first_name,
                    last_name,
                    email,
                    password,
                    **extra_fields):
        if not email:
            raise ValueError("Email must be provided")
        email = self.normalize_email(email)
        user = self.model(
            first_name = first_name,
            last_name = last_name,
            email = email,
            **extra_fields
        )
        user.set_password(password)
        user.save()
        return user

    def create_superuser(self,
                         first_name,
                         last_name,
                         email,
                         password,
                         **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)
        extra_fields.setdefault('is_active', True)
        return self.create_user(
                    first_name,
                    last_name,
                    email,
                    password,
                    **extra_fields)
