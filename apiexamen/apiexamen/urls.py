from django.conf.urls import include, url
from django.contrib import admin
admin.autodiscover()

from apiexm.views import ProductoViewSet, ListaViewSet, TiendaFisicaViewSet, TiendaOnLineViewSet
from rest_framework.routers import DefaultRouter
router = DefaultRouter()
router.register(r'Productos', ProductoViewSet)
router.register(r'Listas', ListaViewSet)
router.register(r'TiendaFisica', TiendaFisicaViewSet)
router.register(r'TiendaOnline', TiendaOnLineViewSet)

urlpatterns = [
    url('admin/', admin.site.urls),
    url(r'^', include(router.urls)),
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    
]