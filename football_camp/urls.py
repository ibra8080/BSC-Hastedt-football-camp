from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
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
]