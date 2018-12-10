from .models import Producto, Lista, TiendaFisica, TiendaOnLine
from .serializers import ProductoSerializer, ListaSerializer, TiendaFisicaSerializer, TiendaOnLineSerializer
from rest_framework import viewsets


class ProductoViewSet(viewsets.ModelViewSet):
 
    serializer_class = ProductoSerializer
    queryset = Producto.objects.all()
	
class ListaViewSet(viewsets.ModelViewSet):
 
    serializer_class = ListaSerializer
    queryset = Lista.objects.all()

class TiendaFisicaViewSet(viewsets.ModelViewSet):
 
    serializer_class = TiendaFisicaSerializer
    queryset = TiendaFisica.objects.all()
	
class TiendaOnLineViewSet(viewsets.ModelViewSet):
 
    serializer_class = TiendaOnLineSerializer
    queryset = TiendaOnLine.objects.all()
    