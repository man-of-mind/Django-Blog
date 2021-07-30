from django.contrib.auth import views
from django.urls import path
from .views import UserEditView, UserRegisterView, PasswordsChangeView, password_sucess

urlpatterns = [
   path('register/', UserRegisterView.as_view(), name="register"),
   path('edit_profile/', UserEditView.as_view(), name="edit-profile"),
   path('password/', PasswordsChangeView.as_view()),
   path('password_sucess/', password_sucess, name="password_success"),
]