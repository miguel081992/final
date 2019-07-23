from django.contrib import admin
from .models import Solicitud,Examen,Categoria,Horario,\
					ResExamen,Indicacion
# Register your models here.


@admin.register(Categoria)
class AdminCategoria(admin.ModelAdmin):
    list_display = ('id_categoria','nombre_categoria',)


@admin.register(Examen)
class AdminExamen(admin.ModelAdmin):
    list_display = ('id_examen','categoria','nombre_examen',)


@admin.register(Indicacion)
class AdminIndicacion(admin.ModelAdmin):
    list_display = ('id_indicacion','categoria','num_indicacion','contenido')


@admin.register(Solicitud)
class AdminSolicitud(admin.ModelAdmin):
    list_display = ('id_solicitud','paciente','nombre_medico',
    				'institucion_solicitante','diagnostico_presuntivo',
    				'fecha_solicitud','urgencia',
    				'estado_solicitud','notas_solicitud')


@admin.register(Horario)
class AdminHorario(admin.ModelAdmin):
    list_display = ('id_horario','solicitud_id',
    				'fecha_presentacion','hora_presentacion',
    				'fecha_actualizacion')


@admin.register(ResExamen)
class AdminResExamen(admin.ModelAdmin):
    list_display = ('id_resExamen','ResultadosExamen','ExamenSeleccionado')