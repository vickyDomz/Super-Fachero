from django.db import models
from django.conf import settings
from django.utils import timezone

class CategoriasProductos(models.Model): #:D
    id_categorias = models.AutoField(primary_key=True)
    categorias = models.CharField (max_length=50, unique=True)
    in_active = models.BooleanField(default=True)

    def __str__(self):
        return self.categorias

class MetodoPago(models.Model): #:D
    id_metodos = models.AutoField(primary_key=True)
    metodos = models.CharField (max_length = 40)
    descripcion = models.CharField (max_length=100, blank=True, null=True)
    in_active = models.BooleanField(default=True)


    def __str__(self):
        return self.metodos

class Clientes(models.Model): #:D
    nombreC = models.CharField(max_length=40)
    apellido = models.CharField(max_length=40)
    ci_o_ruc = models.CharField(primary_key=True, max_length=20, unique=True)
    fecha_creacion = models.DateTimeField(auto_now_add = True)
    in_active = models.BooleanField(default=True)

    def __str__(self):
        return f"{self.nombreC} {self.apellido}"
    def save(self):
        self.fecha_creacion.strftime('%Y-%m-%d %H:%M')


class Horarios(models.Model):
    id_horarios = models.AutoField(primary_key=True)
    desde = models.TimeField()
    hasta = models.TimeField(blank=True, null=True)
    in_active = models.BooleanField(default=True)

    def __str__(self):
        return self.horarios()

    def horarios(self):
        if self.hasta:
            return f"{self.desde.strftime('%H:%M')} - {self.hasta.strftime('%H:%M')}"
        else:
            return f"{self.desde.strftime('%H:%M')} - No definido"

class Cargos(models.Model):
    id_cargos = models.AutoField(primary_key=True)
    cargos = models.CharField(max_length=60)
    descripcion = models.CharField(max_length=500, blank=True, null=True)
    in_active = models.BooleanField(default=True)

    def __str__(self):
        return self.cargos

class Usuario(models.Model):
    id_usuario = models.AutoField(primary_key=True)
    nombreU = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.PROTECT)
    cargues = models.ForeignKey(Cargos, on_delete=models.CASCADE)
    horario = models.ForeignKey(Horarios, on_delete=models.CASCADE)
    salario = models.IntegerField(blank=True, null=True)
    fecha_creacion = models.DateTimeField(auto_now_add = True)
    in_active = models.BooleanField(default=True)

    def __str__(self):
        return f"{self.nombreU.username}"

class Productos(models.Model): #:D
    id_productos = models.AutoField(primary_key = True)
    id_categorias = models.ForeignKey(CategoriasProductos, on_delete=models.CASCADE)
    stock = models.IntegerField(blank=True, null=True)
    precioCost = models.FloatField(null=True, blank=True)
    precio = models.FloatField(null=True, blank=True)
    fecha_creacion = models.DateTimeField(auto_now_add = True)
    nombreP = models.CharField(max_length = 70) 
    in_active = models.BooleanField(default=True)

    def __str__(self):
        return self.nombreP

    def save (self, *args, **kwargs):
        if self.precioCost is not None:
            self.precio = self.precioCost * 1.1

class Descuentos(models.Model): #:D
    id_descuento = models.AutoField(primary_key=True)
    tipo = models.CharField(max_length=50)
    porcentaje = models.IntegerField(blank=True, null=True)
    in_active = models.BooleanField(default=True)

    def __str__(self):
        return self.tipo


class DescuentosProductos(models.Model): #:D
    id_descuentos = models.AutoField(primary_key = True)
    id_productos = models.ForeignKey(Productos, on_delete=models.CASCADE)
    descuento_tipo = models.ForeignKey(Descuentos, on_delete=models.CASCADE)
    valor = models.IntegerField(blank=True, null=True)
    fecha_inicio = models.DateField()
    fecha_fin = models.DateField()
    descripcion = models.CharField(max_length=500, blank=True, null=True)
    fecha_creacion = models.DateTimeField(auto_now_add = True)
    in_active = models.BooleanField(default=True)

    def __str__(self):
        return self.fecha_creacion.strftime('%Y-%m-%d %H:%M')
    
class Proveedores(models.Model): #:D
    id_proveedores = models.AutoField(primary_key = True)
    nombrePEE = models.CharField(max_length = 100)
    direccion = models.CharField (max_length = 100)
    telefono = models.CharField(max_length = 20)
    email = models.CharField(max_length = 100)
    fecha_creacion = models.DateTimeField(auto_now_add = True)
    in_active = models.BooleanField(default=True)

    def __str__(self):
        return self.nombrePEE
        return self.fecha_creacion.strftime('%Y-%m-%d %H:%M')

class Inventario(models.Model):
    id_inventario = models.AutoField(primary_key = True)
    id_proveedores = models.ForeignKey(Proveedores, on_delete=models.CASCADE)
    id_productos = models.ForeignKey(Productos, on_delete=models.CASCADE)
    fecha_entrada = models.DateField()
    cantidad = models.IntegerField()
    fecha_creacion = models.DateTimeField(auto_now_add = True)
    in_active = models.BooleanField(default=True)

class Ventas(models.Model): #dejar para el ultimo
    id_ventas = models.AutoField(primary_key = True)
    id_clientes = models.ForeignKey(Clientes, on_delete=models.CASCADE, null=True)
    id_usuario = models.ForeignKey(Usuario, on_delete=models.CASCADE, null=True)
    id_metodos = models.ForeignKey(MetodoPago, on_delete=models.CASCADE, null=True)
    fecha_hora = models.DateTimeField(auto_now_add = True)
    total = models.DecimalField(max_digits=15, decimal_places=2, default=0.00)
    in_active = models.BooleanField(default=True)

    def __str__(self):
        return f'{self.id_ventas}'

class DetallesVentas(models.Model): #dejar para el ultimo
    id_detalles_venta = models.AutoField(primary_key = True)
    id_ventas = models.OneToOneField(Ventas, on_delete=models.CASCADE)
    id_productos = models.ManyToManyField(Productos)
    cantidad = models.CharField(max_length=150)
    fecha_creacion = models.DateTimeField(auto_now_add = True)
    total = models.DecimalField(max_digits=15, decimal_places=2, blank=True, null=True)
    in_active = models.BooleanField(default=True)

class Marcas(models.Model):
    id_marcas = models.AutoField(primary_key=True)
    marca = models.CharField(max_length=150)

class Equipos(models.Model):
    id_equipo = models.AutoField(primary_key=True)
    fecha_compra = models.DateTimeField()
    ubicacion = models.CharField(max_length=200)

#hacer un modelo equipos/insumos
#hacer un modelo "Marcas"

#HACER MIGRACIONES

#hacer una prueba de ventas y detalles de venta
#si algun productos esta inactivo, que no salga en otras tablas (detalles venta)
#modelo que diga que cajero esta en cierta caja dependiendo de la hora