from django.urls import path
from .views import UserView, UserLoginView,UserLogoutView, GetUserView

urlpatterns = [
    path('register/', UserView().as_view(), name = 'user-register'),
    path('login/', UserLoginView().as_view(), name = 'user-login'),
    path('profile/',GetUserView().as_view(), name='user-profile'),
    path('update/',UserView().as_view(), name='user-update'),
    path('logout/', UserLogoutView().as_view(), name='user-logout'),
]