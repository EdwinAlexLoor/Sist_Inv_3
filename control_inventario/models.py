from django.db import models

# Create your models here.
class ciudad(models.Model):
    nombre = models.CharField(max_length=125)


    fecha_creacion = models.DateTimeField(auto_now_add=True)
    fecha_modificacion = models.DateTimeField(auto_now=True)
    usuario_creacion = models.CharField(max_length=15)
    usuario_modificacion = models.CharField(max_length=15)
    estado = models.IntegerField(default=1)

    class Meta:
        db_table = "inv_ciudad"
        verbose_name = "Ciudad"
        verbose_name_plural = "Ciudades"
        ordering = ['fecha_creacion']

    def __str__(self):
        return '{}'.format(self.nombre)


class CategoriaBodega(models.Model):
    nombre = models.CharField(max_length=125)
    descripcion_catbog = models.CharField(max_length=250)

    fecha_creacion = models.DateTimeField(auto_now_add=True)
    fecha_modificacion = models.DateTimeField(auto_now=True)
    usuario_creacion = models.CharField(max_length=15)
    usuario_modificacion = models.CharField(max_length=15)
    estado = models.IntegerField(default=1)

    class Meta:
        db_table = "inv_categoria_bodega"
        verbose_name = "Categoria_bodega"
        verbose_name_plural = "Categorias_bodegas"
        ordering = ['fecha_creacion']

    def __str__(self):
        return '{}'.format(self.nombre)


class bodega (models.Model):
    nombre = models.CharField ( max_length=125 )
    descripcion = models.CharField ( max_length=250 )

    categoria = models.OneToOneField ( CategoriaBodega , on_delete=models.CASCADE )

    fecha_creacion = models.DateTimeField ( auto_now_add=True )
    fecha_modificacion = models.DateTimeField ( auto_now=True )
    usuario_creacion = models.CharField ( max_length=15 )
    usuario_modificacion = models.CharField ( max_length=15 )
    estado = models.IntegerField ( default=1 )

    class Meta :
        db_table = "inv_bodega"
        verbose_name = "Bodega"
        verbose_name_plural = "Bodegas"
        ordering = ['fecha_creacion']

    def __str__( self ) :
        return '{}'.format ( self.nombre )


class Categoria_producto ( models.Model ) :
    nombre = models.CharField ( max_length=150 )
    descripcion = models.CharField ( max_length=250 )

    fecha_creacion = models.DateTimeField ( auto_now_add=True )
    fecha_modificacion = models.DateTimeField ( auto_now=True )
    usuario_creacion = models.CharField ( max_length=15 )
    usuario_modificacion = models.CharField ( max_length=15 )
    estado = models.IntegerField ( default=1 )

    class Meta :
        db_table = "inv_categoria_producto"
        verbose_name = "Categoria Producto"
        verbose_name_plural = "Categorias Productos"
        ordering = ['fecha_creacion']

    def __str__( self ) :
        return '{}'.format ( self.nombre )


class Marca (models.Model):
    nombre = models.CharField(max_length=50)

    usuario_creacion = models.CharField ( max_length=15 )
    usuario_modificacion = models.CharField ( max_length=15 )
    fecha_creacion = models.DateTimeField ( auto_now_add=True )
    fecha_modificacion = models.DateTimeField ( auto_now=True )
    estado = models.IntegerField ( default=1 )

    class Meta :
        db_table = "inv_marca"
        verbose_name = "Marca"
        verbose_name_plural = "Marcas"
        ordering = ['fecha_creacion']

    def __str__( self ) :
        return '{}'.format ( self.nombre )


class rol_persona (models.Model):
    cargo = models.CharField(max_length=50)

    usuario_creacion = models.CharField(max_length=15)
    usuario_modificacion =models.CharField(max_length=15)
    fecha_creacion =models.DateTimeField(auto_now_add=True)
    fecha_modificacion =models.DateTimeField(auto_now=True)
    estado = models.IntegerField(default=1)

    class Meta:
        db_table = 'inv_rol_persona'
        verbose_name = "Rol Persona"
        verbose_name_plural = "Roles De Personas"
        ordering = ['fecha_creacion']

    def __str__(self):
        return "{}".format(self.cargo)


class ingreso_cabecera (models.Model):
    codigo_documento_cabecera = models.CharField ( max_length=15 )
    fecha_documento_cabecera = models.DateTimeField()
    usuario_recibe_cabecera = models.CharField ( max_length=15 )
    usuario_entrega_cabecera = models.CharField ( max_length=15 )
    total_ingreso_cabecera = models.DecimalField ( max_digits=16 , decimal_places=4 )

    fecha_creacion = models.DateTimeField ( auto_now_add=True )
    fecha_modificacion = models.DateTimeField ( auto_now=True )
    usuario_creacion = models.CharField ( max_length=15 )
    usuario_modificacion = models.CharField ( max_length=15 )
    estado = models.IntegerField ( default=1 )

    class Meta :
        db_table = "inv_ingreso_cabecera"
        verbose_name = "Ingreso Cabecera "
        verbose_name_plural = "Ingresos Cabeceras"
        ordering = ['fecha_creacion']

    def __str__( self ) :
        return '{}'.format ( self.codigo_documento_cabecera )


class Egreso_cabecera ( models.Model ) :
    codigo_documento_eg = models.CharField ( max_length=15 )
    fecha_documento_eg = models.DateTimeField ()
    usuario_entrega_eg = models.CharField ( max_length=15 )
    usuario_recibe_eg = models.CharField ( max_length=15 )
    total_egreso_eg = models.DecimalField ( max_digits=16 , decimal_places=4 )

    fecha_creacion = models.DateTimeField ( auto_now_add=True )
    fecha_modificacion = models.DateTimeField ( auto_now=True )
    usuario_creacion = models.CharField ( max_length=15 )
    usuario_modificacion = models.CharField ( max_length=15 )
    estado = models.IntegerField ( default=1 )

    class Meta :
        db_table = "inv_egreso_cabecera"
        verbose_name = "Egreso Cabecera"
        verbose_name_plural = "Egresos Cabeceras"
        ordering = ['fecha_creacion']

    def __str__( self ) :
        return '{}'.format ( self.codigo_documento_eg )

class Persona (models.Model):
    nombre = models.CharField(max_length=50)
    apellido = models.CharField(max_length=100)
    edad = models.CharField(max_length=3)
    direccion = models.CharField(max_length=250)
    cedula =models.CharField(max_length=10)
    correo =models.EmailField(null= True, blank= True)
    Rol_persona = models.ForeignKey(rol_persona, on_delete=models.CASCADE)

    usuario_creacion = models.CharField(max_length=15)
    usuario_modificacion =models.CharField(max_length=15)
    fecha_creacion =models.DateTimeField(auto_now_add=True)
    fecha_modificacion =models.DateTimeField(auto_now=True)
    estado = models.IntegerField(default= 1)

    class Meta:
        db_table = 'inv_persona'
        verbose_name = "Persona"
        verbose_name_plural = "Personas"
        ordering = ['fecha_creacion']

    def __str__(self):
        return "{}{}{} ".format(self.nombre, "    ", self.apellido)



class producto (models.Model):
    codigo = models.CharField ( max_length=20 )
    nombre = models.CharField ( max_length=150 )
    descripcion = models.CharField ( max_length=250 )
    categoria_producto = models.ForeignKey ( Categoria_producto, on_delete=models.CASCADE)

    fecha_creacion = models.DateTimeField ( auto_now_add=True )
    fecha_modificacion = models.DateTimeField ( auto_now=True )
    usuario_creacion = models.CharField ( max_length=15 )
    usuario_modificacion = models.CharField ( max_length=15 )
    estado = models.IntegerField ( default=1 )

    class Meta :
        db_table = "inv_producto"
        verbose_name = "Producto"
        verbose_name_plural = "Productos"
        ordering = ['fecha_creacion']

    def __str__( self ) :
        return '{}'.format ( self.nombre )

class Devolucion ( models.Model ) :
    detalle = models.CharField ( max_length= 256 )
    Producto = models.ForeignKey(producto, on_delete=models.CASCADE)


    usuario_creacion = models.CharField ( max_length=15 )
    usuario_modificacion = models.CharField ( max_length=15 )
    fecha_creacion = models.DateTimeField ( auto_now_add=True )
    fecha_modificacion = models.DateTimeField ( auto_now=True )
    estado = models.IntegerField(default= 1)

    class Meta :
        db_table = "inv_devolucion"
        verbose_name = "Devolucion"
        verbose_name_plural = "Devoluciones"
        ordering = ['fecha_creacion']

    def __str__( self ) :
        return '{}'.format ( self.detalle )

class proveedor (models.Model):
    ruc = models.CharField(max_length=13)
    nombre_empresa = models.CharField(max_length=100)
    descripcion_proveedor = models.CharField(max_length=100)
    direccion = models.CharField(max_length=250)
    celular = models.CharField(max_length=10)
    Ciudad = models.ForeignKey(ciudad , on_delete=models.CASCADE)

    usuario_creacion = models.CharField(max_length=15)
    usuario_modificacion =models.CharField(max_length=15)
    fecha_creacion = models.DateTimeField ( auto_now_add=True )
    fecha_modificacion = models.DateTimeField ( auto_now=True )
    estado = models.IntegerField ( default=1 )

    class Meta :
        db_table = "inv_proveedor"
        verbose_name = "Proovedor"
        verbose_name_plural = "Proovedores"
        ordering = ['fecha_creacion']

    def __str__( self ) :
        return '{}'.format ( self.nombre_empresa )



class Bodega_producto (models.Model):
    Bodega = models.ForeignKey ( bodega , on_delete=models.CASCADE )
    Producto = models.ForeignKey ( producto , on_delete=models.CASCADE )
    cantidad_existencia = models.IntegerField ()  # STOCK
    precio_compra = models.DecimalField ( max_digits=16 , decimal_places=4 )
    precio_venta = models.DecimalField ( max_digits=16 , decimal_places=4 )
    stock_maximo = models.IntegerField ()
    stock_minimo = models.IntegerField ()

    fecha_creacion = models.DateTimeField ( auto_now_add=True )
    fecha_modificacion = models.DateTimeField ( auto_now=True )
    usuario_creacion = models.CharField ( max_length=15 )
    usuario_modificacion = models.CharField ( max_length=15 )
    estado = models.IntegerField ( default=1 )

    class Meta :
        db_table = "inv_bodegaproducto"
        verbose_name = "Bodega Producto"
        verbose_name_plural = "Bodegas Productos"
        ordering = ['fecha_creacion']

    def __str__( self ) :
        return '{}'.format ( self.Bodega )



class ingreso_detalle (models.Model):
    Ingreso_cabecera = models.OneToOneField ( ingreso_cabecera , on_delete=models.CASCADE )
    Producto = models.ForeignKey ( producto , on_delete=models.CASCADE )
    cantidad_ingreso = models.IntegerField ()
    precio_ingreso = models.DecimalField ( max_digits=16 , decimal_places=4 )
    sub_total_ingreso = models.DecimalField ( max_digits=16 , decimal_places=4 )

    fecha_creacion = models.DateTimeField ( auto_now_add=True )
    fecha_modificacion = models.DateTimeField ( auto_now=True )
    usuario_creacion = models.CharField ( max_length=15 )
    usuario_modificacion = models.CharField ( max_length=15 )
    estado = models.IntegerField ( default=1 )

    class Meta :
        db_table = "inv_ingreso_detale"
        verbose_name = "Ingreso Detalle"
        verbose_name_plural = "Ingresos Detalles"
        ordering = ['fecha_creacion']

    def __str__( self ) :
        return '{}'.format ( self.Ingreso_cabecera )


class Egreso_detalle ( models.Model ) :
    egreso_cabecera = models.OneToOneField ( Egreso_cabecera , on_delete=models.CASCADE )
    Producto = models.ForeignKey ( producto , on_delete=models.CASCADE )
    cantidad_egreso = models.IntegerField ()
    precio_egreso = models.DecimalField ( max_digits=16 , decimal_places=4 )
    sub_total_egreso = models.DecimalField ( max_digits=16 , decimal_places=4 )

    fecha_creacion = models.DateTimeField ( auto_now_add=True )
    fecha_modificacion = models.DateTimeField ( auto_now=True )
    usuario_creacion = models.CharField ( max_length=15 )
    usuario_modificacion = models.CharField ( max_length=15 )
    estado = models.IntegerField ( default=1 )

    class Meta :
        db_table = "inv_egreso_detalle"
        verbose_name = "Egreso Detalle"
        verbose_name_plural = "Egresos Detalles"
        ordering = ['fecha_creacion']

    def __str__( self ) :
        return '{}'.format ( self.egreso_cabecera )