import hashlib

from django.http import HttpResponse, JsonResponse
from django.shortcuts import render

from .forms import CustomUserCreationForm, CustomAuthenticationForm
from .models import CustomUser


def register_view(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            return HttpResponse("Registration successful.")
    else:
        form = CustomUserCreationForm()
    return render(request, 'register.html', {'form': form})


def login_view(request):
    if request.method == 'POST':
        form = CustomAuthenticationForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            client_hashed_password = form.cleaned_data['password']
            iterations = form.cleaned_data['iterations']  # Get the iterations value from the form

            user = CustomUser.objects.filter(username=username).first()

            if user:
                # Hash the stored password once for comparison
                hashed_password = user.hashed_password
                server_hashed_password = hashlib.sha256(client_hashed_password.encode('utf-8')).hexdigest()
                print('client_hashed_password (sent from client) :', client_hashed_password)
                print('server_hashed_password (H(client_hashed_password)) :', server_hashed_password)
                print('hashed_password in DB:', hashed_password)
                print('iterations:', user.iterations)
                if server_hashed_password == hashed_password:
                    user.hashed_password = client_hashed_password
                    user.iterations = iterations - 1
                    user.save()
                    return HttpResponse("Login successful.")
            return HttpResponse("Invalid username or password.")
    else:
        form = CustomAuthenticationForm()
    return render(request, 'login.html', {'form': form})

def get_iterations_view(request):
    if request.method == 'GET':
        username = request.GET.get('username', None)
        if username:
            user = CustomUser.objects.filter(username=username).first()
            if user:
                return JsonResponse({'iterations': user.iterations})
    return JsonResponse({'error': 'Invalid request'})