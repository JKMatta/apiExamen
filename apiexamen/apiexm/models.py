from django.db import models


class Producto( models.Model ):
    Nombre = models.CharField( max_length = 255 )
    CostoPresupuesto = models.IntegerField()
    CostoReal = models.IntegerField()
    Tienda = models.CharField( max_length = 255 )
    NotaAdicional = models.TextField(max_length=100)
    GrupoList = models.CharField( max_length = 255 )
	

class Lista( models.Model ):
    Nombre = models.CharField( max_length = 255 )
    CantidadMax = models.IntegerField()


class TiendaFisica( models.Model ):
    Nombre = models.CharField( max_length = 255 )
    NombreSucursal = models.CharField( max_length = 255 )
    Direccion = models.CharField( max_length = 255 )
    Ciudad = models.CharField( max_length = 255 )
    Region = models.CharField( max_length = 255 )
	

class TiendaOnLine( models.Model ):
    Nombre = models.CharField( max_length = 255 )
    NombreSucursal = models.CharField( max_length = 255 )
    Link = models.CharField( max_length = 255 )
    Email= models.CharField( max_length = 255, default = '' )
    