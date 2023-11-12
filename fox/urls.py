from django.urls import path
from . import views

urlpatterns = [
    path("login/", views.LoginJWTView.as_view()),
    path('create_user/', views.UserProfileCreateView.as_view(), name='create-user'),
    path('list_users/', views.UserProfileListView.as_view(), name='list-users')
]
