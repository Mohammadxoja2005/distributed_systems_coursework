from django.contrib import admin
from django.urls import path, include
from . import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('admin/', admin.site.urls),
    
    # User Auth
    path('register/', views.register_view, name='register'),
    path('login/', auth_views.LoginView.as_view(template_name='login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    
    # Note CRUD
    path('', views.note_list, name='note_list'),
    path('new/', views.note_create, name='note_create'),
    path('delete/<int:pk>/', views.note_delete, name='note_delete'),
]