from django.urls import  path
from .views import UserView, UserLoginView

urlpatterns = [
    path('register/', UserView().as_view(), name = 'user-view'),
    path('login/', UserLoginView().as_view(), name = 'user-login'),
]