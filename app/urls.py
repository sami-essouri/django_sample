

from django.urls import path

from . import views

urlpatterns = [
    path("", views.Index.as_view(), name="index"),
    path("accounts/profile/", views.AccountProfile.as_view(), name="profile"),
    path('<pk>/delete/', views.UserDeleteView.as_view(), name="delete"),
    path("register/", views.register_request, name="register")
]