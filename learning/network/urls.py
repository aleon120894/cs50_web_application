from django.urls import path
from . import views


urlpatterns = [
    path("", views.index, name="index"),
    path('add/', views.add_post, name='add_post'),
    path("login/", views.login_view, name="login"),

    path("logout/", views.logout_view, name="logout"),
    path("register/", views.register, name="register"),
    path("account_page/", views.account_page, name="account_page"),
]
