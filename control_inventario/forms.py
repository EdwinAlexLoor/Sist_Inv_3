from django.forms import ModelForm
from django import forms
from .models import CategoriaBodega, bodega, Categoria_producto,Marca, rol_persona, ingreso_cabecera, Egreso_cabecera,\
    Persona, producto, Devolucion, proveedor,Bodega_producto, ingreso_detalle, Egreso_detalle, ciudad

class BuscarCod(forms.Form):
    codigo = forms.CharField(label="Codigo De Documento", required=True)


class BuscarbodegaForm(forms.Form):

    nombre=forms.CharField (label="Nombre", required="True")
class BuscarNombreProductoForm ( forms.Form ) :
    nombre = forms.CharField ( label="Nombre Producto" , required=True )

class BuscarRucProveedorForm(forms.Form):

    ruc = forms.CharField (label= "Ruc",required=True)

class BuscarFecha(forms.Form):
    desde = forms.DateTimeField(label="Desde", required=True, widget=forms.DateInput(format=('%Y-%m-%d'),
                                                                                     attrs={
                                                                                         'placeholder': 'Select a date',
                                                                                         'type': 'date', 'size': 40}))

    hasta = forms.DateTimeField(label="Hasta", required=True, widget=forms.DateInput(format=('%Y-%m-%d'),
                                                                                     attrs={
                                                                                         'placeholder': 'Select a date',
                                                                                         'type': 'date', 'size': 40}))


class BuscarPersonaForm(forms.Form):
    desde = forms.DateTimeField(label="Desde", required=True, widget=forms.DateInput(format=('%Y-%m-%d'),
                                                                                     attrs={
                                                                                         'placeholder': 'Select a date',
                                                                                         'type': 'date', 'size': 40}))

    hasta = forms.DateTimeField(label="Hasta", required=True, widget=forms.DateInput(format=('%Y-%m-%d'),
                                                                                     attrs={
                                                                                         'placeholder': 'Select a date',
                                                                                         'type': 'date', 'size': 40}))

class BuscarNombreFecha(forms.Form):
    desde = forms.DateTimeField ( label="Desde" , required=True , widget=forms.DateInput ( format=('%Y-%m-%d') ,
                                                                                           attrs={
                                                                                               'placeholder' : 'Select a date' ,
                                                                                               'type' : 'date' ,
                                                                                               'size' : 40} ) )

    hasta = forms.DateTimeField ( label="Hasta" , required=True , widget=forms.DateInput ( format=('%Y-%m-%d') ,
                                                                                           attrs={
                                                                                               'placeholder' : 'Select a date' ,
                                                                                               'type' : 'date' ,
                                                                                               'size' : 40} ) )

    nombre = forms.CharField (label= "Nombre", required=True)

class Categoria_bodegaForm (ModelForm):
    class Meta:
        model = CategoriaBodega
        fields = ['nombre', 'descripcion_catbog' ]

class BodegaForm (ModelForm):
    class Meta:
        model = bodega
        fields = ['nombre', 'descripcion', 'categoria' ]


class Categoria_productoForm (ModelForm):
    class Meta:
        model = Categoria_producto
        fields = ['nombre', 'descripcion' ]


class MarcaForm (ModelForm):
    class Meta:
        model = Marca
        fields = ['nombre']


class Rol_personaForm(ModelForm):
    class Meta:
        model = rol_persona
        fields = ['cargo']



class Ingreso_cabeceraForm(ModelForm):
    class Meta:
        model = ingreso_cabecera
        fields = ['codigo_documento_cabecera', 'fecha_documento_cabecera', 'usuario_recibe_cabecera', 'usuario_entrega_cabecera', 'total_ingreso_cabecera' ]


class Egreso_cabeceraForm (ModelForm):
    class Meta:
        model = Egreso_cabecera
        fields = ['codigo_documento_eg', 'fecha_documento_eg', 'usuario_entrega_eg', 'usuario_recibe_eg', 'total_egreso_eg' ]


class PersonaForm(ModelForm):
    class Meta:
        model = Persona
        fields = ['nombre', 'apellido', 'edad', 'direccion', 'cedula', 'correo', 'Rol_persona' ]


class ProductoForm (ModelForm):
    class Meta:
        model = producto
        fields = [ 'codigo', 'nombre', 'descripcion', 'categoria_producto' ]

class CiudadForm (ModelForm):
    class Meta:
        model = ciudad
        fields = ['nombre' ]

class DevolucionForm (ModelForm):
    class Meta:
        model = Devolucion
        fields = ['detalle' ,'Producto' ]


class ProveedorForm (ModelForm):
    class Meta:
        model = proveedor
        fields = ['ruc', 'nombre_empresa', 'descripcion_proveedor', 'direccion', 'celular', 'Ciudad' ]


class Bodega_productoForm (ModelForm):
    class Meta:
        model = Bodega_producto
        fields = ['Bodega', 'Producto', 'cantidad_existencia', 'precio_compra', 'precio_venta', 'stock_maximo', 'stock_minimo' ]


class Ingreso_detalleForm (ModelForm):
    class Meta:
        model = ingreso_detalle
        fields = ['Ingreso_cabecera', 'Producto', 'cantidad_ingreso', 'precio_ingreso', 'sub_total_ingreso' ]

class Egreso_detalleForm (ModelForm):
    class Meta:
        model = Egreso_detalle
        fields = ['egreso_cabecera', 'Producto', 'cantidad_egreso', 'precio_egreso', 'sub_total_egreso']