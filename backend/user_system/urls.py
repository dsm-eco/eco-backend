from django.urls import path

from user_system import views

urlpatterns = [
    path('register/', views.create_user),
]
