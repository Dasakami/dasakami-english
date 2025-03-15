from django.shortcuts import render, HttpResponsePermanentRedirect, redirect, get_object_or_404
from django.urls import reverse
from django.contrib import auth
from django.contrib import messages
from users.forms import UserLoginForm, UserRegistrationForm,UserProfileForm
from users.models import User
from django.contrib.auth.decorators import login_required
from django.contrib.auth import update_session_auth_hash 
from .forms import UserSearchForm
from django.contrib.auth.forms import PasswordResetForm
from django.contrib.auth.tokens import default_token_generator
from django.contrib import messages
from django.utils.http import urlsafe_base64_encode
from django.contrib.auth import get_user_model
from django.core.mail import send_mail
from django.http import HttpResponse
from django.conf import settings


def login(request):
    if request.method == 'POST':
        form = UserLoginForm(data=request.POST)
        if form.is_valid():
            username = request.POST['username']
            password = request.POST['password']
            user = auth.authenticate(username=username, password=password)
            if user:
                auth.login(request, user)
                return HttpResponsePermanentRedirect('/')
    else:
        form = UserLoginForm()
    context = {'form':form}
    return render(request, 'users/login.html', context)

def profile(request):
    if request.method == 'POST':
        form = UserProfileForm( instance=request.user ,data=request.POST, files=request.FILES)
        if form.is_valid():
            # print(form.cleaned_data) 
            form.save()
            messages.success(request, 'Поздравляем!, Вы успешно зарегестрировались!')
            return HttpResponsePermanentRedirect(reverse( 'users:profile'))
        else:
            print("Form errors:", form.errors)  
    else:
        form = UserProfileForm(instance=request.user)
    context = {'form': form}
    return render(request, 'users/profile.html', context)

def logout(request):
    auth.logout(request)
    return HttpResponsePermanentRedirect(reverse('home'))

def register(request):
    if request.method == 'POST':
        form = UserRegistrationForm(data=request.POST)
        if form.is_valid():
            form.save()
            return  HttpResponsePermanentRedirect(reverse('users:login'))
    else:
        form = UserRegistrationForm()
    context = {'form':form}
    return render(request, 'users/register.html', context)



@login_required
def setting(request):
    user = request.user  # просто текущий пользователь

    if request.method == 'POST':
        form = UserProfileForm(instance=user, data=request.POST, files=request.FILES)
        if form.is_valid():
            # Сохраняем профиль пользователя
            user_profile = form.save(commit=False)

            # Обработка смены пароля
            old_pass = request.POST.get('old_pass')
            new_pass = request.POST.get('new_pass')
            confirm_pass = request.POST.get('confirm_new_pass')

            if old_pass and new_pass and confirm_pass:
                if new_pass == confirm_pass:
                    if user.check_password(old_pass):
                        user.set_password(new_pass)
                        user.save()
                        update_session_auth_hash(request, user)  # чтобы не выкинуло из аккаунта
                        messages.success(request, 'Пароль успешно обновлён!')
                    else:
                        messages.error(request, 'Неверный старый пароль.')
                else:
                    messages.error(request, 'Новый пароль и подтверждение не совпадают.')

            # Обновление роли пользователя
            role = request.POST.get('role')
            if role and role != user_profile.role:
                user_profile.role = role

            user_profile.save()  # сохраняем изменения

            messages.success(request, 'Профиль успешно обновлён!')
            return redirect('users:profile')
        else:
            print("Form errors:", form.errors)
    else:
        form = UserProfileForm(instance=user)

    context = {
        'form': form,
    }
    return render(request, 'users/setting.html', context)


def search_users(request):
    form = UserSearchForm(request.GET)
    users = User.objects.all()

    if form.is_valid():
        search = form.cleaned_data['search']
        if search:
            users = users.filter(username__icontains=search)  # Поиск по username

    context = {
        'form': form,
        'users': users,
    }
    return render(request, 'users/search_results.html', context)


def view_profile(request, user_id):
    user = get_object_or_404(User, id=user_id)
    context = {
        'user': user,
    }
    return render(request, 'users/view_profile.html', context)

