from django.contrib.auth.views import PasswordChangeView
from members.forms import EditProfileForm, PasswordChangingForm, SignUpForm
from django.shortcuts import render
from django.views import generic
from django.urls import reverse_lazy
# Create your views here.


class UserRegisterView(generic.CreateView):
    form_class = SignUpForm
    template_name = 'registration/registration.html'
    success_url = reverse_lazy('login')


class UserEditView(generic.UpdateView):
    form_class = EditProfileForm
    template_name = 'registration/edit_profile.html'
    success_url = reverse_lazy('home')

    def get_object(self):
        return self.request.user


class PasswordsChangeView(PasswordChangeView):
    form_class = PasswordChangingForm
    template_name = 'registration/change-password.html'
    success_url = reverse_lazy('password_success')


def password_sucess(request):
    return render(request, 'registration/password_success.html', {})
