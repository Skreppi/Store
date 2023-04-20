from django.urls import path

from .views import (EmailVerificationView, LoginUser, LogoutUser,
                    ProfileUserForm, RegistrationUserForm)

urlpatterns = [
    path('login/', LoginUser, name='login'),
    path('logout/', LogoutUser, name='logout'),
    path('registration/', RegistrationUserForm.as_view(), name='regist'),
    path('verify/<str:email>/<uuid:code>/', EmailVerificationView.as_view(), name='email_verification'),
    path('profile/<int:pk>/', ProfileUserForm.as_view(), name='profile'),
]
