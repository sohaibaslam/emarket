from django.contrib.auth import logout
from django.urls import reverse_lazy
from django.views import generic

from . import forms


class LogoutView(generic.RedirectView):
    url = reverse_lazy("stores:all_stores")

    def get(self, *args, **kwargs):
        logout(self.request)
        return super().get(*args, *kwargs)


class SignUpView(generic.CreateView):
    form_class = forms.UserCreateForm
    success_url = reverse_lazy('login')
    template_name = 'accounts/signup.html'
