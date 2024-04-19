from django.urls import path
from django.contrib.auth import views as auth_views
from . import views


app_name = "authentication"


urlpatterns = [
    path(
        "login",
        auth_views.LoginView.as_view(template_name="authentication/login.html"),
        name="login",
    ),
    path(
        "logout",
        views.logout_user,
        name="logout",
    ),
    path("signup", views.signup, name="signup"),
    # path('signup', auth_views.LoginView.as_view(template_name='authentication/signup.html'), name='signup'),
    path("check_who_loggedin", views.check_who_loggedin, name="check_who_loggedin"),
]
