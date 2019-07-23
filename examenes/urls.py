from django.contrib import admin
from django.urls import path
from . import views
from django.contrib.auth import views as auth_views


urlpatterns = [
	#URL DEL HOME
    path('home/', views.home,name='home'),

    #URLS PARA EL REGISTRO Y LOGUEO DE USUARIOS
    path('login/', views.authentication, name='login'),
    path('signup/', views.RegistroUsuario, name = 'reg'),
    path('logout', auth_views.logout, {'next_page': '/home'}, name='logout'),

    #URLS PARA LOS EXAMENES CATEGORIAS E INDICACIONES
    path('examenes/categoria/', views.ViewCategoria, name = 'categorias'),
    path('examenes/categoria/editar/<int:id>/',views.UpdateCategoria, name='editarCat'),
    path('examenes/categoria/crear/',views.CreateCategoria, name='crearCat'),
    path('examenes/categoria/delete/<int:id>/', views.DeleteCategoria, name='deleteCat'),
    path('examenes/editar/<int:id>/', views.UpdateExamen, name='updateEx'),
    path('examenes/crear/', views.CreateExamen, name='crearEx'),
    path('examenes/<int:id>/',views.ViewExamen,name='examenes'),
    path('examenes/delete/<int:id>', views.DeleteExamen, name='deleteExamen'),

    #URLS PARA EL REGISTRO DE SOLICITUDES DE EXAMENES
    #para el paciente
    path('solicitudes/lista/', views.ListSolicitud.as_view(), name= 'listar_solicitudes'),
    path('solicitudes/registrar/', views.CreateSolicitud.as_view(), name= 'crear_solicitud'),
    path('solicitudes/<pk>/ver-detalles/', views.DetailSolicitud.as_view(), name= 'ver_solicitud'),
    path('solicitudes/<pk>/actualizar/', views.UpdateSolicitud.as_view(), name= 'actualizar_solicitud'),
    path('solicitudes/<pk>/eliminar/', views.DeleteSolicitud.as_view(), name= 'borrar_solicitud'),
    #para el encargado
    path('solicitudes/<pk>/actualizar-estado/', views.UpdateEstadoSolicitud.as_view(), name= 'actualizar_estado_solicitud'),

    #URLS PARA EL REGISTRO DE LOS RESULTADOS DE LOS EXAMENES
    path('examenes/',views.gestion.as_view(), name='ResultadoExamenes'),
]
