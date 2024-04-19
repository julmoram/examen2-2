from django.contrib import admin
from django.urls import path, include
from rest_framework import routers
from rest_framework.authtoken.views import obtain_auth_token  # Importamos la vista de obtención de token

from mascotas import views

router = routers.DefaultRouter()
router.register('Mascota', views.MascotasViewset)

urlpatterns = [
    path('api-auth/', obtain_auth_token),
    path('admin/', admin.site.urls),
    path('api/', include(router.urls)),

]

