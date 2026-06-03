from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.contrib import messages
from django.views.generic import CreateView, UpdateView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.contrib.auth.forms import UserCreationForm

class RegistroView(CreateView):
    model = User
    template_name = 'usuarios/registro.html'
    form_class = UserCreationForm
    success_url = reverse_lazy('productos:inicio')

    def form_valid(self, form):
        response = super().form_valid(form)
        user = form.save()
        login(self.request, user)
        messages.success(self.request, '¡Registro exitoso!')
        return response

    def form_invalid(self, form):
        messages.error(self.request, 'Error en el registro.')
        return super().form_invalid(form)


def login_view(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        
        if user is not None:
            login(request, user)
            messages.success(request, f'¡Bienvenido {user.username}!')
            return redirect('productos:inicio')
        else:
            messages.error(request, 'Usuario o contraseña incorrectos.')
    
    return render(request, 'usuarios/login.html')


def logout_view(request):
    logout(request)
    messages.success(request, 'Has cerrado sesión.')
    return redirect('productos:inicio')


class PerfilView(LoginRequiredMixin, UpdateView):
    model = User
    template_name = 'usuarios/perfil.html'
    fields = ['first_name', 'last_name', 'email']
    success_url = reverse_lazy('usuarios:perfil')

    def get_object(self):
        return self.request.user