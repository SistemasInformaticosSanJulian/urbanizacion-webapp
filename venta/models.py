from django.db import models


class Cliente(models.Model):
    GENEROS = [
        ('M', 'Masculino'),
        ('F', 'Femenino')
    ]
    nombres = models.CharField(max_length=35)
    apellidos = models.CharField(max_length=50)
    telefono = models.CharField(max_length=10, verbose_name='Celular')
    email = models.CharField(max_length=50)
    genero = models.CharField(max_length=1, choices=GENEROS, default='M')
    fecha_nacimiento = models.DateField(verbose_name='Fecha Nacimiento')

    def __str__(self):
        return "%s %s" % (self.nombres, self.apellidos)

    class Meta:
        managed = False
        db_table = 'cliente'


class Contrato(models.Model):
    TIPO_PAGOS = [
        ('E', 'Contado'),
        ('C', 'Credito'),
    ]

    ESTADOS = [
        ('V', 'Vigente'),
        ('C', 'Cancelado'),
        ('F', 'Finalizado'),
    ]

    fecha_inicial = models.DateField()
    fecha_final = models.DateField()
    monto_total = models.IntegerField(verbose_name='Monto Total .Bs')
    tipo_pago = models.CharField(max_length=1, choices=TIPO_PAGOS, default='E')
    cliente_titular = models.ForeignKey(Cliente, models.DO_NOTHING)
    cliente_testigo = models.ForeignKey(Cliente, models.DO_NOTHING, related_name='contrato_cliente_testigo_set',
                                        blank=True, null=True)
    lote = models.ForeignKey('Lote', models.DO_NOTHING)
    representante = models.ForeignKey('Representante', models.DO_NOTHING)
    estado = models.CharField(max_length=1, choices=ESTADOS, default='V')

    def __str__(self):
        return "%s %s %s" % (self.id, self.fecha_inicial, self.cliente_titular)

    class Meta:
        managed = False
        db_table = 'contrato'


class Cuota(models.Model):
    fecha = models.DateField()
    numero = models.IntegerField()
    vencimiento = models.DateField()
    total_pago = models.IntegerField()
    deuda_inicial = models.IntegerField()
    saldo = models.IntegerField()
    contrato = models.ForeignKey(Contrato, models.DO_NOTHING)
    
    def __str__(self):
        return "#%s | %s | %s" % (self.id, self.fecha, self.contrato)

    class Meta:
        managed = False
        db_table = 'cuota'


class Lote(models.Model):
    ESTADOS = [
        ('D', 'Disponible'),
        ('V', 'Vendido'),
        ('R', 'Revertido'),
    ]
    numero = models.IntegerField()
    superficie = models.IntegerField()
    valor_m2 = models.IntegerField()
    precio = models.IntegerField(verbose_name='Precio .Bs')
    codigo = models.CharField(max_length=11)
    estado = models.CharField(max_length=1, choices=ESTADOS, default='D')
    manzano = models.ForeignKey('Manzano', models.DO_NOTHING)

    def __str__(self):
        return "%s | Lot. %s #%s | %s" % ( self.estado, self.manzano, self.codigo, self.numero,)

    class Meta:
        managed = False
        db_table = 'lote'


class Manzano(models.Model):
    numero = models.IntegerField()
    superficie_total = models.IntegerField(verbose_name='Superficie Total m2')
    precio_total = models.IntegerField(verbose_name='Precio .Bs', default=5000)

    def __str__(self):
        return "Mz. %s" % (self.numero)

    class Meta:
        managed = False
        db_table = 'manzano'


class Recibo(models.Model):
    numero = models.IntegerField()
    fecha = models.DateField()
    cuota = models.ForeignKey(Cuota, models.DO_NOTHING)

    def __str__(self):
        return "%s #%s | %s" % (self.id, self.numero, self.fecha,)

    class Meta:
        managed = False
        db_table = 'recibo'


class Representante(models.Model):
    GENEROS = [
        ('M', 'Masculino'),
        ('F', 'Femenino')
    ]

    nombres = models.CharField(max_length=35)
    apellidos = models.CharField(max_length=35)
    genero = models.CharField(max_length=1, choices=GENEROS, default='M', )
    telefono = models.CharField(max_length=10)

    def __str__(self):
        return "%s %s" % (self.nombres, self.apellidos,)

    class Meta:
        managed = False
        db_table = 'representante'
