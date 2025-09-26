from .models import CategoriasProductos, Productos, Proveedores, Ventas, Inventario, Clientes, Usuario, DetallesVentas, MetodoPago, DescuentosProductos, Descuentos, Cargos, Horarios
from django.utils import timezone
from django.shortcuts import render, get_object_or_404, redirect
from .forms import CategoriasProductosForm, ProductosForm, ProveedoresForm, InventarioForm, ClientesForm, UsuariosForm, DetallesVentasForm, MetodoPagoForm, DescuentosProductosForm, DescuentosForm, CargosForm, HorariosForm, VentasForm
from django.http import JsonResponse
from django.contrib.auth.models import User
from django.http import HttpResponse

#CATEGORIAS
def categorias_list(request):
    categorias = CategoriasProductos.objects.all()
    in_active = request.POST.get("in_active")
    categoria = request.POST.get("categoria")
    id_categorias = request.POST.get("id_categorias")

    if request.method == "POST":
        if in_active == 'si':
            categorias = categorias.filter(in_active=True)
        elif in_active == 'no':
            categorias = categorias.filter(in_active=False)
        if id_categorias:
            categorias = categorias.filter(id_categorias=id_categorias)
        if categoria:
            categorias = categorias.filter(categorias__icontains=categoria)
    return render(request, 'SuperStock/categorias_list.html', {'categorias': categorias})

def categorias_detail(request, pk):
    categorias = get_object_or_404(CategoriasProductos, pk=pk)

    return render(request, 'SuperStock/categorias_detail.html', {'categorias': categorias,})

def categorias_edit(request, pk):
    categorias = get_object_or_404(CategoriasProductos, pk=pk)
    if request.method == "POST":
        form = CategoriasProductosForm(request.POST, instance=categorias)
        if form.is_valid():
            categorias=form.save(commit=False)
            categorias.save()
            return redirect('categorias_list')
        else:
            return redirect ('categorias_edit', pk=categorias.pk)
    else:
        form = CategoriasProductosForm(instance=categorias)
    return render(request, 'SuperStock/categorias_edit.html', {'form': form, 'categorias': categorias})

def categorias_new (request):
    if request.method == "POST":
        form = CategoriasProductosForm(request.POST)
        if form.is_valid():
            categorias = form.save(commit=False)
            categorias.save()
            return redirect ('categorias_list')
        else:
            return redirect ('categorias_new')
    else: 
        form = CategoriasProductosForm()
    return render (request, 'SuperStock/categorias_edit.html', {'form': form})


def categorias_delete(request, pk):
    categorias = get_object_or_404(CategoriasProductos, pk=pk)
    CategoriasProductos.objects.filter(id_categorias=pk).update(in_active=False)

    return redirect('categorias_list')

def categorias_restore(request, pk):
    categorias = get_object_or_404(CategoriasProductos, pk=pk)
    CategoriasProductos.objects.filter(id_categorias=pk).update(in_active=True)

    return redirect('categorias_list')


#CLIENTES
def clientes_list(request):
    clientes = Clientes.objects.all()

    id_clientes = request.POST.get("id_clientes")
    nombres = request.POST.get("nombres")
    apellido = request.POST.get("apellido")
    ci_ruc = request.POST.get("ci_ruc")
    in_active = request.POST.get("in_active")

    if request.method == "POST":
        if id_clientes:
            clientes = clientes.filter(id_clientes=id_clientes)
        if nombres:
            clientes = clientes.filter(nombreC__icontains=nombres)
        if apellido:
            clientes = clientes.filter(apellido__icontains=apellido)
        if ci_ruc:
            clientes = clientes.filter(ci_o_ruc__icontains=ci_ruc)
        if in_active == "si":
            clientes = clientes.filter(in_active=True)
        elif in_active == "no":
            clientes = clientes.filter(in_active=False)
    return render(request, 'SuperStock/clientes_list.html', {'clientes': clientes})

def clientes_detail(request, pk):
    clientes = get_object_or_404(Clientes, pk=pk)
    return render (request, 'SuperStock/clientes_detail.html', {'clientes': clientes})

def clientes_edit(request, pk):
    clientes = get_object_or_404(Clientes, pk=pk)
    if request.method == "POST":
        form = ClientesForm(request.POST, instance=clientes)
        if form.is_valid():
            clientes = form.save(commit=False)
            clientes.save()
            return redirect ('clientes_list')
        else:
            return redirect ('clientes_edit', pk=clientes.pk)
    else:
        form = ClientesForm(instance=clientes)
    return render (request, 'SuperStock/clientes_edit.html', {'form': form, 'clientes': clientes})

def clientes_new(request):
    if request.method == "POST":
        form = ClientesForm(request.POST)
        if form.is_valid():
            clientes = form.save(commit=False)
            clientes.save()
            return redirect ('clientes_list')
        else:
            return redirect ('clientes_new')
    else:
        form = ClientesForm()
    return render (request, 'SuperStock/clientes_edit.html', {'form': form})

def clientes_delete(request, pk):
    clientes = get_object_or_404(Clientes, pk=pk)
    Clientes.objects.filter(id_clientes=pk).update(in_active=False)

    return redirect('clientes_list')

def clientes_restore(request, pk):
    clientes = get_object_or_404(Clientes, pk=pk)
    Clientes.objects.filter(id_clientes=pk).update(in_active=True)

    return redirect('clientes_list')



#METODOS DE PAGO
def metodos_list(request):
    metodos = MetodoPago.objects.all()  

    id_metodos = request.POST.get("id_metodos")
    metodo = request.POST.get("metodo")
    in_active = request.POST.get("in_active")
    
    if request.method == "POST":
        if id_metodos:
            metodos = metodos.filter(id_metodos=id_metodos)
        if metodo:
            metodos = metodos.filter(metodos__contains=metodo)
        if in_active == "si":
            metodos = metodos.filter(in_active=True)
        elif in_active == "no":
            metodos = metodos.filter(in_active=False)

    return render (request, 'SuperStock/metodos_list.html', {'metodos': metodos})  

def metodos_detail(request, pk):
    metodos= get_object_or_404(MetodoPago, pk=pk)
    return render (request, 'SuperStock/metodos_detail.html', {'metodos': metodos})

def metodos_edit(request, pk):
    metodos=get_object_or_404(MetodoPago, pk=pk)
    if request.method == "POST":
        form = MetodoPagoForm(request.POST, instance=metodos)
        if form.is_valid():
            metodos = form.save(commit=False)
            metodos.save()
            return redirect ('metodos_list')
        else: 
            return redirect ('metodos_edit', pk=metodos.pk)
    else:
        form = MetodoPagoForm(instance=metodos)
    return render (request, 'SuperStock/metodos_edit.html', {'form': form, 'metodos': metodos})

def metodos_new(request):
    if request.method == "POST":
        form = MetodoPagoForm(request.POST)
        if form.is_valid():
            metodos = form.save(commit=False)
            metodos.save()
            return redirect ('metodos_list')
        else:
            return redirect ('metodos_new')
    else:
        form = MetodoPagoForm()
    return render (request, 'SuperStock/metodos_edit.html', {'form': form})

def metodos_delete(request, pk):
    metodos = get_object_or_404(MetodoPago, pk=pk)
    MetodoPago.objects.filter(id_metodos=pk).update(in_active=False)

    return redirect('metodos_list')

def metodos_restore(request, pk):
    metodos = get_object_or_404(MetodoPago, pk=pk)
    MetodoPago.objects.filter(id_metodos=pk).update(in_active=True)

    return redirect('metodos_list')
 

#PRODUCTOS
def productos_list(request):
    productos = Productos.objects.all()
    categoriass = CategoriasProductos.objects.all()

    id_productos = request.POST.get("id_productos")
    id_categoria = request.POST.get("id_categoria")
    nombreP = request.POST.get("nombreP")
    mayor = request.POST.get("mayor")
    menor = request.POST.get("menor")
    in_active = request.POST.get("in_active")
    if request.method == "POST":
        if id_productos:
            productos = productos.filter(id_productos=id_productos)
        if id_categoria:
            productos = productos.filter(id_categorias__categorias__contains=id_categoria)
        if nombreP:
            productos = productos.filter(nombreP__icontains=nombreP)
        if mayor:
            productos = productos.filter(precio__gte=mayor)
        if menor:
            productos = productos.filter(precio__lte=menor)
        if in_active == 'si':
            productos = productos.filter(in_active=True)
        elif in_active == 'no':
            productos = productos.filter(in_active=False)
    return render (request, 'SuperStock/productos_list.html', {'productos': productos, 'categoriass': categoriass})

def productos_detail(request, pk):
    productos = get_object_or_404(Productos, pk=pk)
    return render (request, 'SuperStock/productos_detail.html', {'productos': productos})

def productos_edit(request, pk):
    productos = get_object_or_404(Productos, pk=pk)
    if request.method == "POST":
        form = ProductosForm(request.POST, instance=productos)
        if form.is_valid():
            productos = form.save(commit=False)
            productos.save()
            return redirect ('productos_list')
        else:
            return redirect ('productos_edit', pk=productos.pk)
    else:
        form = ProductosForm(instance=productos)    
    return render (request, 'SuperStock/productos_edit.html', {'form': form, 'productos': productos})

def productos_new(request):
    if request.method == "POST":
        form = ProductosForm(request.POST)
        if form.is_valid():
            productos = form.save(commit=False)
            productos.save()
            return redirect ('productos_list')
        else:
            return redirect ('productos_new')
    else:
        form = ProductosForm()
    return render (request, 'SuperStock/productos_edit.html', {'form': form})

def productos_delete(request, pk):
    productos = get_object_or_404(Productos, pk=pk)
    Productos.objects.filter(id_productos=pk).update(in_active=False)

    return redirect('productos_list')

def productos_restore(request, pk):
    productos = get_object_or_404(Productos, pk=pk)
    Productos.objects.filter(id_productos=pk).update(in_active=True)

    return redirect('productos_list')


#DESCUENTOS DE PRODUCTOS
def descuentos_list(request): #hacer que los productos que salgan en el dropdown sean los de la categoria elegida
    descuentos = DescuentosProductos.objects.all()
    descuentosT = Descuentos.objects.all()
    producte = Productos.objects.all()
    categories = CategoriasProductos.objects.all()

    id_descuentos = request.POST.get("id_descuentos")
    categoria = request.POST.get("categoria")
    producto = request.POST.get("producto")
    tipos = request.POST.get("tipos")
    in_active = request.POST.get("in_active")

    if request.method == "POST":
        if id_descuentos:
            descuentos = descuentos.filter(id_descuentos=id_descuentos)
        if categoria:
            descuentos = descuentos.filter(id_productos__id_categorias__categorias__contains=categoria)
        if producto:
            descuentos = descuentos.filter(id_productos__nombreP__contains=producto)
        #if producto and categoria:
        #    descuentos = descuentos.filter(id_productos__nombreP__contains=producto)
        #    descuentos = descuentos.filter(id_productos__id_categorias=categoria)
        if tipos:
            descuentos = descuentos.filter(descuento_tipo__tipo__contains=tipos)
        if in_active == 'si':
            descuentos = descuentos.filter(in_active=True)
        elif in_active == 'no':
            descuentos = descuentos.filter(in_active=False)
    return render (request, 'SuperStock/descuentos_list.html', {'descuentos': descuentos, 'descuentosT': descuentosT, 'producte': producte, 'categories': categories})

def descuentos_detail(request, pk):
    descuentos = get_object_or_404(DescuentosProductos, pk=pk)
    return render (request, 'SuperStock/descuentos_detail.html', {'descuentos': descuentos})

def descuentos_edit(request, pk):
    descuentos = get_object_or_404(DescuentosProductos, pk=pk)
    if request.method == "POST":
        form = DescuentosProductosForm(request.POST, instance=descuentos)
        if form.is_valid():
            descuentos = form.save(commit=False)
            descuentos.save()
            return redirect ('descuentos_list')
        else:
            return redirect ('descuentos_edit', pk=descuentos.pk)
    else:
        form = DescuentosProductosForm(instance=descuentos)
    return render (request, 'SuperStock/descuentos_edit.html', {'form': form, 'descuentos': descuentos})

def descuentos_new(request):
    if request.method == 'POST':
        form = DescuentosProductosForm(request.POST)
        if form.is_valid():
            descuentos = form.save(commit=False)
            descuentos.save()
            return redirect ('descuentos_list')
        else:
            return redirect ('descuentos_new')
    else:
        form = DescuentosProductosForm()
    return render (request, 'SuperStock/descuentos_edit.html', {'form': form})

def descuentos_delete(request, pk):
    descuentos = get_object_or_404(DescuentosProductos, pk=pk)
    DescuentosProductos.objects.filter(id_descuentos=pk).update(in_active=False)

    return redirect('descuentos_list')

def descuentos_restore(request, pk):
    descuentos = get_object_or_404(DescuentosProductos, pk=pk)
    DescuentosProductos.objects.filter(id_descuentos=pk).update(in_active=True)

    return redirect('descuentos_list')


#DESCUENTOS TIPO
def descuento_list(request):
    descuento = Descuentos.objects.all()

    id_descuento = request.POST.get("id_descuento")
    tipo = request.POST.get("tipo")
    in_active = request.POST.get("in_active")

    if request.method == "POST":
        if id_descuento:
            descuento = descuento.filter(id_descuento=id_descuento)
        if tipo:
            descuento = descuento.filter(tipo__icontains=tipo)
        if in_active == "si":
            descuento = descuento.filter(in_active = True)
        elif in_active == "no":
            descuento = descuento.filter(in_active = False)

    return render (request, 'SuperStock/descuento_list.html', {'descuento': descuento})

def descuento_detail(request, pk):
    descuento = get_object_or_404(Descuentos, pk=pk)
    return render (request, 'SuperStock/descuento_detail.html', {'descuento': descuento})

def descuento_edit(request, pk):
    descuento = get_object_or_404(Descuentos, pk=pk)
    if request.method == "POST":
        form = DescuentosForm(request.POST, instance=descuento)
        if form.is_valid():
            descuento = form.save(commit=False)
            descuento.save()
            return redirect ('descuento_list')
        else:
            return redirect ('descuento_edit', pk=descuento.pk)
    else:
        form = DescuentosForm(instance=descuento)
    return render (request, 'SuperStock/descuento_edit.html', {'form': form, 'descuento': descuento})

def descuento_new(request):
    if request.method == 'POST':
        form = DescuentosForm(request.POST)
        if form.is_valid():
            descuento = form.save(commit=False)
            descuento.save()
            return redirect ('descuento_list')
        else:
            return redirect ('descuento_new')
    else:
        form = DescuentosForm()
    return render (request, 'SuperStock/descuento_edit.html', {'form': form})

def descuento_delete(request, pk):
    descuento = get_object_or_404(Descuentos, pk=pk)
    Descuentos.objects.filter(id_descuento=pk).update(in_active=False)

    return redirect('descuento_list')

def descuento_restore(request, pk):
    descuento = get_object_or_404(Descuentos, pk=pk)
    Descuentos.objects.filter(id_descuento=pk).update(in_active=True)

    return redirect('descuento_list')


#PROVEEDORES
def proveedores_list(request):
    proveedores = Proveedores.objects.all() 

    id_proveedores = request.POST.get("id_proveedores")
    nombre = request.POST.get("nombre")
    fecha = request.POST.get("fecha")
    in_active = request.POST.get("in_active")

    if request.method == "POST":
        if id_proveedores:
            proveedores = proveedores.filter(id_proveedores=id_proveedores)
        if nombre:
            proveedores = proveedores.filter(nombrePEE__icontains=nombre)
        if fecha:
            proveedores = proveedores.filter(fecha_creacion__contains=fecha)
        if in_active == 'si':
            proveedores = proveedores.filter(in_active=True)
        elif in_active == 'no':
            proveedores = proveedores.filter(in_active=False)
    return render(request, 'SuperStock/proveedores_list.html', {'proveedores': proveedores})

def proveedores_detail(request, pk):
    proveedores = get_object_or_404(Proveedores, pk=pk)

    return render(request, 'SuperStock/proveedores_detail.html', {'proveedores': proveedores,})

def proveedores_edit(request, pk):
    proveedores = get_object_or_404(Proveedores, pk=pk)
    if request.method == "POST":
        form = ProveedoresForm(request.POST, instance=proveedores)
        if form.is_valid():
            proveedores=form.save(commit=False)
            proveedores.save()
            return redirect('proveedores_list')
        else:
            return redirect ('proveedores_edit', pk=proveedores.pk)
    else:
        form = ProveedoresForm(instance=proveedores)
    return render(request, 'SuperStock/proveedores_edit.html', {'form': form, 'proveedores': proveedores})

def proveedores_new (request):
    if request.method == "POST":
        form = ProveedoresForm(request.POST)
        if form.is_valid():
            proveedores = form.save(commit=False)
            proveedores.save()
            return redirect ('proveedores_list')
        else:
            return redirect ('proveedores_new')
    else: 
        form = ProveedoresForm()
    return render (request, 'SuperStock/proveedores_edit.html', {'form': form})

def proveedores_delete(request, pk):
    proveedores = get_object_or_404(Proveedores, pk=pk)
    Proveedores.objects.filter(id_proveedores=pk).update(in_active=False)

    return redirect('proveedores_list')

def proveedores_restore(request, pk):
    proveedores = get_object_or_404(Proveedores, pk=pk)
    Proveedores.objects.filter(id_proveedores=pk).update(in_active=True)

    return redirect('proveedores_list')


#INVENTARIO
def inventario_list(request):
    inventario = Inventario.objects.all()

    id_inventario = request.POST.get("id_inventario")
    proveedores = request.POST.get("proveedores")
    productos = request.POST.get("productos")
    fecha = request.POST.get("fecha")
    in_active = request.POST.get("in_active")

    if request.method == "POST":
        if id_inventario:
            inventario = inventario.filter(id_inventario=id_inventario)
        if proveedores:
            inventario = inventario.filter(id_proveedores__icontains=proveedores)
        if productos:
            inventario = inventario.filter(id_productos__icontains=productos)
        if fecha:
            inventario = inventario.filter(fecha_entrada__contains=fecha)
        if in_active == 'si':
            inventario = inventario.filter(in_active=True)
        elif in_active == 'no':
            inventario = inventario.filter(in_active=False)
    return render (request, 'SuperStock/inventario_list.html', {'inventario': inventario})

def inventario_detail(request, pk):
    inventario = get_object_or_404(Inventario, pk=pk)
    return render (request, 'SuperStock/inventario_detail.html', {'inventario': inventario})

def inventario_edit(request, pk):
    inventario = get_object_or_404(Inventario, pk=pk)
    if request.method == "POST":
        form = InventarioForm(request.POST, instance=inventario)
        if form.is_valid():
            inventario = form.save(commit=False)
            inventario.save()
            return redirect ('inventario_list')
        else:
            return redirect ('inventario_edit', pk=inventario.pk)
    else:
        form = InventarioForm(instance=inventario)
    return render (request, 'SuperStock/inventario_edit.html', {'form': form, 'inventario': inventario})

def inventario_new(request):
    if request.method == "POST":
        form = InventarioForm(request.POST)
        if form.is_valid():
            inventario = form.save(commit=False)
            inventario.save()
            return redirect ('inventario_list')
        else:
            return redirect ('inventario_new')
    else:
        form = InventarioForm()
    return render (request, 'SuperStock/inventario_edit.html', {'form': form}) 

def inventario_delete(request, pk):
    inventario = get_object_or_404(Inventario, pk=pk)
    Inventario.objects.filter(id_inventario=pk).update(in_active=False)

    return redirect('inventario_list')

def inventario_restore(request, pk):
    inventario = get_object_or_404(Inventario, pk=pk)
    Inventario.objects.filter(id_inventario=pk).update(in_active=True)

    return redirect('inventario_list')


#USUARIOS
def usuarios_list(request):
    usuarios = Usuario.objects.all()
    cargoss = Cargos.objects.all()
    horarioss = Horarios.objects.all()

    id_usuario = request.POST.get("id_usuario")
    nombreU = request.POST.get("nombreU")
    cargo = request.POST.get("cargo")
    desde = request.POST.get("desde")
    hasta = request.POST.get("hasta")
    in_active = request.POST.get("in_active")

    if request.method == "POST":
        if id_usuario:
            usuarios = usuarios.filter(id_usuario=id_usuario)
        if nombreU:
            usuarios = usuarios.filter(nombreU__username__icontains=nombreU)
        if cargo:
            usuarios = usuarios.filter(cargues__cargos__icontains=cargo)
        if desde:
            usuarios = usuarios.filter(horario__desde__contains=desde)
        if hasta:
            usuarios = usuarios.filter(horario__hasta__contains=hasta)
        if in_active == 'si':
            usuarios = usuarios.filter(in_active=True)
        elif in_active == 'no':
            usuarios = usuarios.filter(in_active=False)
    return render(request, 'SuperStock/usuarios_list.html', {'usuarios': usuarios, 'cargoss': cargoss, 'horarioss': horarioss})


def usuarios_detail(request, pk):
    usuarios = get_object_or_404(Usuario, pk=pk)

    return render(request, 'SuperStock/usuarios_detail.html', {'usuarios': usuarios})

def usuarios_edit(request, pk):
    usuarios = get_object_or_404(Usuario, pk=pk)
    if request.method == "POST":
        form = UsuariosForm(request.POST, instance=usuarios)
        if form.is_valid():
            usuarios=form.save(commit=False)
            usuarios.save()
            return redirect('usuarios_list')
        else:
            return redirect ('usuarios_edit', pk=usuarios.pk)
    else:
        form = UsuariosForm(instance=usuarios)
    return render(request, 'SuperStock/usuarios_edit.html', {'form': form, 'usuarios': usuarios})

def usuarios_new (request):
    if request.method == "POST":
        form = UsuariosForm(request.POST)
        if form.is_valid():
            usuarios = form.save(commit=False)
            usuarios.save()
            return redirect ('usuarios_list')
        else:
            return redirect ('usuarios_new')
    else: 
        form = UsuariosForm()
    return render (request, 'SuperStock/usuarios_edit.html', {'form': form})

def usuarios_delete(request, pk):
    usuarios = get_object_or_404(Usuario, pk=pk)
    Usuario.objects.filter(id_usuario=pk).update(in_active=False)

    return redirect('usuarios_list')

def usuarios_restore(request, pk):
    usuarios = get_object_or_404(Usuario, pk=pk)
    Usuario.objects.filter(id_usuario=pk).update(in_active=True)

    return redirect('usuarios_list')


#CARGOS
def cargos_list(request):
    cargos = Cargos.objects.all()
    in_active = request.POST.get("in_active")
    id_cargos = request.POST.get("id_cargos")
    cargo = request.POST.get("cargo")
    if request.method == "POST":
        if in_active == 'si':
            cargos = cargos.filter(in_active=True)
        elif in_active == 'no':
            cargos = cargos.filter(in_active=False)
        if id_cargos:
            cargos = cargos.filter(id_cargos=id_cargos) 
        if cargo:
            cargos = cargos.filter(cargos__icontains=cargo)
    return render(request, 'SuperStock/cargos_list.html', {'cargos': cargos})

def cargos_detail(request, pk):
    cargos = get_object_or_404(Cargos, pk=pk)

    return render(request, 'SuperStock/cargos_detail.html', {'cargos': cargos,})

def cargos_edit(request, pk):
    cargos = get_object_or_404(Cargos, pk=pk)
    if request.method == "POST":
        form = CargosForm(request.POST, instance=cargos)
        if form.is_valid():
            cargos=form.save(commit=False)
            cargos.save()
            return redirect('cargos_list')
        else:
            return redirect ('cargos_edit', pk=cargos.pk)
    else:
        form = CargosForm(instance=cargos)
    return render(request, 'SuperStock/cargos_edit.html', {'form': form, 'cargos': cargos})

def cargos_new (request):
    if request.method == "POST":
        form = CargosForm(request.POST)
        if form.is_valid():
            cargos = form.save(commit=False)
            cargos.save()
            return redirect ('cargos_list')
        else:
            return redirect ('cargos_new')
    else: 
        form = CargosForm()
    return render (request, 'SuperStock/cargos_edit.html', {'form': form})

def cargos_delete(request, pk):
    cargos = get_object_or_404(Cargos, pk=pk)
    Cargos.objects.filter(id_cargos=pk).update(in_active=False)

    return redirect('cargos_list')

def cargos_restore(request, pk):
    cargos = get_object_or_404(Cargos, pk=pk)
    Cargos.objects.filter(id_cargos=pk).update(in_active=True)

    return redirect('cargos_list')


#HORARIOS
def horarios_list(request):
    horarios = Horarios.objects.all()

    id_horarios = request.POST.get("id_horarios")
    desde = request.POST.get("desde")
    hasta = request.POST.get("hasta")
    in_active = request.POST.get("in_active")

    if request.method == "POST":
        if id_horarios:
            horarios = horarios.filter(id_horarios=id_horarios)
        if desde:
            horarios = horarios.filter(desde__contains=desde)
        if hasta:
            horarios = horarios.filter(hasta__contains=hasta)
        if in_active == 'si':
            horarios = horarios.filter(in_active=True)
        elif in_active == 'no':
            horarios = horarios.filter(in_active=False)
    return render(request, 'SuperStock/horarios_list.html', {'horarios': horarios})

def horarios_detail(request, pk):
    horarios = get_object_or_404(Horarios, pk=pk)

    return render(request, 'SuperStock/horarios_detail.html', {'horarios': horarios,})

def horarios_edit(request, pk):
    horarios = get_object_or_404(Horarios, pk=pk)
    if request.method == "POST":
        form = HorariosForm(request.POST, instance=horarios)
        if form.is_valid():
            horarios=form.save(commit=False)
            horarios.save()
            return redirect('horarios_list')
        else:
            return redirect ('horarios_edit', pk=horarios.pk)
    else:
        form = HorariosForm(instance=horarios)
    return render(request, 'SuperStock/horarios_edit.html', {'form': form, 'horarios': horarios})

def horarios_new (request):
    if request.method == "POST":
        form = HorariosForm(request.POST)
        if form.is_valid():
            horarios = form.save(commit=False)
            horarios.save()
            return redirect ('horarios_list')
        else:
            return redirect ('horarios_new')
    else:
        form = HorariosForm()
    return render (request, 'SuperStock/horarios_edit.html', {'form': form})

def horarios_delete(request, pk):
    horarios = get_object_or_404(Horarios, pk=pk)
    Horarios.objects.filter(id_horarios=pk).update(in_active=False)

    return redirect('horarios_list')

def horarios_restore(request, pk):
    horarios = get_object_or_404(Horarios, pk=pk)
    Horarios.objects.filter(id_horarios=pk).update(in_active=True)

    return redirect('horarios_list')


#DETALLES VENTAS
def detalles_list(request):
    detalles = DetallesVentas.objects.all()
    #if request.method == 'POST':
    #    form = DetallesVentasForm(request.POST)
    #    if form.is_valid():
    #        cantidades = form.cleaned_data['cantidad']
    #        return render (request, 'SuperStock/detalles_list.html', {'cantidades': cantidades})
    #else:
    #    form = DetallesVentasForm()
    id_detalles_venta = request.POST.get("id_detalles_venta")
    id_ventas = request.POST.get("id_ventas")
    fecha = request.POST.get("fecha")
    in_active = request.POST.get("in_active")

    if request.method == "POST":
        if id_detalles_venta:
            detalles = detalles.filter(id_detalles_venta=id_detalles_venta)
        if id_ventas:
            detalles = detalles.filter(id_ventas=id_ventas)
        if fecha:
            detalles = detalles.filter(fecha_creacion__contains=fecha)
        if in_active == 'si':
            detalles = detalles.filter(in_active=True)
        elif in_active == 'no':
            detalles = detalles.filter(in_active=False)
    return render (request, 'SuperStock/detalles_list.html', {'detalles': detalles})

def detalles_detail(request, pk):
    detalles = get_object_or_404(DetallesVentas, pk=pk)
    return render (request, 'SuperStock/detalles_detail.html', {'detalles': detalles} )

def detalles_edit(request, pk):
    detalles = get_object_or_404 (DetallesVentas, pk=pk)
    if request.method == "POST":
        form = DetallesVentasForm(request.POST, instance = detalles)
        if form.is_valid():
            detalles = form.save(commit=False)
            detalles.save()
            form.save_m2m()
            return redirect ('detalles_list')
        else:
            return redirect ('detalles_edit', pk=detalles.pk)
    else:
        form = DetallesVentasForm(instance=detalles)
    return render (request, 'SuperStock/detalles_edit.html', {'form': form, 'detalles': detalles})
    
def detalles_new(request):
    if request.method == "POST":
        form = DetallesVentasForm(request.POST)
        if form.is_valid():
            detalles = form.save(commit=False)
            detalles.save()
            form.save_m2m()
            return redirect ('detalles_list')
        else:
            return redirect ('detalles_new')
    else:
        form = DetallesVentasForm()
    return render (request, 'SuperStock/detalles_edit.html', {'form': form})

def detalles_delete(request, pk):
    detalles = get_object_or_404(DetallesVentas, pk=pk)
    DetallesVentas.objects.filter(id_detalles_venta=pk).update(in_active=False)

    return redirect('detalles_list')

def detalles_restore(request, pk):
    detalles = get_object_or_404(DetallesVentas, pk=pk)
    DetallesVentas.objects.filter(id_detalles_venta=pk).update(in_active=True)

    return redirect('detalles_list')


#VENTAS
def ventas_list(request):
    ventas = Ventas.objects.all()
    metodes = MetodoPago.objects.all()

    id_ventas = request.POST.get('id_ventas')
    clientes = request.POST.get('clientes')
    metodo = request.POST.get('metodo')
    fecha = request.POST.get('fecha')
    in_active = request.POST.get('in_active')

    if request.method == "POST":
        if id_ventas:
            ventas = ventas.filter(id_ventas=id_ventas)
        if clientes:
            ventas = ventas.filter(ci_o_ruc__nombreC__icontains=clientes)
        if metodo:
            ventas = ventas.filter(id_metodos__metodos__contains=metodo)
        if fecha:
            ventas = ventas.filter(fecha_hora__icontains=fecha)
        if in_active == 'si':
            ventas = ventas.filter(in_active=True)
        elif in_active == 'no':
            ventas = ventas.filter(in_active=False)
    return render (request, 'SuperStock/ventas_list.html', {'ventas': ventas, 'metodes': metodes})

def ventas_detail(request, pk):
    ventas = get_object_or_404(Ventas, pk=pk)
    return render (request, 'SuperStock/ventas_detail.html', {'ventas': ventas})

def ventas_edit(request, pk):
    ventas = get_object_or_404(Ventas, pk=pk)
    if request.method == "POST":
        form = VentasForm(request.POST, instance=ventas)
        if form.is_valid():
            ventas = form.save(commit=False)
            ventas.save()
            #productos_seleccionados = ventas.id_productos.all()
            return redirect ('ventas_list')
        else:
            return redirect ('ventas_edit', pk=ventas.pk)
    else: 
        form = VentasForm(instance=ventas)
    return render (request, 'SuperStock/ventas_edit.html', {'form': form, 'ventas': ventas})

def ventas_new(request):
    if request.method == "POST":
        form = VentasForm(request.POST)
        if form.is_valid():
            ventas = form.save(commit=False)
            ventas.save()
            return redirect ('ventas_list')
        else:
            return redirect ('ventas_new')
    else:
        form = VentasForm()
    return render (request, 'SuperStock/ventas_edit.html', {'form': form})

def ventas_delete(request, pk):
    ventas = get_object_or_404(Ventas, pk=pk)
    Ventas.objects.filter(id_ventas=pk).update(in_active=False)

    return redirect('ventas_list')

def ventas_restore(request, pk):
    ventas = get_object_or_404(Ventas, pk=pk)
    Ventas.objects.filter(id_ventas=pk).update(in_active=True)

    return redirect('ventas_list')

def paginaprincipal(request):
    return render(request, 'SuperStock/paginaprincipal.html')