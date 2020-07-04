from django.contrib import admin
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from modulos.transaccion.views import TransaccionViewSet



urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(('modulos.users.urls', 'modulos.users'), namespace='users')),
    path('', include(('modulos.transaccion.urls', 'modulos.transaccion'), namespace='transaccion')),


]
