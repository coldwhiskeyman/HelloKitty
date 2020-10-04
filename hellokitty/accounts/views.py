from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views import View
from django.views.generic import FormView

from . import forms


class RegisterView(FormView):
    template_name = 'register.html'
    form_class = forms.RegisterForm
    success_url = reverse_lazy('get_pets')
    logout_url = reverse_lazy('get_pets')

    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect(self.success_url)
        return render(request, self.template_name, {'form': form})


class LoginView(FormView):
    template_name = 'login.html'
    form_class = forms.LoginForm
    success_url = reverse_lazy('get_pets')
    logout_url = reverse_lazy('get_pets')

    def post(self, request, *args, **kwargs):
        form = self.form_class(data=request.POST)
        if form.is_valid():
            username = request.POST['username']
            password = request.POST['password']
            user = authenticate(username=username, password=password)
            login(request, user)
            return redirect(self.success_url)
        return render(request, self.template_name, {'form': form})


class LogoutView(LoginRequiredMixin, View):
    success_url = reverse_lazy('get_pets')
    login_url = reverse_lazy('login')

    def get(self, request):
        logout(request)
        return redirect(self.success_url)
