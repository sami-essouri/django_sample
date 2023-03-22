from django.contrib import messages
from django.contrib.auth import login
from django.contrib.auth.mixins import (LoginRequiredMixin,
                                        PermissionRequiredMixin)
from django.shortcuts import redirect, render
from django.urls import reverse_lazy
from django.views.generic import DeleteView, ListView, TemplateView

from app.forms import NewUserForm
from app.models import User


class Index(TemplateView):
    template_name = 'index.html'

def register_request(request):
    if request.method == "POST":
        form = NewUserForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            messages.success(request, "Registration successful.")
            return redirect("profile")
        messages.error(
            request, "Unsuccessful registration. Invalid information.")
    form = NewUserForm()
    return render(request=request, template_name="django_registration/registration_form.html", context={"form": form})


class AccountProfile(LoginRequiredMixin, ListView):
    template_name = 'account_profile.html'
    login_url = '/login/'

    model = User

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["active_user"] = self.request.user
        context["users"] = self.get_queryset()
        return context

    def get_queryset(self):
        queryset = User.objects.all()
        if not self.request.user.is_admin:
            queryset = queryset.defer('location')
        return queryset


class UserDeleteView(LoginRequiredMixin, DeleteView):
    model = User
    success_url = reverse_lazy('profile')
    template_name = "delete_user.html"