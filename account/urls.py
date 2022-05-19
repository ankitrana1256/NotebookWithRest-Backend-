from django.urls import path
from account.views import UserRegistrationView, UserLoginView, UserProfileView, UserChangePasswordView, SendPasswordResetEmailView,UserPasswordResetView

urlpatterns = [
    path('register/', UserRegistrationView.as_view(),name="register"),
    path('login/', UserLoginView.as_view(), name="login"),
    path('profile/', UserProfileView.as_view(), name="profile"),
    path('changepassword/', UserChangePasswordView.as_view(), name="changepwd"),
    path('send-reset-email/', SendPasswordResetEmailView.as_view(), name="send-email"),
    path('reset/<uid>/<token>/', UserPasswordResetView.as_view(), name="reset")
]

