from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms  import UserCreationForm
from .models import Solicitud,Examen,Categoria,Horario,\
                    Indicacion,ResExamen

from betterforms.multiform import MultiModelForm
from datetime import datetime, date, time

"""
    FORMULARIOS REFERENTES AL REGISTRO Y LOGUEO DE USUARIOS
"""
class RegistroForm(UserCreationForm):
    class Meta:
        model = User
        fields = [
            'username',
            'first_name',
            'last_name',
            'email',
        ]

        labels ={
                'username': 'Nombre de usuario',
                'first_name':'Nombre',
                'last_name':'Apellido',
                'email':'Correo',
        }


"""
    FORMULARIOS REFERENTES A LOS EXAMENES E INDICACIONES
"""
class CategoriaForm(forms.Form):
    nombre = forms.CharField(min_length = 4,max_length=50,
                            widget=forms.TextInput(attrs={'class':'form-control',
                            'pattern':'[0-9,a-z,A-Z," ",á-ú,Á-Ú]+',
                            'title':'Texto y números únicamente'}))

    class Meta:
        model = Categoria

    def clean_nombre_categoria(self):
        nombre_categoria=self.cleaned_data.get("nombre_categoria")

        return nombre_categoria


class UpdateFormCat(forms.Form):
    id = forms.IntegerField()
    nombre = forms.CharField(min_length = 4,max_length=50,
                            widget=forms.TextInput(attrs={'class':'form-control',
                            'pattern':'[0-9,a-z,A-Z," ",á-ú,Á-Ú]+',
                            'title':'Texto y números únicamente'}))

class ExamenForm(forms.Form):
    categoria = forms.ModelChoiceField(queryset= Categoria.objects.all())
    nombre = forms.CharField(min_length = 4,max_length=50,
                            widget=forms.TextInput(attrs={'class':'form-control',
                            'pattern':'[0-9,a-z,A-Z," ",á-ú,Á-Ú]+',
                            'title':'Texto y números únicamente'}))
    descripcion=forms.CharField(min_length=4, max_length=200,
                                widget=forms.Textarea(attrs={'class':'form-control',
                                'pattern':'[0-9,a-z,A-Z," ",á-ú,Á-Ú]+',
                                'title':'Texto y números únicamente'}))



class UpdateExamenForm(forms.Form):
    id = forms.IntegerField(widget=forms.HiddenInput())
    nombre = forms.CharField(min_length=4, max_length=50,
                            widget=forms.TextInput(attrs={'class':'form-control',
                            'pattern':'[0-9,a-z,A-Z," ",á-ú,Á-Ú]+',
                            'title':'Texto y números únicamente'}))
    categoria= forms.ModelChoiceField(queryset= Categoria.objects.all())
    descripcion=forms.CharField(widget=forms.Textarea,max_length=1000)



"""
    FORMULARIOS REFERENTES REGISTRO DE SOLICITUDES
"""
#Formularios para el paciente
class CrearSolicitudModelForm(forms.ModelForm):
    class Meta:
        model = Solicitud

        fields = [
            'nombre_medico','institucion_solicitante',
            'diagnostico_presuntivo','urgencia',
            'examen',
        ]

        labels = {
            'nombre_medico': 'Médico que solicita',
            'institucion_solicitante': 'Institución que solicita',
            'diagnostico_presuntivo': 'Diagnóstico',
            'urgencia': 'Urgencia',
            'examen': 'Seleccione los Examenes',
        }

        widgets = {
            'nombre_medico': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Nombre del médico que le pidió realizarse un exámen',
            }),
            'institucion_solicitante': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Nombre de la institución donde le pidieron realizarse el exámen',
            }),
            'diagnostico_presuntivo': forms.Textarea(attrs={
                'class': 'form-control',
                'placeholder': 'Escriba si cuenta con el diagnóstico que el médico indicó',
            }),
            'urgencia': forms.Select(attrs={
                'class': 'form-control',
            }),
            'examen': forms.SelectMultiple(attrs={
                'class': 'form-control',
            }),
        }

    def clean_nombre_medico(self):
        nombre_medico = self.cleaned_data.get("nombre_medico")
        partes_nombre = nombre_medico.split(" ")
        for partes in partes_nombre:
            if not partes.isalpha():
                raise forms.ValidationError("El nombre del médico escrito no es válido.")

        return nombre_medico


class CrearHorarioModelForm(forms.ModelForm):
    class Meta:
        model = Horario

        fields = [#'id_horario','solicitud',
            'fecha_presentacion','hora_presentacion',#'fecha_actualizacion',
        ]

        labels = {
            'fecha_presentacion': 'Fecha para presentarse',
            'hora_presentacion': 'Hora para presentarse',
        }

        widgets = {
            'fecha_presentacion': forms.DateInput(attrs={
                'class': 'form-control',
                'placeholder': 'dd/mm/yyy',
            }),
            'hora_presentacion': forms.TimeInput(attrs={
                'class': 'form-control',
                'placeholder': 'hh:mm'
            }),
        }

    def clean_fecha_presentacion(self):
        fecha_presentacion = self.cleaned_data.get("fecha_presentacion")
        hoy = datetime.now().date()
        if str(fecha_presentacion) < str(hoy):
            raise forms.ValidationError("La fecha ingresada ya pasó.\
                                        Escriba una fecha válida.")

        if fecha_presentacion.weekday() in [5,6]:
            raise forms.ValidationError("No hay atención en la fecha ingresada.\
                                        Por favor ingrese otra fecha.")

        return fecha_presentacion

    def clean_hora_presentacion(self):
        hora_presentacion = self.cleaned_data.get("hora_presentacion")
        fecha_presentacion = self.cleaned_data.get("fecha_presentacion")
        hoy = datetime.now()

        if  str(fecha_presentacion) == str(hoy.date()) and \
            str(hora_presentacion) < str(hoy.time()):
            raise forms.ValidationError("La hora ingresada ya pasó.\
                                         Escriba una hora válida.")

        if hora_presentacion.hour < 8 or hora_presentacion.hour > 17:
            raise forms.ValidationError("No hay atención a la hora ingresada.\
                                         Por favor ingrese otra hora.")

        return hora_presentacion


class CrearSolicitudHorarioModelForm(MultiModelForm):
    form_classes = {
    'solicitud': CrearSolicitudModelForm,
    'horario': CrearHorarioModelForm,
    }

#Formularios para el encargardo
class ActualizarEstadoSolicitudModelForm(forms.ModelForm):
    class Meta:
        model = Solicitud

        fields = ['estado_solicitud','notas_solicitud',]

        labels = {
            'estado_solicitud': 'Elija el estado de la solicitud',
            'notas_solicitud': 'Notas',
        }

        widgets = {
            'estado_solicitud': forms.Select(attrs={
                'class': 'form-control',
            }),
            'notas_solicitud': forms.Textarea(attrs={
                'class': 'form-control',
                'placeholder': 'Notas si existe algun imprevisto al realizar examenes',
            }),
        }


class ResultdoExamenModelForm(forms.ModelForm):
    class Meta:
        model = ResExamen

        fields = ['ResultadosExamen']

        labels = {
            'ResultadosExamen': 'Diagnóstico del paciente'
        }

        widgets = {
            'ResultadosExamen': forms.Textarea(attrs={
                'class': 'form-control',
                'placeholder': 'Resultado de examen solicitado a secretaria',
            }),
        }

class CrearSolicitudResExamenForm(MultiModelForm):
    form_classes = {
    'Registro': RegistroForm,
    'solicitud': CrearSolicitudModelForm,
    'horario': CrearHorarioModelForm,
    'ResExamen': ResultdoExamenModelForm,
    'Registro': RegistroForm,
     }

"""
    FORMULARIOS REFERENTES AL REGISTRO DE RESULTADOS DE EXAMENES
"""
