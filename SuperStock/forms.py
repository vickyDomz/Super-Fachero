from .models import CategoriasProductos, Productos, Proveedores, Ventas, Inventario, Clientes, Usuario, DetallesVentas, MetodoPago, DescuentosProductos, Descuentos, Cargos, Horarios
from django import forms
from django.contrib.auth.models import User

class CategoriasProductosForm(forms.ModelForm):
    class Meta:
        model = CategoriasProductos
        fields = ('categorias',)
        widgets = {
            'categorias': forms.TextInput(attrs={'placeholder': 'Ingrese una nueva categoria: '})
        }
class ProductosForm(forms.ModelForm):
    class Meta:
        model = Productos
        fields = ('id_categorias', 'nombreP', 'precioCost', 'precio')

class ProveedoresForm(forms.ModelForm):
    class Meta:
        model = Proveedores
        fields = ('nombrePEE', 'direccion', 'telefono', 'email')

class InventarioForm(forms.ModelForm):
    class Meta:
        model = Inventario
        fields = ('id_proveedores', 'id_productos', 'fecha_entrada', 'cantidad')
        widgets = {
            'fecha_entrada': forms.DateInput(attrs={'type': 'date'}),
        }

class ClientesForm(forms.ModelForm):
    class Meta:
        model = Clientes
        fields = ('ci_o_ruc', 'nombreC', 'apellido')

class VentasForm(forms.ModelForm):
    class Meta:
        model = Ventas
        fields = ('id_clientes', 'id_usuario', 'id_metodos',)

    id_clientes = forms.ModelChoiceField(label='Cliente', queryset=Clientes.objects.all(), empty_label="(Nothing)")
    id_usuario = forms.ModelChoiceField(label='Usuario', queryset=Usuario.objects.all(), empty_label="(Nothing)")
    id_metodos = forms.ModelChoiceField(label='Metodo', queryset=MetodoPago.objects.all(), empty_label="(Nothing)")

'''
def clean(self):
    cleaned_data = super().clean()
    productos = cleaned_data.get('productos')
    cantidades = cleaned_data.get('cantidades')

    if not cantidades:
        raise forms.ValidationError("Debe ingresar cantidades para los productos seleccionados.")

    cantidades = cantidades.split(',')

    if len (productos) != len(cantidades):
        raise forms.ValidationError("El numero de cantidades no coincide con el numero de productos seleccionados.")
    productos_con_cantidad = []
    for producto, cantidad in zip(productos, cantidades):
            productos_con_cantidad.append({
                'id_producto': producto.id,
                'cantidad': int(cantidad)
            })
    cleaned_data['productos_con_cantidad'] = productos_con_cantidad
    return cleaned_data
'''


class DetallesVentasForm(forms.ModelForm):
    class Meta:
        model = DetallesVentas
        fields = ('id_ventas','id_productos', 'cantidad')

    id_productos = forms.ModelMultipleChoiceField(
    label='Selecciona los productos', 
    queryset = Productos.objects.all(), 
    widget = forms.CheckboxSelectMultiple(attrs={'class': 'checkbox-widget'}),
    required = True
    )
    cantidad = forms.CharField()
    
    def clean_cantidad(self):
        cantidad = self.cleaned_data.get('cantidad', '')

        try:
            cantidades = [int(x) for x in cantidad.split(',')]
        except ValueError:
            raise forms.ValidationError("Porfavor ingrese las cantidades de los productos separados por una coma.")
        return cantidades            

class MetodoPagoForm(forms.ModelForm):
    class Meta:
        model = MetodoPago
        fields = ('metodos', 'descripcion')

class DescuentosProductosForm(forms.ModelForm):
    class Meta:
        model = DescuentosProductos
        fields = ('id_productos', 'descuento_tipo', 'fecha_inicio', 'fecha_fin', 'descripcion')
        widgets = {
            'fecha_inicio': forms.DateInput(attrs={'type': 'date'}),
            'fecha_fin': forms.DateInput(attrs={'type': 'date'}),
        }

class DescuentosForm(forms.ModelForm):
    class Meta:
        model = Descuentos
        fields = ('tipo', 'porcentaje')

class HorariosForm(forms.ModelForm):
    class Meta:
        model = Horarios
        fields = ('desde', 'hasta',)
        widgets = {
            'desde': forms.TimeInput(attrs={'type': 'time'}),
            'hasta': forms.TimeInput(attrs={'type': 'time'}),
        }

class CargosForm(forms.ModelForm):
    class Meta:
        model = Cargos
        fields = ('cargos', 'descripcion', 'in_active')

class UsuariosForm(forms.ModelForm):
    class Meta:
        model = Usuario
        fields = ('nombreU', 'cargues', 'horario')

    nombreU = forms.ModelChoiceField(label='Usuario', queryset=User.objects.all(), empty_label="(Nothing)")
    cargues = forms.ModelChoiceField(label='Cargo', queryset=Cargos.objects.all(), empty_label="(Nothing)")
    horario = forms.ModelChoiceField(label='Horario', queryset=Horarios.objects.all(), empty_label="(Nothing)")
