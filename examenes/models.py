from django.db import models
from django.contrib.auth.models import User

# Create your models here.
"""
    MODELOS REFERENTES A LA PARTE DE CONSULTAR EXAMENES E INDICACIONES
"""
class Categoria(models.Model):
    #llaves y referencias
    id_categoria=models.AutoField(primary_key=True)
    #datos
    nombre_categoria=models.CharField(max_length=30)

    #metadatos
    class Meta:
        db_table = 'TblCategoria'
        verbose_name = "categoria"
        verbose_name_plural = "categorias"
        ordering = ['nombre_categoria']
    def __str__(self):
         cad=self.nombre_categoria
         return cad


class Examen(models.Model):
    #llaves y referencias
    id_examen=models.AutoField(primary_key=True)
    categoria=models.ForeignKey(Categoria, null=True, blank=True, on_delete=models.CASCADE)
    #datos
    nombre_examen=models.CharField(max_length=50)
    descripcion_examen = models.CharField(max_length=1000, null=False, blank=False, default='No hay descripción')

    #metadatos
    class Meta:
        db_table = 'TblExamenes'
        verbose_name = "examen"
        verbose_name_plural = "examenes"
        ordering = ['categoria']


    def __str__(self):
        cad = self.nombre_examen + " (" + self.categoria.nombre_categoria + ")"
        return cad


class Indicacion(models.Model):
    #llaves y referencias
    id_indicacion = models.AutoField(primary_key=True)
    categoria = models.ForeignKey(Categoria, on_delete=models.CASCADE)
    #datos del modelo
    num_indicacion = models.IntegerField(null=False, blank=False)
    contenido = models.CharField(max_length=500,
                                 null=False, blank=False)

    #metadatos
    class Meta:
        db_table = 'TblIndicaciones'
        verbose_name = "indicacion"
        verbose_name_plural = "indicaciones"
        ordering = ['id_indicacion']


    def __str__(self):
        return self.id_indicacion


"""
    MODELOS REFERENTES AL REGISTRO DE SOLICITUDES
"""
class Solicitud(models.Model):
    #Para los campos de opciones multiples
    URGENCIA_CHOICES = [
        ('1', 'Baja'),
        ('2', 'Media'),
        ('3', 'Alta'),
    ]

    ESTADO_SOLICITUD_CHOICES = [
        ('1', 'Registrada'),
        ('2', 'En Proceso'),
        ('3', 'Cancelada'),
        ('4', 'Completada'),
        ('5', 'Parcialmente'),
    ]

    #llaves y referencias
    id_solicitud = models.AutoField(primary_key=True)
    examen = models.ManyToManyField(Examen)
    paciente = models.ForeignKey(User, on_delete=models.CASCADE)
    #datos
    nombre_medico = models.CharField(max_length=200, null=False, blank=False)#string
    institucion_solicitante = models.CharField(max_length=100, null=False, blank=False)#string
    diagnostico_presuntivo = models.TextField(max_length=2000, null=False, blank=False)#string largo
    fecha_solicitud = models.DateField(auto_now=True)#date
    fecha_actualizacion = models.DateTimeField(auto_now=True, null=True, blank=True)
    urgencia = models.CharField(max_length=1,
                                choices=URGENCIA_CHOICES,
                                default='1')#string
    estado_solicitud = models.CharField(max_length=1,
                              choices=ESTADO_SOLICITUD_CHOICES,
                              default='1')#string
    notas_solicitud = models.TextField(max_length=1000, null=True, blank=True)

    #metadatos
    class Meta:
        db_table = 'TblSolicitudes'
        verbose_name = "solicitud"
        verbose_name_plural = "solicitudes"
        ordering = ['-fecha_solicitud']


    def __str__(self):
        return self.id_solicitud


class Horario(models.Model):
    #llaves y referencias
    id_horario = models.AutoField(primary_key=True)
    solicitud = models.ForeignKey(Solicitud, on_delete=models.CASCADE,null=True, blank=True)
    #datos del modelo
    fecha_presentacion = models.DateField(null=True, blank=True)
    hora_presentacion = models.TimeField(null=True, blank=True)
    fecha_actualizacion = models.DateTimeField(auto_now=True, null=True, blank=True)

    #metadatos
    class Meta:
        db_table = 'TblHorario'
        verbose_name = "horario"
        verbose_name_plural = "horarios"
        ordering = ['fecha_actualizacion']


    def __str__(self):
        return self.id_horario


"""
    MODELOS REFERENTES A LOS RESULTADOS DE LOS EXAMENES
"""
class ResExamen(models.Model):
    #llaves y referencias
    id_resExamen = models.AutoField(primary_key=True)
    #datos
    ResultadosExamen = models.TextField(max_length=2000, null=False, blank=False)
    ExamenSeleccionado = models.ForeignKey(Solicitud, on_delete=models.CASCADE)

    #metadatos
    class Meta:
        db_table = 'TblResExamen'
        verbose_name = "resultado de examen"
        verbose_name_plural = "resultados de examenes"
        #ordering = ['fecha_solicitud']

    def __str__(self):
        return self.id_resExamen
