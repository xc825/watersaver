from django.urls import path
from django.conf.urls import include
from django.contrib.auth import views as auth_views
from django.conf import settings
from . import views

app_name = "water"

urlpatterns = [
    path("", views.index, name="index"),
    path("property/<int:property_id>/", views.property, name="property"),
    path("property_create/", views.property_create, name="property_create"),
    path("property/<int:property_id>/residents/", views.residents, name="residents"),
    path("property/<int:property_id>/resident_add/", views.resident_add, name="resident_add"),
    path("user/<int:user_id>/", views.user, name="user"),
    path("user_create/", views.user_create, name="user_create"),
    path("accounts/", include("django.contrib.auth.urls")),
    path("login/", auth_views.LoginView.as_view(template_name="water/login.html")),
    path('logout/', auth_views.LogoutView.as_view(next_page=settings.LOGOUT_REDIRECT_URL), name='logout'),
    path("accounts/profile", views.user, name="profile")
]

