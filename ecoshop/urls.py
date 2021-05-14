from django.urls import path

from ecoshop import views

urlpatterns = [
    path('list/', views.ecoshop_list),
]
