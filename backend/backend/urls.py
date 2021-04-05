"""backend URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include

from ecoshop.views import EcoShopViewSet

shop_list = EcoShopViewSet.as_view({"get": "list", "post": "create"})
shop_detail = EcoShopViewSet.as_view({"patch": "partial_update", "delete": "destroy"})

urlpatterns = [
    path('admin/', admin.site.urls),
    path('user/', include('user_system.urls')),
    path('shop/', shop_list),
    path('shop/<int:pk>/', shop_detail)
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
