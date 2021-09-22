from django.contrib import admin
from .models import Clientes, Op, Pedido, Remito, Vendedores

# Register your models here.
admin.site.register(Op)
admin.site.register(Pedido)
admin.site.register(Remito)
admin.site.register(Clientes)
admin.site.register(Vendedores)