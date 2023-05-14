

from django.shortcuts import render, redirect
from .forms import CustomUserCreationForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth import get_user_model
from .models import User
def register(request):
    if request.user.is_authenticated: 
        return redirect('/dashboard/') 
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/user/login/')
    else:
        form = CustomUserCreationForm()
    return render(request, 'user/register.html', {'form': form})



from django.contrib.auth.views import LoginView
from django.urls import path, reverse_lazy

class MyLoginView(LoginView):
    template_name = 'user/login.html'
    redirect_authenticated_user = True
    success_url = reverse_lazy('dashboard')
    def get_success_url(self):
        return self.success_url

def login(request): 
    if request.user.is_authenticated: 
        return redirect('/dashboard/') 
    else: 
        return MyLoginView.as_view()(request)

from django.contrib.auth import logout

@login_required
def logout_view(request):
    logout(request)
    return redirect('/user/login/')


@login_required
def get_user_info(request):
  user = get_user_model().objects.get(id=request.user.id)
  
  return render(request, 'home/user.html' , context={'user' : user.username , 'user_info' : user})