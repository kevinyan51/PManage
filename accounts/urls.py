from django.urls import path
from accounts.views import Login, Logout, signup

urlpatterns = [
    path("login/", Login, name="login"),
    path("logout/", Logout, name="logout"),
    path("signup/", signup, name="signup"),
]
