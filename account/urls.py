from django.urls import path, include
from django.contrib.auth import views as auth_views

from . import views

app_name = 'account'
urlpatterns = [
    path('admin_dashboard/', views.AdminDashboard.as_view(), name='admin_dashboard'),
    path('customer_dashboard/', views.CustomerDashboard.as_view(), name='customer_dashboard'),
    path("logout/", auth_views.LogoutView.as_view(next_page="/login/"), name="logout"),
]