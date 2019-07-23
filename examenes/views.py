from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.models import User, Group
from django.contrib.auth import authenticate, login as auth_login
from django.urls import reverse, reverse_lazy
from django.views.generic import CreateView,ListView,UpdateView,\
                                DetailView, DeleteView
from .models import Solicitud,Examen,Categoria,Horario,\
                    Indicacion,ResExamen
from .forms import RegistroForm, CrearSolicitudHorarioModelForm, CrearSolicitudResExamenForm,\
                    ActualizarEstadoSolicitudModelForm
from .forms import UpdateFormCat, ExamenForm, \
                    UpdateExamenForm, CategoriaForm
from django.http import HttpResponseRedirect
from django.contrib import messages


# Create your views here.
"""
    VISTA DEL HOME
"""
def home(request):
    return render(request, 'home.html')


"""
    VISTAS PARA EL REGISTRO Y LOGIN DE USUARIOS
"""



def authentication(request):
    if request.method == 'POST':
        username = request.POST.get('username', None)
        password = request.POST.get('password', None)
        user = authenticate(username=username, password=password)
        if user is not None and user.is_active:
            auth_login(request, user)
            return redirect('home')
        else:
            messages.error(request, 'Usuario o contreseña incorrectos')
            return redirect('login')
    return render(request, 'usuarios/login.html',{})

"""
class RegistroUsuario(CreateView):
    model = User
    form_class = RegistroForm
    template_name = 'usuarios/registro.html'
    success_url = '/home'
    g=Group.objects.get(name='paciente')
    User.groups=g
"""
def RegistroUsuario(request):
    if request.method=='POST':
        form = RegistroForm(request.POST)
        if form.is_valid():
            user=form.save()
            g=Group.objects.get(name='paciente')
            g.user_set.add(user)
            return redirect('login')
    else:
        form = RegistroForm()
    return render(request, 'usuarios/registro.html', {'form':form})




"""
    VISTAS LOS EXAMENES CATEGORIAS INDICACIONES
"""
def ViewCategoria(request):
    list = Categoria.objects.all()
    context = {
        "list": list
    }
    return render(request, 'examenes/categoria_list.html', context)


def CreateCategoria(request):
    if request.method == 'POST':
        form = CategoriaForm(request.POST)
        if form.is_valid():
            cat = Categoria()
            cat.nombre_categoria=form.cleaned_data['nombre']
            cat.save()
            return redirect('categorias')
        context = {
            'form': form
        }
        return render(request, 'examenes/create_categoria.html', context)
    elif request.method == 'GET':
        form = CategoriaForm()
        context = {
            'form': form
            }
        return render(request, 'examenes/create_categoria.html', context)


def UpdateCategoria(request, id):
    if request.method == 'POST':
        form = UpdateFormCat(request.POST)
        if form.is_valid():
            cat = get_object_or_404(Categoria, pk=form.cleaned_data['id'])
            cat.nombre_categoria=form.cleaned_data['nombre']
            cat.save()
            return redirect('categorias')
        context = {
            'form': form
        }
        return render(request, 'examenes/update_categoria.html', context)
    elif request.method == 'GET':
        cat = get_object_or_404(Categoria,pk=id)
        form = UpdateFormCat(initial={'id':cat.id_categoria,'nombre':cat.nombre_categoria})
        context = {
            'form': form
            }
        return render(request, 'examenes/update_categoria.html', context)


def DeleteCategoria(request, id):
    cat= Categoria.objects.get(id_categoria=id)
    if request.method == 'POST':
        cat.delete()
        return redirect('categorias')
    return render(request,'examenes/delete_categoria.html',{'cat':cat})



def ViewExamen(request,id):
    list = Examen.objects.filter(categoria=id)
    context = {
            'list': list
    }
    return render (request, 'examenes/examen_list.html', context)



def CreateExamen(request):
    if request.method == 'POST':
        form = ExamenForm(request.POST)
        if form.is_valid():
            ex = Examen()
            ex.nombre_examen=form.cleaned_data['nombre']
            ex.categoria=form.cleaned_data['categoria']
            ex.descripcion_examen=form.cleaned_data['descripcion']
            ex.save()
            id=ex.categoria
            return ViewExamen(request, id )
        context = {
            'form': form
            }
        return render(request, 'examenes/create_examen.html', context)
    elif request.method == 'GET':
        form = ExamenForm()
        context = {
            'form': form
            }
        return render(request, 'examenes/create_examen.html', context)



def UpdateExamen(request, id):
    if request.method == 'POST':
        form = UpdateExamenForm(request.POST)
        if form.is_valid():
            cat = get_object_or_404(Examen, pk=form.cleaned_data['id']) #obtiene el objeto de la base o 404
            cat.nombre_examen=form.cleaned_data['nombre']   # actualiza cada campo
            cat.categoria=form.cleaned_data['categoria']
            cat.descripcion_examen=form.cleaned_data['descripcion']
            cat.save()
            pk = cat.categoria
            return ViewExamen(request,pk)
        context = {
            'form': form
        }
        return render(request, 'examenes/update_examen.html', context)
    elif request.method == 'GET':
        ex = get_object_or_404(Examen,pk=id)
        form = UpdateExamenForm(initial={'id':ex.id_examen,
                                        'nombre':ex.nombre_examen,
                                        'categoria':ex.categoria,
                                        'descripcion':ex.descripcion_examen})
        context = {
            'form': form
            }
    return render(request, 'examenes/update_examen.html', context)


def DeleteExamen(request, id):
    ex=Examen.objects.get(id_examen=id)
    pk = ex.categoria
    if request.method == 'POST':
        ex.delete()
        return ViewExamen(request, pk)
    return render(request, 'examenes/delete_examen.html', {'list':ex})


"""
    VISTAS PARA EL REGISTRO DE LAS SOLICITUDES
"""
class ListSolicitud(ListView):
    #model = Solicitud
    template_name = 'solicitudes/lista_solicitudes.html'
    #en web: if not request.user.is_authenticated or request.user.groups.all.first.name == 'paciente'

    def get_queryset(self):
        return None


    def get_context_data(self, **kwargs):
        context = super(ListSolicitud,self).get_context_data(**kwargs)
        #consultar grupo en vistas
        usuario = self.request.user
        g = Group.objects.filter(user__in=[usuario])

        if g.exists():
            grupo = g[0]
            if grupo.name == 'paciente':
                context['solicitudes'] = Horario.objects.filter(solicitud__paciente__in=[usuario])
            elif grupo.name == 'encargado':
                usuarios = User.objects.all()
                context['solicitudes'] = Horario.objects.filter(solicitud__paciente__in=usuarios)
        elif usuario.is_superuser:
            usuarios = User.objects.all()
            context['solicitudes'] = Horario.objects.filter(solicitud__paciente__in=usuarios)

        return context


class CreateSolicitud(CreateView):
    model = Solicitud
    form_class = CrearSolicitudHorarioModelForm
    template_name = 'solicitudes/crear_solicitud.html'
    success_url = reverse_lazy('listar_solicitudes')

    def form_valid(self, form):
        solicitud = form['solicitud'].save(commit=False)
        solicitud.paciente = self.request.user
        solicitud.save()
        form['solicitud'].save_m2m()#para guardar la relacion de examenes-solicitudes
        horario = form['horario'].save(commit=False)
        horario.solicitud = solicitud
        horario.save()

        return HttpResponseRedirect(reverse('listar_solicitudes'))


class UpdateSolicitud(UpdateView):
    model = Solicitud
    form_class = CrearSolicitudHorarioModelForm
    template_name = 'solicitudes/actualizar_solicitud.html'
    success_url = reverse_lazy('listar_solicitudes')


    def get_form_kwargs(self):
        kwargs = super(UpdateSolicitud, self).get_form_kwargs()
        kwargs.update(instance={
            'solicitud': self.object,
            'horario': Horario.objects.get(solicitud=self.object.id_solicitud),
        })

        return kwargs


    def form_valid(self, form):
        solicitud = form['solicitud'].save(commit=False)
        solicitud.paciente = self.object.paciente
        solicitud.save()
        form['solicitud'].save_m2m()#para guardar la relacion de examenes-solicitudes
        horario = form['horario'].save(commit=False)
        horario.solicitud = solicitud
        horario.save()

        return HttpResponseRedirect(reverse('listar_solicitudes'))


class DetailSolicitud(DetailView):
    model = Solicitud
    template_name = 'solicitudes/detalle_solicitud.html'

    def get_context_data(self, **kwargs):
        context = super(DetailSolicitud, self).get_context_data(**kwargs)

        solicitud = Solicitud.objects.filter(id_solicitud=self.kwargs['pk'])
        horario = Horario.objects.filter(solicitud=self.kwargs['pk'])
        examenes = Examen.objects.filter(solicitud__in=solicitud)

        context['solicitud'] = solicitud[0]
        context['horario'] = horario[0]
        context['examenes'] = examenes

        return context


class DeleteSolicitud(DeleteView):
	model = Solicitud
	template_name = 'solicitudes/borrar_solicitud.html'
	success_url = reverse_lazy('listar_solicitudes')

	def get_context_data(self, **kwargs):
		context = super(DeleteSolicitud, self).get_context_data(**kwargs)
		context['horario'] = Horario.objects.filter(solicitud=self.object.id_solicitud)[0]
		return context


class UpdateEstadoSolicitud(UpdateView):
    model = Solicitud
    form_class = ActualizarEstadoSolicitudModelForm
    template_name = 'solicitudes/actualizar_solicitud.html'
    success_url = reverse_lazy('listar_solicitudes')
    success_message = 'Registro editado correctamente'


"""
    VISTAS PARA EL REGISTRO DE LOS RESULTADOS DE LOS EXAMENES
"""
class gestion(CreateView):
    model = ResExamen
    form_class = CrearSolicitudResExamenForm
    template_name = 'examenes/ResultadoExamenes.html'
    success_url = reverse_lazy('ResultadoExamenes')

    def form_valid(self, form):
        solicitud = form['solicitud'].save(commit=False)
        solicitud.paciente = self.request.user
        solicitud.save()
        form['solicitud'].save_m2m()#para guardar la relacion de examenes-solicitudes
        horario = form['horario'].save(commit=False)
        horario.solicitud = solicitud
        horario.save()
        return HttpResponseRedirect(reverse('ResultadoExamenes'))
