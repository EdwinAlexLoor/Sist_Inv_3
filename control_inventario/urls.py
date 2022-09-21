"""Sist_Inv URL Configuration

ESTE ARCHIVO ES DE LA APLICACION CONTROL_INVENTARIO.
"""

from django.urls import path
from . import views

urlpatterns = [
    ##path('ruta1/', views.MiPrimeraFuncion),
    path('ruta1/', views.base2),


    ##----------- Ruta Para Bodega -----------##

    path('consultar_bodega/', views.consultar_bodega, name="consultar_bodega"),
    path('crear_bodega/', views.crear_bodega, name="crear_bodega"),
    path('eliminar_bodega/<int:id>', views.eliminar_bodega,name="eliminar_bodega" ),
    path('modificar_bodega/<int:id>', views.modificar_bodega, name = "modificar_bodega"),

    ##----------- Ruta Para Bodega Producto -----------##

    path('consultar_bodega_producto/', views.consultar_bodega_producto, name = "consultar_bodega_producto"),
    path('crear_bodega_producto/', views.crear_bodega_producto, name = "crear_bodega_producto"),
    path('eliminar_bodega_producto/<int:id>', views.eliminar_bodega_producto, name = "eliminar_bodega_producto"),
    path('modificar_bodega_producto/<int:id>', views.modificar_bodega_producto, name = "modificar_bodega_producto"),

    ##----------- Ruta Para Categoria Producto -----------##

    path ( 'consultar_categoria_producto/' , views.consultar_categoria_producto, name = "consultar_categoria_producto" ) ,
    path ( 'crear_categoria_producto/' , views.crear_categoria_producto, name = "crear_categoria_producto") ,
    path ( 'eliminar_categoria_producto/<int:id>' , views.eliminar_categoria_producto, name = "eliminar_categoria_producto" ) ,
    path ( 'modificar_categoria_producto/<int:id>' , views.modificar_categoria_producto, name = "modificar_categoria_producto" ) ,

    ##----------- Ruta Para Entidad devolucion -----------##

    path('consultar_devolucion/', views.consultar_devolucion, name = "consultar_devolucion"),
    path('crear_devolucion/', views.crear_devolucion, name = "crear_devolucion"),
    path('eliminar_devolucion/<int:id>', views.eliminar_devolucion, name = "eliminar_devolucion"),
    path('modificar_devolucion/<int:id>', views.modificar_devolucion, name = "modificar_devolucion"),

    ##----------- Ruta Para EGRESO CABECERA -----------##

    path('consultar_egreso_cabecera/', views.consultar_egreso_cabecera, name = "consultar_egreso_cabecera"),
    path('crear_egreso_cabecera/', views.crear_egreso_cabecera, name = "crear_egreso_cabecera"),
    path('eliminar_egreso_cabecera/<int:id>', views.eliminar_egreso_cabecera, name = "eliminar_egreso_cabecera"),
    path('modificar_egreso_cabecera/<int:id>', views.modificar_egreso_cabecera, name = "modificar_egreso_cabecera"),

    ##----------- Ruta Para EGRESO detalle -----------##

    path('consultar_egreso_detalle/', views.consultar_egreso_detalle, name = "consultar_egreso_detalle"),
    path('crear_egreso_detalle/', views.crear_egreso_detalle, name = "crear_egreso_detalle"),
    path('eliminar_egreso_detalle/<int:id>', views.eliminar_egreso_detalle, name = "eliminar_egreso_detalle"),
    path('modificar_egreso_detalle/<int:id>', views.modificar_egreso_detalle, name = "modificar_egreso_detalle"),

    ##----------- Ruta Para INGRESO CABECERA -----------##

    path('consultar_ingreso_cabecera/', views.consultar_ingreso_cabecera, name = "consultar_ingreso_cabecera"),
    path('crear_ingreso_cabecera/', views.crear_ingreso_cabecera, name = "crear_ingreso_cabecera"),
    path('eliminar_ingreso_cabecera/<int:id>', views.eliminar_ingreso_cabecera, name = "eliminar_ingreso_cabecera"),
    path('modificar_ingreso_cabecera/<int:id>', views.modificar_ingreso_cabecera, name = "modificar_ingreso_cabecera"),


    ##----------- Ruta Para INGRESO DETALLE -----------##

    path('consultar_ingreso_detalle/', views.consultar_ingreso_detalle, name = "consultar_ingreso_detalle"),
    path('crear_ingreso_detalle/', views.crear_ingreso_detalle, name = "crear_ingreso_detalle"),
    path('eliminar_ingreso_detalle/<int:id>', views.eliminar_ingreso_detalle, name = "eliminar_ingreso_detalle"),
    path('modificar_ingreso_detalle/<int:id>', views.modificar_ingreso_detalle, name = "modificar_ingreso_detalle"),

##----------- Ruta Para PERSONA -----------##

    path('consultar_persona/', views.consultar_persona, name="consultar_persona"),
    path('crear_persona/', views.crear_persona, name="crear_persona"),
    path('eliminar_persona/<int:id>', views.eliminar_persona, name="eliminar_persona"),
    path('modificar_persona/<int:id>', views.modificar_persona, name="modificar_persona"),

    ##----------- Ruta Para Entidad producto -----------##

    path ( 'consultar_producto/' , views.consultar_producto, name = "consultar_producto" ) ,
    path ( 'crear_producto/' , views.crear_producto , name = "crear_producto") ,
    path ( 'eliminar_producto/<int:id>' , views.eliminar_producto , name = "eliminar_producto") ,
    path ( 'modificar_producto/<int:id>' , views.modificar_producto , name = "modificar_producto") ,

    ##----------- Ruta Para Entidad proveedor -----------##

    path ( 'consultar_proveedor/' , views.consultar_proveedor , name = "consultar_proveedor") ,
    path ( 'crear_proveedor/' , views.crear_proveedor , name = "crear_proveedor") ,
    path ( 'eliminar_proveedor/<int:id>' , views.eliminar_proveedor, name = "eliminar_proveedor" ) ,
    path ( 'modificar_proveedor/<int:id>' , views.modificar_proveedor, name = "modificar_proveedor" ) ,


    ##----------- Ruta Para Entidad rol persona -----------##

    path('consultar_rol_persona/', views.consultar_rol_persona, name = "consultar_rol_persona"),
    path('crear_rol_persona/', views.crear_rol_persona, name = "crear_rol_persona"),
    path('eliminar_rol_persona/<int:id>', views.eliminar_rol_persona, name = "eliminar_rol_persona"),
    path('modificar_rol_persona/<int:id>', views.modificar_rol_persona, name = "modificar_rol_persona"),

    ##----------- Ruta Para Stock -----------##

    path ( 'consultar_ciudad/' , views.consultar_ciudad , name="consultar_ciudad" ) ,
    path ( 'crear_ciudad/' , views.crear_ciudad , name="crear_ciudad" ) ,
    path ( 'eliminar_ciudad/<int:id>' , views.eliminar_ciudad , name="eliminar_ciudad" ) ,
    path ( 'modificar_ciudad/<int:id>' , views.modificar_ciudad , name="modificar_ciudad" ) ,

    ##----------- Ruta Para _categoria_bodega -----------##

    path ( 'consultar_categoria_bodega/' , views.consultar_categoria_bodega, name="consultar_categoria_bodega" ) ,
    path ( 'crear_categoria_bodega/' , views.crear_categoria_bodega, name="crear_categoria_bodega" ) ,
    path ( 'eliminar_categoria_bodega/<int:id>' , views.eliminar_categoria_bodega, name="eliminar_categoria_bodega" ) ,
    path ( 'modificar_categoria_bodega/<int:id>' , views.modificar_categoria_bodega, name="modificar_categoria_bodega" ) ,

    ##----------- Ruta Para marca -----------##

    path ( 'consultar_marca/' , views.consultar_marca , name="consultar_marca" ) ,
    path ( 'crear_marca/' , views.crear_marca , name="crear_marca" ) ,
    path ( 'eliminar_marca/<int:id>' , views.eliminar_marca, name="eliminar_marca" ) ,
    path ( 'modificar_marca/<int:id>' , views.modificar_marca , name="modificar_marca" ) ,

    path('exportarListaPersonaPdf/', views.exportarListaPersonaPdf, name="exportarListaPersonaPdf"),
    path('exportarListaProductoPdf/', views.exportarListaProductoPdf, name="exportarListaProductoPdf"),

]
