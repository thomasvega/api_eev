from django.urls import path

from . import views

urlpatterns = [
    path('', views.login_page, name='login_page'),
    path('register/', views.register_page, name='register'),
    path('password_forgot/', views.password_forgot, name='password_forgot'),
    # HOME  
    path('home/', views.home, name="home"),
    # EVENT
    path('event/', views.event, name="event_create"),
]