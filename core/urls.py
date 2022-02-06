from django.urls import path
from .views import *

app_name = "HMS"
urlpatterns = [
    path("", HomeView.as_view(), name="index"),
    path("/signup", SignUpView.as_view(), name="signup"),
    path("login", LoginView.as_view(), name="login")
]