from django.urls import path
from .views import LoginView, LogoutView, RegisterView, dashboard, RefreshTokenView

urlpatterns = [
    path('login/', LoginView.as_view(), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('register/', RegisterView.as_view(), name="register"),
    path('refresh/', RefreshTokenView.as_view(), name="refresh"),
    path("", dashboard, name="dashboard"),

]


# path('register/', RegisterView.as_view(), name="register"),
