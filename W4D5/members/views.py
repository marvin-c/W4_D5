from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth.forms import UserCreationForm
from .forms import RegisterUserForm
from django.urls import reverse_lazy
from django.views import generic
from .forms import RegisterUserForm

# Create your views here.
def login_user(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            # Redirect to a success page.
            return redirect('home')
        else:
            # Return an 'invalid login' error message.
            messages.success(request, ("Invalid username or password."))
            return render(request, 'authenticate/login.html', {})

    else:
        return render(request, 'authenticate/login.html', {})

# def register_user(request):
#     if request.method == 'POST':
#         form = UserCreationForm(request.POST)
#         if form.is_valid():
#             form.save()
#             username = form.cleaned_data['username']
#             password = form.cleaned_data['password1'] 
#             user = authenticate(username=username, password=password)
#             login(request, user)
#             messages.success(request, ("User registrationsuccessful"))
#             return redirect('home')

#     else:
#         form = UserCreationForm()
#     return render(request, 'authenticate/register.html', {
#         'form': form,
#     })

class register_user(generic.CreateView):
    form_class = RegisterUserForm
    template_name = 'authenticate/register.html'
    success_url = reverse_lazy('home')
