from django.contrib.auth.views import LoginView
from django.http import HttpResponse
from django.contrib.auth import logout, login
from django.shortcuts import redirect
from django.urls import reverse_lazy
from django.shortcuts import render
from django.contrib.sites.shortcuts import get_current_site
from django.utils.encoding import force_bytes
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from django.template.loader import render_to_string
from django.views.generic import UpdateView

from .forms import RegisterUserForm, LoginUserForm, ChangeProfile
from .token import account_activation_token
from django.contrib.auth.models import User
from django.core.mail import EmailMessage


class LoginUser(LoginView):
    form_class = LoginUserForm
    template_name = 'registration/login.html'

    def get_success_url(self):
        return reverse_lazy('home')


def usersignup(request):
    if request.method == 'POST':
        form = RegisterUserForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.is_active = False
            user.save()
            current_site = get_current_site(request)
            email_subject = 'Activate Your Account'
            message = render_to_string('registration/acc_active_email.html', {
                'user': user,
                'domain': current_site.domain,
                'uid': urlsafe_base64_encode(force_bytes(user.pk)),
                'token': account_activation_token.make_token(user),
            })
            to_email = form.cleaned_data.get('email')
            email = EmailMessage(email_subject, message, to=[to_email])
            email.send()
            return redirect('email_confirm')
    else:
        form = RegisterUserForm()
    return render(request, 'registration/register.html', {'form': form})


def activate_account(request, uidb64, token):
    try:
        uid = force_bytes(urlsafe_base64_decode(uidb64))
        user = User.objects.get(pk=uid)
    except(TypeError, ValueError, OverflowError, User.DoesNotExist):
        user = None
    if user is not None and account_activation_token.check_token(user, token):
        user.is_active = True
        user.save()
        login(request, user)
        return redirect('success')
    else:
        return HttpResponse('Activation link is invalid!')


def logout_user(request):
    logout(request)
    return redirect('home')

def email_confirm(request):
    return render(request, 'registration/email_confirm.html')

def success(request):
    return render(request,'registration/success.html')


class Change_profile(UpdateView):
    template_name = 'registration/change_profile.html'
    model = User
    form_class = ChangeProfile
    success_url = '/'

