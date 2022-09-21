from django.contrib.auth.decorators import login_required
from django.db.models import Q
from django.shortcuts import render , HttpResponse , redirect , get_object_or_404
from .forms import  PersonaForm , BodegaForm, Rol_personaForm, Categoria_productoForm, Bodega_productoForm, \
    DevolucionForm, Egreso_cabeceraForm, MarcaForm, Egreso_detalleForm, Ingreso_cabeceraForm, Ingreso_detalleForm, \
    ProductoForm, ProveedorForm, Categoria_bodegaForm, BuscarPersonaForm, BuscarFecha, \
    CiudadForm, BuscarNombreFecha,BuscarRucProveedorForm,BuscarNombreProductoForm,BuscarbodegaForm, BuscarCod

from .models import Persona, rol_persona, bodega, Categoria_producto, Bodega_producto, \
    Devolucion, Egreso_cabecera, Marca, Egreso_detalle, ingreso_cabecera, ingreso_detalle, producto , \
    proveedor, CategoriaBodega, ciudad


import io
from django.http import FileResponse
from reportlab.lib import colors
from reportlab.lib.pagesizes import A4
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib.units import cm, inch
from reportlab.pdfgen import canvas

#from django.shortcuts import render, HttpResponse, redirect, get_object_or_404
from django.contrib.auth import authenticate, login
from reportlab.platypus import TableStyle, Table, SimpleDocTemplate, Paragraph, Spacer
from reportlab.lib.enums import TA_JUSTIFY, TA_RIGHT, TA_CENTER, TA_LEFT


# Create your views here.


@login_required(None, "", 'login')
def exportarListaPersonaPdf(request):
    # Create a file-like buffer to receive PDF data.
    response = HttpResponse(content_type='application/pdf')
    response['Content-Disposition'] = 'filename="lista_personas.pdf"'

    buffer = io.BytesIO()

    doc = SimpleDocTemplate(buffer,
                            rightMargin=inch / 4,
                            leftMargin=inch / 4,
                            topMargin=inch / 2,
                            bottomMargin=inch / 4,
                            pagesize=A4)
    styles = getSampleStyleSheet()
    styles.add(ParagraphStyle(name='centered', alignment=TA_CENTER))
    styles.add(ParagraphStyle(name='RightAlign', fontName='Arial', align=TA_RIGHT))

    personas = []
    styles = getSampleStyleSheet()
    header = Paragraph("     Reporte de Personas", styles['Heading1'])
    personas.append(header)


    headings = ('Id', 'Nombre', 'Apellido', 'Edad', 'Direccion', 'Cedula', 'Correo')
    allpersonas = [(c.id, c.nombre, c.apellido, c.edad, c.direccion, c.cedula, c.correo) for c in Persona.objects.all()
]
    print
    allpersonas

    t = Table([headings] + allpersonas)
    t.setStyle(TableStyle(
        [
            ('GRID', (0, 0), (9, -1), 1, colors.springgreen),
            ('LINEBELOW', (0, 0), (-1, 0), 2, colors.springgreen),
            ('BACKGROUND', (0, 0), (-1, 0), colors.springgreen)
        ]
    ))
    personas.append(t)
    doc.build(personas)
    response.write(buffer.getvalue())
    buffer.close()
    return response


@login_required(None, "", 'login')
def exportarListaProductoPdf(request):
    # Create a file-like buffer to receive PDF data.
    response = HttpResponse(content_type='application/pdf')
    response['Content-Disposition'] = 'filename="lista_productos.pdf"'

    buffer = io.BytesIO()

    doc = SimpleDocTemplate(buffer,
                            rightMargin=inch / 4,
                            leftMargin=inch / 4,
                            topMargin=inch / 2,
                            bottomMargin=inch / 4,
                            pagesize=A4)
    styles = getSampleStyleSheet()
    styles.add(ParagraphStyle(name='centered', alignment=TA_CENTER))
    styles.add(ParagraphStyle(name='RightAlign', fontName='Arial', align=TA_RIGHT))

    productos = []
    styles = getSampleStyleSheet()
    header = Paragraph("     Reporte De Todos Los Productos", styles['Heading1'])
    productos.append(header)


    headings = ('Id', 'Codigo', 'Nombre', 'Descripcion', 'Cactegoria Del Producto')
    allproductos = [(c.id, c.codigo, c.nombre, c.descripcion, c.categoria_producto) for c in producto.objects.all()
]
    print
    allproductos

    t = Table([headings] + allproductos)
    t.setStyle(TableStyle(
        [
            ('GRID', (0, 0), (9, -1), 1, colors.springgreen),
            ('LINEBELOW', (0, 0), (-1, 0), 2, colors.springgreen),
            ('BACKGROUND', (0, 0), (-1, 0), colors.springgreen)
        ]
    ))
    productos.append(t)
    doc.build(productos)
    response.write(buffer.getvalue())
    buffer.close()
    return response


def saludo( request ) :
    return HttpResponse ( "Hola Mundo" )


def index( request ) :
    return render ( request , "registration/login.html" )


#def MiPrimeraFuncion( request ) :
   # return render ( request , "base.html" )
@login_required(None, "", 'login')
def base2 (request):
    return render (request, "base2.html")


##----------------------------- BODEGGA --------------##
@login_required(None, "", 'login')
def consultar_bodega( request ) :
    buscarbodeganombreform = BuscarbodegaForm ()
    bodega1 = None

    if request.method == "POST" :
        buscarbodeganombreform = BuscarbodegaForm ( request.POST or None )
        if buscarbodeganombreform.is_valid () :
            nombre = buscarbodeganombreform.cleaned_data['nombre']
            bodega1 = bodega.objects.filter ( nombre__icontains=nombre )
    else :
        bodega1 = bodega.objects.all ()
    #Bodega = bodega.objects.all()
    return render ( request , "bodega/consultar_bodega.html" , {'bodega_ls' : bodega1, 'bodegabuscar' : buscarbodeganombreform} )

@login_required(None, "", 'login')
def crear_bodega( request ) :
    if request.method == "POST" :
        bodegaForm = BodegaForm ( request.POST )
        if bodegaForm.is_valid () :
            bodegaForm.save ()
            return redirect ( 'consultar_bodega' )
        else :
            bodegaForm = BodegaForm ()
    else :
        bodegaForm = BodegaForm ()
    return render ( request , "bodega/crear_bodega.html" , {'bodegaForm' : bodegaForm} )

@login_required(None, "", 'login')
def eliminar_bodega (request,id):
    if request.method == "POST":
        bodega1 = get_object_or_404(bodega, pk=id)
        bodegaForm = BodegaForm(request.POST or None, instance=bodega1)
        if bodegaForm.is_valid():
            bodega1.estado = 0
            bodega1.save()
            return redirect('consultar_bodega')
    else:
        bodega1 = get_object_or_404(bodega, pk=id)
        bodegaForm = BodegaForm(request.POST or None, instance=bodega1)
    return render(request, "bodega/eliminar_bodega.html",{'bodega_e': bodegaForm})

@login_required(None, "", 'login')
def modificar_bodega (request,id):
    if request.method == "POST":
        bodega1 = get_object_or_404(bodega, pk=id)
        bodegaForm = BodegaForm(request.POST or None, instance=bodega1)
        if bodegaForm.is_valid():
            bodegaForm.save()
            return redirect('consultar_bodega')
        else:
            bodegaForm = BodegaForm(instance=bodega1)
    else:  ##GET
        bodega1 = get_object_or_404(bodega, pk=id)
        bodegaForm = BodegaForm(request.POST or None, instance=bodega1)
    return render(request, "bodega/modificar_bodega.html",{'bodega_m': bodegaForm})


##----------------------------- BODEGA_PRODUCTO --------------##
@login_required(None, "", 'login')
def consultar_bodega_producto (request):
    buscarnombreproductoform = BuscarFecha ()
    bodega_producto1 = None

    if request.method == "POST" :
        buscarnombreproductoform = BuscarFecha ( request.POST or None )
        if buscarnombreproductoform.is_valid () :
            desde = buscarnombreproductoform.cleaned_data['desde']
            hasta = buscarnombreproductoform.cleaned_data['hasta']

            bodega_producto1 = Bodega_producto.objects.filter ( fecha_creacion__range=(desde , hasta) )
    else :
        bodega_producto1 = Bodega_producto.objects.all ()
    #bodega_producto1 =Bodega_producto.objects.all()
    return render(request, "bodega_producto/consultar_bodega_producto.html",{'bodega_producto_ls': bodega_producto1, 'productobusca': buscarnombreproductoform})

@login_required(None, "", 'login')
def crear_bodega_producto (request):
    if request.method == "POST":
        bodega_productoForm = Bodega_productoForm(request.POST)
        if bodega_productoForm.is_valid():
            bodega_productoForm.save()
            return redirect('consultar_bodega_producto')
        else:
            bodega_productoForm = Bodega_productoForm()
    else:
         bodega_productoForm = Bodega_productoForm ()
    return render(request, "bodega_producto/crear_bodega_producto.html",{'bodega_producto_ls': bodega_productoForm})

@login_required(None, "", 'login')
def eliminar_bodega_producto (request,id):
    if request.method == "POST":
        bodega_producto1 = get_object_or_404(Bodega_producto, pk=id)
        bodega_productoForm = Bodega_productoForm(request.POST or None, instance=bodega_producto1)
        if bodega_productoForm.is_valid():
            bodega_producto1.estado = 0
            bodega_producto1.save()
            return redirect('consultar_bodega_producto')
    else:
        bodega_producto1 = get_object_or_404(Bodega_producto, pk=id)
        bodega_productoForm = BodegaForm(request.POST or None, instance=bodega_producto1)
    return render(request, "bodega_producto/eliminar_bodega_producto.html",{'bodega_producto_ls': bodega_productoForm})

@login_required(None, "", 'login')
def modificar_bodega_producto (request,id):
    if request.method == "POST":
        bodega_producto1 = get_object_or_404(Bodega_producto, pk=id)
        bodega_productoForm = Bodega_productoForm(request.POST or None, instance=bodega_producto1)
        if bodega_productoForm.is_valid():
            bodega_productoForm.save()
            return redirect('consultar_bodega_producto')
        else:
            bodega_productoForm = Bodega_productoForm(instance=bodega_producto1)
    else:  ##GET
        bodega_producto1 = get_object_or_404(Bodega_producto, pk=id)
        bodega_productoForm = Bodega_productoForm(request.POST or None, instance=bodega_producto1)
    return render(request, "bodega_producto/modificar_bodega_producto.html",{'bodega_producto_ls': bodega_productoForm})


##----------------------------- CATEGORIA_PRODUCTO --------------##

@login_required(None, "", 'login')
def consultar_categoria_producto (request):
    buscarpersonaform = BuscarNombreFecha ()
    categoriaproductoform = None

    if request.method == "POST" :
        buscarpersonaform = BuscarNombreFecha ( request.POST or None )
        if buscarpersonaform.is_valid () :
            desde = buscarpersonaform.cleaned_data['desde']
            hasta = buscarpersonaform.cleaned_data['hasta']
            nombre = buscarpersonaform.cleaned_data['nombre']

            categoriaproductoform = Categoria_producto.objects.filter (
                Q ( nombre__startswith=nombre ) & Q ( fecha_creacion__range=(desde , hasta) ) )
    else :
         categoriaproductoform = Categoria_producto.objects.all()
    return render(request, "categoria_producto/consultar_categoria_producto.html",{'categoria_producto_ls': categoriaproductoform, 'buscarfechanombre': buscarpersonaform})

@login_required(None, "", 'login')
def crear_categoria_producto (request):

    if request.method == "POST":
        categoria_productoForm = Categoria_productoForm(request.POST)
        if categoria_productoForm.is_valid():
            categoria_productoForm.save()
            return redirect('consultar_categoria_producto')
        else:
           categoria_productoForm = Categoria_productoForm()
    else:
         categoria_productoForm = Categoria_productoForm ()
    return render(request, "categoria_producto/crear_categoria_producto.html",{'categoria_productoForm': categoria_productoForm})


@login_required(None, "", 'login')
def eliminar_categoria_producto (request,id):
    if request.method == "POST":
        categoria_producto1 = get_object_or_404(Categoria_producto, pk=id)
        categoria_productoForm = Categoria_productoForm(request.POST or None, instance=categoria_producto1)
        if categoria_productoForm.is_valid():
            categoria_producto1.estado = 0
            categoria_producto1.save()
            return redirect('consultar_categoria_producto')
    else:
        categoria_producto1 = get_object_or_404(Categoria_producto, pk=id)
        categoria_productoForm = Categoria_productoForm(request.POST or None, instance=categoria_producto1)
    return render(request, "categoria_producto/eliminar_categoria_producto.html",{'categoria_producto_e': categoria_productoForm})

@login_required(None, "", 'login')
def modificar_categoria_producto (request,id):
    if request.method == "POST":
        categoria_producto1 = get_object_or_404(Categoria_producto, pk=id)
        categoria_productoForm = Categoria_productoForm(request.POST or None, instance=categoria_producto1)
        if categoria_productoForm.is_valid():
            categoria_productoForm.save()
            return redirect('consultar_categoria_producto')
        else:
            categoria_productoForm = Categoria_productoForm(instance=categoria_producto1)
    else:  ##GET
        categoria_producto1 = get_object_or_404(Categoria_producto, pk=id)
        categoria_productoForm = Categoria_productoForm(request.POST or None, instance=categoria_producto1)
    return render(request, "categoria_producto/modificar_categoria_producto.html",{'categoria_producto_m': categoria_productoForm})


##----------------------------- DEVOLUCION --------------##

@login_required(None, "", 'login')
def consultar_devolucion(request):
    buscarfechaform = BuscarFecha ()
    devolucion = None

    if request.method == "POST" :
        buscarfechaform = BuscarFecha ( request.POST or None )
        if buscarfechaform.is_valid () :
            desde = buscarfechaform.cleaned_data['desde']
            hasta = buscarfechaform.cleaned_data['hasta']

            devolucion = Devolucion.objects.filter ( fecha_creacion__range=(desde , hasta) )
    else :
        devolucion = Devolucion.objects.all ()
    #devolucion1 = Devolucion.objects.all()
    return render(request, "devolucion/consultar_devolucion.html",{'devolucion_ls': devolucion,'buscarfecha': buscarfechaform})

@login_required(None, "", 'login')
def crear_devolucion(request):
    if request.method == "POST":
        devolucionForm = DevolucionForm(request.POST)
        if devolucionForm.is_valid():
            devolucionForm.save()
            return redirect('consultar_devolucion')
        else:
           devolucionForm = DevolucionForm()
    else:
         devolucionForm = DevolucionForm ()
    return render(request, "devolucion/crear_devolucion.html",{'devolucion_ls': devolucionForm})

@login_required(None, "", 'login')
def eliminar_devolucion(request,id):
    if request.method == "POST":
        devolucion1 = get_object_or_404(Devolucion, pk=id)
        devolucionForm = DevolucionForm(request.POST or None, instance=devolucion1)
        if devolucionForm.is_valid():
            devolucion1.estado = 0
            devolucion1.save()
            return redirect('consultar_devolucion')
    else:
        devolucion1 = get_object_or_404(Devolucion, pk=id)
        devolucionForm = DevolucionForm(request.POST or None, instance=devolucion1)
    return render(request, "devolucion/eliminar_devolucion.html",{'devolucion_ls': devolucionForm})

@login_required(None, "", 'login')
def modificar_devolucion(request,id):
    if request.method == "POST":
        devolucion1 = get_object_or_404(Devolucion, pk=id)
        devolucionForm = DevolucionForm(request.POST or None, instance=devolucion1)
        if devolucionForm.is_valid():
            devolucionForm.save()
            return redirect('consultar_devolucion')
        else:
            devolucionForm = DevolucionForm(instance=devolucion1)
    else:  ##GET
        devolucion1 = get_object_or_404(Devolucion, pk=id)
        devolucionForm = DevolucionForm(request.POST or None, instance=devolucion1)
    return render(request, "devolucion/modificar_devolucion.html",{'devolucion_ls': devolucionForm})


##----------------------------- EGRESO CABECERA --------------##

@login_required(None, "", 'login')
def consultar_egreso_cabecera (request):
    buscarbodeganombreform = BuscarCod()
    egreso_cabecera1 = None

    if request.method == "POST" :
        buscarbodeganombreform = BuscarCod( request.POST or None )
        if buscarbodeganombreform.is_valid () :
            codigo = buscarbodeganombreform.cleaned_data['codigo']
            egreso_cabecera1 = Egreso_cabecera.objects.filter (codigo_documento_eg__iendswith=codigo )
    else :
        egreso_cabecera1 = Egreso_cabecera.objects.all()
    return render(request, "egreso_cabecera/consultar_egreso_cabecera.html",{'egreso_cabecera_ls': egreso_cabecera1, 'buscarcod': buscarbodeganombreform})

@login_required(None, "", 'login')
def crear_egreso_cabecera (request):
    if request.method == "POST":
        egreso_cabeceraForm = Egreso_cabeceraForm(request.POST)
        if egreso_cabeceraForm.is_valid():
            egreso_cabeceraForm.save()
            return redirect ('consultar_egreso_cabecera')
        else:
            egreso_cabeceraForm = Egreso_cabeceraForm()
    else:
         egreso_cabeceraForm = Egreso_cabeceraForm ()
    return render(request, "egreso_cabecera/crear_egreso_cabecera.html",{'egreso_cabecera_c': egreso_cabeceraForm})

def eliminar_egreso_cabecera (request,id):
    if request.method == "POST":
        egreso_cabecera1 = get_object_or_404(Egreso_cabecera, pk=id)
        egreso_cabeceraForm = Egreso_cabeceraForm(request.POST or None, instance=egreso_cabecera1)
        if egreso_cabeceraForm.is_valid():
            egreso_cabecera1.estado = 0
            egreso_cabecera1.save()
            return redirect('consultar_egreso_cabecera')
    else:
        egreso_cabecera1 = get_object_or_404(Egreso_cabecera, pk=id)
        egreso_cabeceraForm = Egreso_cabeceraForm(request.POST or None, instance=egreso_cabecera1)
    return render(request, "egreso_cabecera/eliminar_egreso_cabecera.html",{'egreso_cabecera_e':egreso_cabeceraForm})

@login_required(None, "", 'login')
def modificar_egreso_cabecera (request,id):
    if request.method == "POST":
        egreso_cabecera1 = get_object_or_404(Egreso_cabecera, pk=id)
        egreso_cabeceraForm = Egreso_cabeceraForm(request.POST or None, instance=egreso_cabecera1)
        if egreso_cabeceraForm.is_valid():
            egreso_cabeceraForm.save()
            return redirect('consultar_egreso_cabecera')
        else:
            egreso_cabeceraForm = Egreso_cabeceraForm(instance=egreso_cabecera1)
    else:  ##GET
        egreso_cabecera1 = get_object_or_404(Egreso_cabecera, pk=id)
        egreso_cabeceraForm = Egreso_cabeceraForm(request.POST or None, instance=egreso_cabecera1)
    return render(request, "egreso_cabecera/modificar_egreso_cabecera.html",{'egreso_cabecera_m':egreso_cabeceraForm})


##----------------------------- EGRESO DETALLE --------------##

@login_required(None, "", 'login')
def consultar_egreso_detalle (request):
    buscarfechaform = BuscarFecha ()
    egreso_detalle1 = None

    if request.method == "POST" :
        buscarfechaform = BuscarFecha ( request.POST or None )
        if buscarfechaform.is_valid () :
            desde = buscarfechaform.cleaned_data['desde']
            hasta = buscarfechaform.cleaned_data['hasta']

            egreso_detalle1 = Egreso_detalle.objects.filter ( fecha_creacion__range=(desde , hasta) )
    else :
        egreso_detalle1 = Egreso_detalle.objects.all()

    return render(request, "egreso_detalle/consultar_egreso_detalle.html",{'egreso_detalle_ls': egreso_detalle1,'buscafecha': buscarfechaform})

@login_required(None, "", 'login')
def crear_egreso_detalle (request):
    if request.method == "POST":
        egreso_detalleForm = Egreso_detalleForm(request.POST)
        if egreso_detalleForm.is_valid():
            egreso_detalleForm.save()
            return redirect('consultar_egreso_detalle')
        else:
          egreso_detalleForm = Egreso_detalleForm()
    else:
         egreso_detalleForm = Egreso_detalleForm ()
    return render(request, "egreso_detalle/crear_egreso_detalle.html",{'egreso_detalle_form': egreso_detalleForm})

@login_required(None, "", 'login')
def eliminar_egreso_detalle (request,id):
    if request.method == "POST":
        egreso_detalle1 = get_object_or_404(Egreso_detalle, pk=id)
        egreso_detalleForm = Egreso_detalleForm(request.POST or None, instance=egreso_detalle1)
        if egreso_detalleForm.is_valid():
            egreso_detalle1.estado = 0
            egreso_detalle1.save()
            return redirect('consultar_egreso_detalle')
    else:
        egreso_detalle1 = get_object_or_404(Egreso_detalle, pk=id)
        egreso_detalleForm = Egreso_detalleForm(request.POST or None, instance=egreso_detalle1)
    return render(request, "egreso_detalle/eliminar_egreso_detalle.html",{'egreso_detalle_ls': egreso_detalleForm})

@login_required(None, "", 'login')
def modificar_egreso_detalle (request,id):
    if request.method == "POST":
        egreso_detalle1 = get_object_or_404(Egreso_detalle, pk=id)
        egreso_detalleForm = Egreso_detalleForm(request.POST or None, instance=egreso_detalle1)
        if egreso_detalleForm.is_valid():
            egreso_detalleForm.save()
            return redirect('consultar_egreso_detalle')
        else:
            egreso_detalleForm = Egreso_detalleForm(instance=egreso_detalle1)
    else:  ##GET
        egreso_detalle1 = get_object_or_404(Egreso_detalle, pk=id)
        egreso_detalleForm = Egreso_detalleForm(request.POST or None, instance=egreso_detalle1)
    return render(request, "egreso_detalle/modificar_egreso_detalle.html",{'egreso_detalle_ls':egreso_detalleForm})



##----------------------------- INGRESO DETALLE--------------##

@login_required(None, "", 'login')
def  consultar_ingreso_detalle (request):
    buscarfechaform = BuscarFecha ()
    ingreso_detalle1 = None

    if request.method == "POST" :
        buscarfechaform = BuscarFecha ( request.POST or None )
        if buscarfechaform.is_valid () :
            desde = buscarfechaform.cleaned_data['desde']
            hasta = buscarfechaform.cleaned_data['hasta']

            ingreso_detalle1 = ingreso_detalle.objects.filter ( fecha_creacion__range=(desde , hasta) )
    else :
        ingreso_detalle1 = ingreso_detalle.objects.all()

    return render(request, "ingreso_detalle/consultar_ingreso_detalle.html",{'ingreso_detalle_ls':ingreso_detalle1,'buscafecha':buscarfechaform})

@login_required(None, "", 'login')
def crear_ingreso_detalle (request):
    if request.method == "POST":
        ingreso_detalleForm = Ingreso_detalleForm(request.POST)
        if ingreso_detalleForm.is_valid():
            ingreso_detalleForm.save()
            return redirect('consultar_ingreso_detalle')
        else:
            ingreso_detalleForm = Ingreso_detalleForm()
    else:
         ingreso_detalleForm = Ingreso_detalleForm ()
    return render(request, "ingreso_detalle/crear_ingreso_detalle.html",{'ingreso_detalle_ls':ingreso_detalleForm})

@login_required(None, "", 'login')
def eliminar_ingreso_detalle (request,id):
    if request.method == "POST":
        ingreso_detalle1 = get_object_or_404(ingreso_detalle, pk=id)
        ingreso_detalleForm = Ingreso_detalleForm(request.POST or None, instance=ingreso_detalle1)
        if ingreso_detalleForm.is_valid():
            ingreso_detalle1.estado = 0
            ingreso_detalle1.save()
            return redirect('consultar_ingreso_detalle')
    else:
        ingreso_detalle1 = get_object_or_404(ingreso_detalle, pk=id)
        ingreso_detalleForm = Ingreso_detalleForm(request.POST or None, instance=ingreso_detalle1)
    return render(request, "ingreso_detalle/eliminar_ingreso_detalle.html",{'ingreso_detalle_ls':ingreso_detalleForm})

@login_required(None, "", 'login')
def modificar_ingreso_detalle (request,id):
    if request.method == "POST":
        ingreso_detalle1 = get_object_or_404(ingreso_detalle, pk=id)
        ingreso_detalleForm = Ingreso_detalleForm(request.POST or None, instance=ingreso_detalle1)
        if ingreso_detalleForm.is_valid():
            ingreso_detalleForm.save()
            return redirect('consultar_ingreso_detalle')
        else:
            ingreso_detalleForm = Ingreso_detalleForm(instance=ingreso_detalle1)
    else:  ##GET
        ingreso_detalle1 = get_object_or_404(ingreso_detalle, pk=id)
        ingreso_detalleForm = Ingreso_detalleForm(request.POST or None, instance=ingreso_detalle1)
    return render(request, "ingreso_detalle/modificar_ingreso_detalle.html",{'ingreso_detalle_ls':ingreso_detalleForm})


##----------------------------- PERSONA --------------##

@login_required(None, "", 'login')
def consultar_persona( request ) :
    buscarpersonaform = BuscarNombreFecha()
    persona = None

    if request.method =="POST":
        buscarpersonaform = BuscarNombreFecha(request.POST or None)
        if buscarpersonaform.is_valid():
            desde = buscarpersonaform.cleaned_data['desde']
            hasta = buscarpersonaform.cleaned_data['hasta']
            nombre = buscarpersonaform.cleaned_data['nombre']

            persona = Persona.objects.filter (Q(nombre__startswith=nombre) & Q(fecha_creacion__range=(desde, hasta)))
    else:
        persona= Persona.objects.all ()

    return render ( request , "persona/consultar_persona.html" , {'persona_ls' : persona, 'buscarpersona' : buscarpersonaform } )


@login_required(None, "", 'login')
def crear_persona( request ) :
    if request.method == "POST" :
        personaForm = PersonaForm ( request.POST )
        if personaForm.is_valid () :
            personaForm.save ()
            return redirect ( 'consultar_persona' )
        else :
            personaForm = PersonaForm ()
    else :
        personaForm = PersonaForm ()

    return render ( request , "persona/crear_persona.html" , {'persona' : personaForm} )

@login_required(None, "", 'login')
def eliminar_persona(request, id ):
    if request.method == "POST" :
        personan = get_object_or_404(Persona, pk = id)
        personaForm = PersonaForm(request.POST or None, instance=personan)
        if personaForm.is_valid():
            personan.estado = 0
            personan.save()
            return redirect('consultar_persona')

    else :
        personan = get_object_or_404(Persona, pk = id)
        personaForm = PersonaForm(request.POST or None, instance=personan)
    return render(request,"persona/eliminar_persona.html",{'personaForm' : personaForm})


@login_required(None, "", 'login')
def modificar_persona( request ,id ):
    if request.method == "POST":
        personan = get_object_or_404(Persona, pk=id)
        personaForm=PersonaForm( request.POST or None,instance = personan)
        if personaForm.is_valid():
            personaForm.save()
            return redirect('consultar_persona')
        else :
            personaForm = PersonaForm (instance=personan)
    else :  ##GET
        personan = get_object_or_404(Persona, pk=id)
        personaForm = PersonaForm(request.POST or None, instance = personan)
    return render (request, "persona/modificar_persona.html" ,{'personaForm' : personaForm} )


##----------------------------- PRODUCTO --------------##

@login_required(None, "", 'login')
def consultar_producto(request):
    buscarnombreproductoform = BuscarNombreProductoForm ()
    Producto = None

    if request.method == "POST" :
        buscarnombreproductoform = BuscarNombreProductoForm ( request.POST or None )
        if buscarnombreproductoform.is_valid () :
            nombre = buscarnombreproductoform.cleaned_data['nombre']
            Producto = producto.objects.filter ( nombre__icontains=nombre  )
    else :
        Producto = producto.objects.all ()
    #producto1 = producto.objects.all()
    return render(request, "producto/consultar_producto.html",{'producto_ls': Producto, 'buscarproducto': buscarnombreproductoform})

@login_required(None, "", 'login')
def crear_producto(request):
    if request.method == "POST":
        productoForm = ProductoForm(request.POST)
        if productoForm.is_valid():
            productoForm.save()
            return redirect('consultar_producto')
        else:
            productoForm = ProductoForm()
    else:
         productoForm = ProductoForm ()
    return render(request, "producto/crear_producto.html",{'productoform': productoForm})

@login_required(None, "", 'login')
def eliminar_producto(request,id):
    if request.method == "POST":
        producto1 = get_object_or_404(producto, pk=id)
        productoForm = ProductoForm(request.POST or None, instance=producto1)
        if productoForm.is_valid():
            producto1.estado = 0
            producto1.save()
            return redirect('consultar_producto')
    else:
        producto1 = get_object_or_404(producto, pk=id)
        productoForm = ProductoForm(request.POST or None, instance=producto1)
    return render(request, "producto/eliminar_producto.html",{'producto_e': productoForm})

@login_required(None, "", 'login')
def modificar_producto(request,id):
    if request.method == "POST":
        producto1 = get_object_or_404(producto, pk=id)
        productoForm = ProductoForm(request.POST or None, instance=producto1)
        if productoForm.is_valid():
            productoForm.save()
            return redirect('consultar_producto')
        else:
            productoForm = ProductoForm(instance=producto1)
    else:  ##GET
        producto1 = get_object_or_404(producto, pk=id)
        productoForm = ProductoForm(request.POST or None, instance=producto1)
    return render(request, "producto/modificar_producto.html",{'producto_m': productoForm})


##----------------------------- PROVEEDOR --------------##

@login_required(None, "", 'login')
def consultar_proveedor(request):
    buscarproveedorrucform = BuscarRucProveedorForm ()
    proveedor1 = None

    if request.method == "POST" :
        buscarproveedorrucform = BuscarRucProveedorForm ( request.POST or None )
        if buscarproveedorrucform.is_valid () :
            ruc = buscarproveedorrucform.cleaned_data['ruc']
            proveedor1 = proveedor.objects.filter ( ruc__icontains=ruc )
    else :
        proveedor1 = proveedor.objects.all ()
    #proveedor1 = proveedor.objects.all()
    return render(request, "proveedor/consultar_proveedor.html",{'proveedor_ls': proveedor1, 'buscarruc': buscarproveedorrucform})

@login_required(None, "", 'login')
def crear_proveedor(request):
    if request.method == "POST":
        proveedorForm = ProveedorForm(request.POST)
        if proveedorForm.is_valid():
            proveedorForm.save()
            return redirect('consultar_proveedor')
        else:
            proveedorForm = ProveedorForm()
    else:
         proveedorForm = ProveedorForm ()
    return render(request, "proveedor/crear_proveedor.html",{'proveedor_ls': proveedorForm})

@login_required(None, "", 'login')
def eliminar_proveedor(request,id):
    if request.method == "POST":
        proveedor1 = get_object_or_404(proveedor, pk=id)
        proveedorForm = ProveedorForm(request.POST or None, instance=proveedor1)
        if proveedorForm.is_valid():
            proveedor1.estado = 0
            proveedor1.save()
            return redirect('consultar_proveedor')
    else:
        proveedor1 = get_object_or_404(proveedor, pk=id)
        proveedorForm = ProveedorForm(request.POST or None, instance=proveedor1)
    return render(request, "proveedor/eliminar_proveedor.html",{'proveedor_ls': proveedorForm})

@login_required(None, "", 'login')
def modificar_proveedor(request,id):
    if request.method == "POST":
        proveedor1 = get_object_or_404(proveedor, pk=id)
        proveedorForm = ProveedorForm(request.POST or None, instance=proveedor1)
        if proveedorForm.is_valid():
            proveedorForm.save()
            return redirect('consultar_proveedor')
        else:
            proveedorForm = ProveedorForm(instance=proveedor1)
    else:  ##GET
        proveedor1 = get_object_or_404(proveedor, pk=id)
        proveedorForm = ProveedorForm(request.POST or None, instance=proveedor1)
    return render(request, "proveedor/modificar_proveedor.html",{'proveedor_ls': proveedorForm})


##----------------------------- ROL PERSONA--------------##


@login_required(None, "", 'login')
def consultar_rol_persona (request):
    buscar_rolpersonaform = BuscarPersonaForm ()
    rol_persona1 = None

    if request.method == "POST" :
        buscar_rolpersonaform = BuscarPersonaForm ( request.POST or None )
        if buscar_rolpersonaform.is_valid () :
            desde = buscar_rolpersonaform.cleaned_data['desde']
            hasta = buscar_rolpersonaform.cleaned_data['hasta']

            rol_persona1 = rol_persona.objects.filter ( fecha_creacion__range=(desde , hasta) )
    else :
        rol_persona1 = rol_persona.objects.all ()
    return render(request, "rol_persona/consultar_rol_persona.html",{'rol_persona_ls': rol_persona1, 'buscar_rolpersona': buscar_rolpersonaform})

@login_required(None, "", 'login')
def crear_rol_persona (request):
    if request.method == "POST":
        rol_personaForm = Rol_personaForm(request.POST)
        if rol_personaForm.is_valid():
            rol_personaForm.save()
            return redirect('consultar_rol_persona')
        else:
            rol_personaForm = Rol_personaForm()
    else:
         rol_personaForm = Rol_personaForm ()
    return render(request, "rol_persona/crear_rol_persona.html",{'rolpersona': rol_personaForm})

@login_required(None, "", 'login')
def eliminar_rol_persona (request,id):
    if request.method == "POST":
        rol_persona1 = get_object_or_404(rol_persona, pk=id)
        rol_personaForm = Rol_personaForm(request.POST or None, instance=rol_persona1)
        if rol_personaForm.is_valid():
            rol_persona1.estado = 0
            rol_persona1.save()
            return redirect('consultar_rol_persona')
    else:
        rol_persona1 = get_object_or_404(rol_persona, pk=id)
        rol_personaForm = Rol_personaForm(request.POST or None, instance=rol_persona1)
    return render(request, "rol_persona/eliminar_rol_persona.html",{'rol_persona_e': rol_personaForm})

@login_required(None, "", 'login')
def modificar_rol_persona (request,id):
    if request.method == "POST":
        rol_persona1 = get_object_or_404(rol_persona, pk=id)
        rol_personaForm = Rol_personaForm(request.POST or None, instance=rol_persona1)
        if rol_personaForm.is_valid():
            rol_personaForm.save()
            return redirect('consultar_rol_persona')
        else:
            rol_personaForm = Rol_personaForm(instance=rol_persona1)
    else:  ##GET
        rol_persona1 = get_object_or_404(rol_persona, pk=id)
        rol_personaForm = Rol_personaForm(request.POST or None, instance=rol_persona1)
    return render(request, "rol_persona/modificar_rol_persona.html",{'rol_persona_m': rol_personaForm})


##----------------------------- ROL ciudad -------------##


@login_required(None, "", 'login')
def consultar_ciudad( request ) :
    buscarfechaform = BuscarFecha()
    Ciudad = None

    if request.method == "POST" :
        buscarfechaform = BuscarFecha ( request.POST or None )
        if buscarfechaform.is_valid () :
            desde = buscarfechaform.cleaned_data['desde']
            hasta = buscarfechaform.cleaned_data['hasta']


            Ciudad = ciudad.objects.filter ( fecha_creacion__range=(desde , hasta) )
    else :
        Ciudad = ciudad.objects.all ()

    #Ciudad = ciudad.objects.all()
    return render ( request , "ciudad/consultar_ciudad.html",{'ciudad_consul': Ciudad, 'buscarfecha': buscarfechaform } )

@login_required(None, "", 'login')
def crear_ciudad( request ) :
    if request.method == "POST" :
        ciudadform = CiudadForm ( request.POST )
        if ciudadform.is_valid () :
            ciudadform.save ()
            return redirect ( 'consultar_ciudad' )
        else :
            ciudadform = CiudadForm ()
    else :
        ciudadform = CiudadForm ()

    return render ( request , "ciudad/crear_ciudad.html" ,{'ciudad_crear': ciudadform} )

@login_required(None, "", 'login')
def eliminar_ciudad( request, id ) :

    if request.method == "POST":
        Ciudad = get_object_or_404(ciudad, pk=id)
        ciudadform = CiudadForm(request.POST or None, instance=Ciudad)
        if ciudadform.is_valid():
            Ciudad.estado = 0
            Ciudad.save()
            return redirect('consultar_ciudad')
    else:
        Ciudad = get_object_or_404(ciudad, pk=id)
        ciudadform = CiudadForm(request.POST or None, instance=Ciudad)


    return render ( request , "ciudad/eliminar_ciudad.html",{'ciudad_e': ciudadform} )

@login_required(None, "", 'login')
def modificar_ciudad( request, id ) :

    if request.method == "POST" :
        Ciudad = get_object_or_404 ( ciudad , pk=id )
        ciudadform = CiudadForm ( request.POST or None , instance=Ciudad )
        if ciudadform.is_valid () :
            ciudadform.save ()
            return redirect ( 'consultar_ciudad' )
        else :
            ciudadform = CiudadForm ( instance=Ciudad )
    else :  ##GET
        Ciudad = get_object_or_404 ( ciudad , pk=id )
        ciudadform = CiudadForm ( request.POST or None , instance=Ciudad )
    return render ( request , "ciudad/modificar_ciudad.html" ,{'ciudad_m': ciudadform} )


##----------------------------- unidad de medida -------------##

@login_required(None, "", 'login')
def consultar_categoria_bodega (request):
    buscarpersonaform = BuscarNombreFecha ()
    categoriabodega = None

    if request.method == "POST" :
        buscarpersonaform = BuscarNombreFecha ( request.POST or None )
        if buscarpersonaform.is_valid () :
            desde = buscarpersonaform.cleaned_data['desde']
            hasta = buscarpersonaform.cleaned_data['hasta']
            nombre = buscarpersonaform.cleaned_data['nombre']

            categoriabodega = CategoriaBodega.objects.filter (
                Q ( nombre__startswith=nombre ) & Q ( fecha_creacion__range=(desde , hasta) ) )
    else :
        categoriabodega = CategoriaBodega.objects.all ()
    #categoriabodega = CategoriaBodega.objects.all()
    return render(request, "categoria_bodega/consultar_categoria_bodega.html",{'categoria_bodega_ls': categoriabodega, 'buscarfechanombre': buscarpersonaform})

@login_required(None, "", 'login')
def crear_categoria_bodega(request):
    if request.method == "POST" :
        categoriabodegaform = Categoria_bodegaForm ( request.POST )
        if categoriabodegaform.is_valid () :
            categoriabodegaform.save ()
            return redirect ( 'consultar_categoria_bodega' )
        else :
            categoriabodegaform = Categoria_bodegaForm ()
    else :
        categoriabodegaform = Categoria_bodegaForm ()
    return render(request, "categoria_bodega/crear_categoria_bodega.html",{'categoriabodegaForm': categoriabodegaform})

@login_required(None, "", 'login')
def eliminar_categoria_bodega(request,id):

    if request.method == "POST":
        categoriabodega1 = get_object_or_404(CategoriaBodega, pk=id)
        categoriabodegaform = Categoria_bodegaForm(request.POST or None, instance=categoriabodega1)
        if categoriabodegaform.is_valid():
            categoriabodega1.estado = 0
            categoriabodega1.save()
            return redirect('consultar_categoria_bodega')
    else:
        categoriabodega1 = get_object_or_404(CategoriaBodega, pk=id)
        categoriabodegaform = Categoria_bodegaForm(request.POST or None, instance=categoriabodega1)

    return render(request, "categoria_bodega/eliminar_categoria_bodega.html",{'categoria_bodega_elim': categoriabodegaform})

@login_required(None, "", 'login')
def modificar_categoria_bodega(request,id):
    if request.method == "POST":
        categoriabodega = get_object_or_404(CategoriaBodega, pk=id)
        categoriabodegaform=Categoria_bodegaForm( request.POST or None,instance = categoriabodega)
        if categoriabodegaform.is_valid():
            categoriabodegaform.save()
            return redirect('consultar_categoria_bodega')
        else :
            categoriabodegaform = Categoria_bodegaForm (instance=categoriabodega)
    else :  ##GET
        categoriabodega = get_object_or_404(CategoriaBodega, pk=id)
        categoriabodegaform = Categoria_bodegaForm(request.POST or None, instance = categoriabodega)
    return render(request, "categoria_bodega/modificar_categoria_bodega.html",{'categoria_bodega_mod': categoriabodegaform})


##----------------------------- unidad de marca -------------##


@login_required(None, "", 'login')
def  consultar_marca(request):
    buscarfechaform = BuscarFecha ()
    marca = None

    if request.method == "POST" :
        buscarfechaform = BuscarFecha ( request.POST or None )
        if buscarfechaform.is_valid () :
            desde = buscarfechaform.cleaned_data['desde']
            hasta = buscarfechaform.cleaned_data['hasta']

            marca = Marca.objects.filter ( fecha_creacion__range=(desde , hasta) )
    else :
        marca = Marca.objects.all ()

    #marca1 = Marca.objects.all()
    return render(request, "marca/consultar_marca.html",{'marca_ls': marca, 'buscarfecha': buscarfechaform} )

@login_required(None, "", 'login')
def crear_marca (request):
    if request.method == "POST":
        marcaForm = MarcaForm(request.POST)
        if marcaForm.is_valid():
            marcaForm.save()
            return redirect('consultar_marca')
        else:
            marcaForm = MarcaForm()
    else:
         marcaForm = MarcaForm ()
    return render(request, "marca/crear_marca.html",{'marca_ls': marcaForm})

@login_required(None, "", 'login')
def eliminar_marca (request,id):
    if request.method == "POST":
        marca1 = get_object_or_404(Marca, pk=id)
        marcaForm = MarcaForm(request.POST or None, instance=marca1)
        if marcaForm.is_valid():
            marca1.estado = 0
            marca1.save()
            return redirect('consultar_marca')
    else:
        marca1 = get_object_or_404(Marca, pk=id)
        marcaForm = MarcaForm(request.POST or None, instance=marca1)
    return render(request, "marca/eliminar_marca.html",{'marca_ls': marcaForm})

@login_required(None, "", 'login')
def modificar_marca (request,id):
    if request.method == "POST":
        marca1 = get_object_or_404(Marca, pk=id)
        marcaForm = MarcaForm(request.POST or None, instance=marca1)
        if marcaForm.is_valid():
            marcaForm.save()
            return redirect('consultar_marca')
        else:
            marcaForm = MarcaForm(instance=marca1)
    else:  ##GET
        marca1 = get_object_or_404(Marca, pk=id)
        marcaForm = MarcaForm(request.POST or None, instance=marca1)
    return render(request, "marca/modificar_marca.html",{'marca_m': marcaForm})


##----------------------------- INGRESO CABECERA--------------##

@login_required(None, "", 'login')
def consultar_ingreso_cabecera (request):
    buscarbodeganombreform = BuscarCod ()
    Ingreso = None

    if request.method == "POST" :
        buscarbodeganombreform = BuscarCod ( request.POST or None )
        if buscarbodeganombreform.is_valid () :
            codigo = buscarbodeganombreform.cleaned_data['codigo']
            Ingreso = ingreso_cabecera.objects.filter ( codigo_documento_eg__iendswith=codigo )
    else :
        Ingreso = ingreso_cabecera.objects.all()

    return render(request, "ingreso_cabecera/consultar_ingreso_cabecera.html",{'ingre_consul':Ingreso, 'buscarcod': buscarbodeganombreform})

@login_required(None, "", 'login')
def crear_ingreso_cabecera(request):
    if request.method == "POST" :
        ingresocaForm = Ingreso_cabeceraForm(request.POST)
        if ingresocaForm.is_valid () :
            ingresocaForm.save ()
            return redirect ('consultar_ingreso_cabecera')
        else :
            ingresocaForm = Ingreso_cabeceraForm()
    else :
        ingresocaForm = Ingreso_cabeceraForm()

    return render(request,"ingreso_cabecera/crear_ingreso_cabecera.html",{'ingreso_cabecera_c':ingresocaForm})

@login_required(None, "", 'login')
def eliminar_ingreso_cabecera (request,id):
    if request.method == "POST":
        ingreso_cabecera1 = get_object_or_404(ingreso_cabecera, pk=id)
        ingreso_cabeceraForm = Ingreso_cabeceraForm(request.POST or None, instance=ingreso_cabecera1)
        if ingreso_cabeceraForm.is_valid():
            ingreso_cabecera1.estado = 0
            ingreso_cabecera1.save()
            return redirect('consultar_ingreso_cabecera')
    else:
        ingreso_cabecera1 = get_object_or_404(ingreso_cabecera, pk=id)
        ingreso_cabeceraForm = Ingreso_cabeceraForm(request.POST or None, instance=ingreso_cabecera1)
    return render(request, "ingreso_cabecera/eliminar_ingreso_cabecera.html",{'ingreso_cabecera_e': ingreso_cabeceraForm})

@login_required(None, "", 'login')
def modificar_ingreso_cabecera (request,id):
    if request.method == "POST":
        ingreso_cabecera1 = get_object_or_404(ingreso_cabecera, pk=id)
        ingreso_cabeceraForm = Ingreso_cabeceraForm(request.POST or None, instance=ingreso_cabecera1)
        if ingreso_cabeceraForm.is_valid():
            ingreso_cabeceraForm.save()
            return redirect('consultar_ingreso_cabecera')
        else:
            ingreso_cabeceraForm = Ingreso_cabeceraForm(instance=ingreso_cabecera1)
    else:  ##GET
        ingreso_cabecera1 = get_object_or_404(ingreso_cabecera, pk=id)
        ingreso_cabeceraForm = Ingreso_cabeceraForm(request.POST or None, instance=ingreso_cabecera1)
    return render(request, "ingreso_cabecera/modificar_ingreso_cabecera.html",{'ingreso_cabecera_m': ingreso_cabeceraForm})


