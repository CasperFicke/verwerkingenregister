# users/urls.py

# django
from django.urls import path, include

# local
from . import views
from .views import ShowProfileView, EditProfileView, CreateProfileView

app_name = "users"

urlpatterns = [
  # user
  path('users/login/'          , views.login_user, name="login"),
  path('users/logout/'         , views.logout_user, name="logout"),
  path('users/register/'       , views.register_user, name="register"),
  path('users/edit_settings/'  , views.edit_usersettings, name="edit_usersettings"),
  path('users/change_password/', views.change_password, name="change_password"),
  # userprofile
  path('users/<int:pk>/profile/'     , ShowProfileView.as_view(), name='show-profile'),
  path('users/<int:pk>/edit_profile/', EditProfileView.as_view(), name='edit-profile'),
  path('users/create_profile/'       , CreateProfileView.as_view(), name='create-profile'),
]
