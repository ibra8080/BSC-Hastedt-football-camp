from django.urls import path
from django.contrib.auth import views as auth_views
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('services/', views.service_list, name='service_list'),
    path('book_service/', views.book_service, name='book_service'),
    path('admin_create_service/', views.admin_create_service, name='admin_create_service'),
    path('admin_manage_services/', views.admin_manage_services, name='admin_manage_services'),
    path('view_training_schedule/', views.view_training_schedule, name='view_training_schedule'),
    path('manage_players/', views.manage_players, name='manage_players'),
    path('player_profile/<int:player_id>/', views.player_profile, name='player_profile'),
    path('edit_service/<int:service_id>/', views.edit_service, name='edit_service'),
    path('delete_service/<int:service_id>/', views.delete_service, name='delete_service'),
    path('register/', views.register, name='register'),
    path('accounts/login/', auth_views.LoginView.as_view(template_name='registration/login.html'), name='login'),
    path('accounts/logout/', auth_views.LogoutView.as_view(next_page='/'), name='logout'),
    path('user_account/', views.user_account, name='user_account'),
    path('edit_booking/<int:booking_id>/', views.edit_booking, name='edit_booking'),
    path('delete_booking/<int:booking_id>/', views.delete_booking, name='delete_booking'),
    path('service/<int:service_id>/', views.service_page, name='service_page'),
    path('player_added/', views.player_added, name='player_added'),
    path('edit_player/<int:player_id>/', views.edit_player, name='edit_player'),
    path('delete_player/<int:player_id>/', views.delete_player, name='delete_player'),
]
