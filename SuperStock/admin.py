from django.contrib import admin
from .models import CategoriasProductos, Productos, Proveedores, Ventas, Inventario, Clientes, Usuario, DetallesVentas, MetodoPago, DescuentosProductos, Descuentos, Cargos, Horarios
from django.contrib.auth.models import User


class CategoriasProductosAdmin(admin.ModelAdmin):
    list_display = ('id_categorias', 'categorias', 'in_active')

admin.site.register(CategoriasProductos, CategoriasProductosAdmin)

class ProductosAdmin(admin.ModelAdmin):
    list_display = ('id_productos', 'id_categorias', 'nombreP', 'stock', 'precio', 'fecha_creacion', 'in_active')

admin.site.register(Productos, ProductosAdmin)

class ProveedoresAdmin(admin.ModelAdmin):
    list_display = ('id_proveedores', 'nombrePEE', 'direccion', 'telefono', 'email', 'fecha_creacion', 'in_active')
admin.site.register(Proveedores, ProveedoresAdmin)

class VentasAdmin(admin.ModelAdmin):
    list_display = ('id_ventas', 'id_clientes', 'id_usuario', 'id_metodos', 'fecha_hora', 'in_active')
admin.site.register(Ventas, VentasAdmin)

class InventarioAdmin(admin.ModelAdmin):
    list_display = ('id_inventario', 'id_proveedores', 'id_productos', 'fecha_entrada', 'cantidad', 'fecha_creacion', 'in_active')
admin.site.register(Inventario, InventarioAdmin)

class ClientesAdmin(admin.ModelAdmin):
    list_display = ('ci_o_ruc', 'nombreC', 'apellido', 'fecha_creacion', 'in_active')
admin.site.register(Clientes, ClientesAdmin)

class DetallesVentasAdmin(admin.ModelAdmin):
    list_display = ('id_detalles_venta', 'id_ventas', 'id_productos', 'cantidad', 'fecha_creacion', 'in_active')
    def id_productos(self, obj):
        return ", ".join([producto.nombreP for producto in obj.id_productos.all()])
    id_productos.short_description = "Productos"
admin.site.register(DetallesVentas, DetallesVentasAdmin)

class MetodoPagoAdmin(admin.ModelAdmin):
    list_display = ('id_metodos', 'metodos', 'in_active')
admin.site.register(MetodoPago, MetodoPagoAdmin)

class DescuentosAdmin(admin.ModelAdmin):
    list_display = ('id_descuento', 'tipo', 'porcentaje', 'in_active')
admin.site.register(Descuentos, DescuentosAdmin)

class DescuentosProductosAdmin(admin.ModelAdmin):
    list_display = ('id_descuentos', 'id_productos', 'descuento_tipo', 'valor', 'fecha_inicio', 'fecha_fin', 'fecha_creacion', 'in_active')
admin.site.register(DescuentosProductos, DescuentosProductosAdmin)

class HorariosAdmin(admin.ModelAdmin):
    list_display = ('id_horarios', 'desde', 'hasta', 'in_active')
admin.site.register(Horarios, HorariosAdmin)

class CargosAdmin(admin.ModelAdmin):
    list_display = ('id_cargos', 'cargos', 'descripcion', 'in_active')

class UsuarioAdmin(admin.ModelAdmin):
    list_display = ('id_usuario', 'nombreU', 'cargues', 'horario', 'fecha_creacion', 'in_active')
admin.site.register(Usuario, UsuarioAdmin)


