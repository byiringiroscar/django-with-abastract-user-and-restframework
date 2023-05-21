from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)
from django.contrib.auth import views as auth_views
from . import views
# from .views import Register, LoginView, UserView

from django.urls import path

urlpatterns = [
    path('', views.home, name='home'),
    path('login', views.login, name='login'),
    path('loginn/', auth_views.LoginView.as_view(template_name='login.html')),
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('register_api', views.registration_user, name='register_api'),
    #     path('register', Register.as_view()),
    #     path('login', LoginView.as_view()),
    #     path('user', UserView.as_view()),
]
