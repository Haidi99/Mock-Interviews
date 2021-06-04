from .api_views import RegisterAPI, LoginAPI, ChangePasswordView, UpdateProfileView
from knox import views as knox_views
from django.urls import path

urlpatterns = [
    path('api/register/', RegisterAPI.as_view(), name='register'),

    path('api/login/', LoginAPI.as_view(), name='login'),
    path('api/logout/', knox_views.LogoutView.as_view(), name='logout'),
    path('api/logoutall/', knox_views.LogoutAllView.as_view(), name='logoutall'),  # law l sha5s 3aml login mn diffrent browsers
    path('api/change_password/<int:pk>/', ChangePasswordView.as_view(), name='auth_change_password'),
    path('api/update_profile/<int:pk>/', UpdateProfileView.as_view(), name='auth_update_profile'),
    
]
