from django.urls import path
from .views import UserView, UserLoginView,UserLogoutView, GetUserView

urlpatterns = [
    path('users/register/', UserView().as_view(), name = 'user-register'),
    path('users/login/', UserLoginView().as_view(), name = 'user-login'),
    path('users/profile/',GetUserView().as_view(), name='user-profile'),
    path('users/update/',UserView().as_view(), name='user-update'),
    path('users/logout/', UserLogoutView().as_view(), name='user-logout'),
]