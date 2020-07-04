from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth.mixins import PermissionRequiredMixin
from django.http import HttpResponseRedirect, Http404
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views import View
from django.views.generic import TemplateView, ListView, CreateView
from django.views.generic.edit import ModelFormMixin, UpdateView

from modulos.users.form import UsersForm, UusForm
from modulos.users.models import Users


class Login(View):
    @staticmethod
    def get(request):
        if request.user:
            if request.user.is_active:
                return HttpResponseRedirect(reverse_lazy('users:base'))
        return render(request, 'inicio.html')

    @staticmethod
    def post(request):
        if request.method == 'POST':
            username = request.POST['usu']
            password = request.POST['passwd']

            user = authenticate(username=username, password=password)

            if user:
                if user.is_active:

                    login(request, user)

                    messages.success(request, "Login Exitoso")
                    return HttpResponseRedirect(reverse_lazy('users:base'))
                else:

                    messages.warning(request, "Usuario invalido")
                    return HttpResponseRedirect(reverse_lazy('users:login'))
            else:

                messages.warning(request, "Login invalido")
                return HttpResponseRedirect(reverse_lazy('users:login'))
        else:
            return HttpResponseRedirect(reverse_lazy('users:login'))


class Panel(TemplateView):
    template_name = "base.html"

    def dispatch(self, *args, **kwargs):
        return super(Panel, self).dispatch(*args, **kwargs)

    def get_context_data(self, **kwargs):
        context = super(Panel, self).get_context_data(**kwargs)
        return context


#Funcion salir
def salir(request):
    if request.user:
        messages.success(request, "Te esperamos pronto.")
        logout(request)
    return HttpResponseRedirect('/')


#Clase listar
class Lus(PermissionRequiredMixin, ListView):
    template_name = 'usu/lis.html'
    model = Users
    paginate_by = 30
    qs = None
    permission_required = 'users.view_users'

    def get_queryset(self):
        if self.request.user.is_staff:
            self.qs = Users.objects.all().order_by('first_name')
        elif self.request.user.is_admin:
            self.qs = Users.objects.all().order_by('first_name')
        else:
            raise Http404
        ape = self.request.GET.get('ape', None)
        nom = self.request.GET.get('nom', None)
        usu = self.request.GET.get('usu', None)

        if usu:
            self.qs = self.qs.filter(username__icontains=usu)
        if nom:
            self.qs = self.qs.filter(first_name__icontains=nom)
        if ape:
            self.qs = self.qs.filter(last_name__icontains=ape)
        return self.qs

    def get_context_data(self, **kwargs):
        context = super(Lus, self).get_context_data(**kwargs)
        tot = len(self.qs)
        context["tot"] = tot
        context['tit_cont'] = 'Lista'
        context['sub_tit_cont'] = ' de usuarios'
        nom = self.request.GET.get('nom', None)
        usu = self.request.GET.get('usu', None)
        ape = self.request.GET.get('ape', None)
        if usu:
            context["usu"] = usu
        if nom:
            context["nom"] = nom
        if ape:
            context["ape"] = ape
        return context


#Clase registrar usuario
class Rus(PermissionRequiredMixin, CreateView):
    template_name = 'form.html'
    form_class = UsersForm
    model = Users
    permission_required = 'users.add_users'

    def get_success_url(self):
        messages.success(self.request, "Usuario registrado exitosamente")
        return reverse_lazy('users:lus')

    def get_context_data(self, **kwargs):
        if not self.request.user.is_superuser and not self.request.user.is_admin:
            raise Http404
        context = super(Rus, self).get_context_data(**kwargs)
        context['tit_cont'] = 'Registrar'
        context['sub_tit_cont'] = ' usuarios'
        return context

    def form_valid(self, form):
        form.instance.set_password(form.instance.password)
        form.instance.first_name = form.instance.first_name.upper()
        form.instance.last_name = form.instance.last_name.upper()

        return super(Rus, self).form_valid(form)


class Uus(PermissionRequiredMixin, UpdateView):
    template_name = 'form.html'
    form_class = UusForm
    model = Users
    permission_required = 'users.change_users'

    def get_object(self, queryset=None):
        if not self.request.user.is_staff and not self.request.user.is_admin:
            raise Http404
        qs = Users.objects.get(pk=self.kwargs['pk'])
        return qs

    def get_success_url(self):
        messages.success(self.request, "Se ha actualizado el usuario")
        return reverse_lazy('users:lus')

    def get_context_data(self, **kwargs):
        if not self.request.user.is_staff and not self.request.user.is_admin:
            raise Http404
        context = super(Uus, self).get_context_data(**kwargs)
        context['tit_cont'] = 'Actualizar'
        context['sub_tit_cont'] = ' Usuario'
        return context

    def form_valid(self, form):
        if not self.request.user.is_staff and not self.request.user.is_admin:
            raise Http404
        form.instance.first_name = form.instance.first_name.upper()
        form.instance.last_name = form.instance.last_name.upper()

        return super(Uus, self).form_valid(form)


#Funcion activar  e inactivar usuario
def CambiarEstado(request, pk):
    if request.method == 'GET':
        if Users.objects.filter(pk=pk).exists():
            qs = Users.objects.get(pk=pk)
            if qs.is_active:
                qs.is_active = False

            else:
                qs.is_active = True

            qs.save()

        else:
            pass
        return HttpResponseRedirect(reverse_lazy('users:lus'))
