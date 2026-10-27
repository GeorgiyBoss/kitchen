from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render, redirect
from  . models import Product
from . forms import ProductForm

def home(request):
    data = {
        'products': Product.objects.all()
    }
    return render(request, 'main/home.html', data)
def about(request):
    return render(request, 'main/about.html')
def login_view(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('/')
        else:
            return redirect('/')
def logout_view(request):
    logout(request)
    return redirect('/')


def create(request):
    error = 'error'
    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('home')
        else:
            error = 'error'
    form = ProductForm()
    data = {
            'form': form,
            'error': error
            }
        # return render(request, 'main/create.html', data)
    return render(request, 'main/create.html', data)

# Create your views here.
