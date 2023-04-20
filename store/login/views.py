from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.messages.views import SuccessMessageMixin
from django.shortcuts import redirect, render
from django.urls import reverse_lazy
from django.utils.decorators import method_decorator
from django.views.generic import CreateView, TemplateView, UpdateView

from login.models import EmailVerification, User

from .forms import ChangeForm, LoginForm, RegistrationForm


class RegistrationUserForm(SuccessMessageMixin, CreateView):
    model = User
    form_class = RegistrationForm
    template_name = 'login/registration.html'
    success_url = reverse_lazy('login')
    success_message = 'Вы успешно зарегистрировались'


class EmailVerificationView(TemplateView):
    template_name = 'login/email_verification.html'

    def get(self, request, *args, **kwargs):
        code = kwargs['code']
        user = User.objects.get(email=kwargs['email'])
        email_verification = EmailVerification.objects.filter(user=user, code=code)
        if email_verification.exists() and not email_verification.first().is_expired():
            user.is_verified_email = True
            user.save()
            return super(EmailVerificationView, self).get(request, *args, **kwargs)
        else:
            return reverse_lazy('home')


def LoginUser(request):
    if request.method == 'POST':
        form = LoginForm(data=request.POST)
        if form.is_valid():
            username = request.POST['username']
            password = request.POST['password']
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user=user)
                return redirect('home')
        else:
            messages.error(request, 'Не правильно введены данные')
    form = LoginForm()
    return render(request, 'login/login.html', {'form': form})


@login_required
def LogoutUser(request):
    if request.method == 'POST':
        logout(request)
        return redirect('home')


class ProfileUserForm(UpdateView):
    model = User
    form_class = ChangeForm
    template_name = 'login/profile.html'

    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        return super(ProfileUserForm, self).dispatch(*args, **kwargs)

    def get_success_url(self):
        return reverse_lazy('profile', kwargs={'pk': self.kwargs['pk']})
