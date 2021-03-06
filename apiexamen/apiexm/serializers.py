from rest_framework import serializers
from .models import Producto, Lista, TiendaFisica, TiendaOnLine

		
class ProductoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Producto
        fields = ('id', 'Nombre', 'CostoPresupuesto', 'CostoReal', 'Tienda', 'NotaAdicional', 'GrupoList', )
		
class ListaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Lista
        fields = ('id', 'Nombre', 'CantidadMax', )
		
class TiendaFisicaSerializer(serializers.ModelSerializer):
    class Meta:
        model = TiendaFisica
        fields = ('id', 'Nombre', 'NombreSucursal', 'Direccion', 'Ciudad', 'Region', )
		
class TiendaOnLineSerializer(serializers.ModelSerializer):
    class Meta:
        model = TiendaOnLine
        fields = ('id', 'Nombre', 'NombreSucursal', 'Link', 'Email', )
		

		



