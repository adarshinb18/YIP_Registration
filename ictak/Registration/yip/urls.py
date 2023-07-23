from django.urls import path
from . import views

urlpatterns = [
    path('', views.registration_view, name='registration'),
    # # path('otp-verification/', views.otp_verification, name='otp_verification'),
    # path('profile-update/', views.profile_update_view, name='profile_update'),
    path("otp_verification",views.api_check_otp_view,name="api_check_otp_view"),
    path("update",views.update_data_view,name="update_data"),
    path("login",views.login_view,name="login")
]