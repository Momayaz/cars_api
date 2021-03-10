"""api_cars URL Configuration

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
from django.contrib import admin
from django.urls import include,path
from rest_framework import routers
from cars.views import Cars_Viewset, Mercedes_Viewset, BMW_Viewset, Chevrolet_Viewset
from django.conf.urls.static import static
from django.conf import settings

router = routers.SimpleRouter()
router.register('cars', Cars_Viewset)
router.register('mercedes', Mercedes_Viewset)
router.register('bmw', BMW_Viewset)
router.register('chevrolet', Chevrolet_Viewset)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(router.urls)),
]+static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
