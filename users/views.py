from django.contrib import messages
from django.contrib.auth import login, logout
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.mixins import LoginRequiredMixin
from users.models import CustomUser
from django.shortcuts import render, redirect
from django.views import View
from users.forms import UserCreateForm, UserLoginForm, ProfileForm


class RegisterView(View):
    def get(self, request):
        create_user = UserCreateForm()

        context = {
            'form': create_user
        }
        return render(request=request, template_name='register.html', context=context)

    def post(self, request):
        create_form = UserCreateForm(data=request.POST)

        if create_form.is_valid():
            create_form.save()
            return redirect('users:login')
        else:
            context = {
                'form': create_form
            }
            return render(request=request, template_name='register.html', context=context)




class LoginView(View):
    def get(self, request):
        # login_form = UserLoginForm()
        login_form = AuthenticationForm()

        return render(request=request, template_name='login.html', context={'form': login_form})

    def post(self, request):


        login_form = AuthenticationForm(data=request.POST)
        if login_form.is_valid():
            user = login_form.get_user()
            login(request, user)
            messages.success(request,  f"Welcome {user.last_name} {user.first_name}")

            return redirect('landing_page')
        else:
            return render(request=request, template_name='login.html', context={'form': login_form})



class ProfileView(View):
    def get(self, request):
        user = request.user
        if user.is_authenticated:
            return render(request,template_name='profile.html',context={'user':user})
        else:
            return redirect('users:login')

class LogoutView(View):
    def get (self, request):
        logout(request)
        messages.info(request, 'You have been logged out.')
        return redirect('landing_page')


class EditProfileView(View):
    def get (self, request):
        user_form = ProfileForm(instance=request.user)
        context = {
            'user_form': user_form
        }
        return render(request, 'edit_profile.html', context)
    def post (self, request):
        user_form = ProfileForm(request.POST, request.FILES, instance=request.user)
        if user_form.is_valid():
            user_form.save()
            return redirect('users:profile')
        context = {
            'user_form': user_form
        }
        return render(request, 'edit_profile.html', context)










