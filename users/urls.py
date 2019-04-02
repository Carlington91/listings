from django.urls import path
from django.contrib.auth import views as auth_views
from .views import UserRegistration

urlpatterns = [
    path('register/', UserRegistration.as_view(), name="register"),
    path('login/', auth_views.LoginView.as_view(template_name="login.html"), name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name="logout"),
]


# path('shop/<slug:category_slug>/', <view name >, name)
