from django.contrib import admin
from .models import Producto, Lista, TiendaFisica, TiendaOnLine

admin.site.register( Producto )
admin.site.register( Lista )
admin.site.register( TiendaFisica )
admin.site.register( TiendaOnLine )


