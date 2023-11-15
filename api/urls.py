"""api URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
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
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include
from lalafo.views import *
from lalafo.views import create_ad_api
from api import settings
from rest_framework.routers import DefaultRouter
from lalafo.views import AdViewSet
from lalafo.views import ApartmentRentListCreate
from lalafo.views import ApartmentSaleListCreate


router = DefaultRouter()
router.register(r'ads', AdViewSet)


urlpatterns =[
    path('admin/', admin.site.urls),
    path('api/create_ad_api/', create_ad_api, name='create_ad_api'),
    path('api/', include(router.urls)),
    path('api/apartment-rent/', ApartmentRentListCreate.as_view(), name='apartment-rent-list-create'),
    path('api/apartment-sale/', ApartmentSaleListCreate.as_view(), name='apartment-sale-list-create'),
]
#
if settings.DEBUG:
    urlpatterns = list(urlpatterns) + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
