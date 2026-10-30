from multiprocessing import context

from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse_lazy
from  . models import Product
from . forms import ProductForm
from django.views.generic import DetailView, ListView, CreateView, UpdateView, DeleteView

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
    return render(request, 'main/create.html', data)
class ProductDetail(DetailView):
    model = Product
    template_name = 'main/detail.html'
    context_object_name = 'pr'
class ProductDelete(DeleteView):
    model = Product
    template_name = 'main/delete.html'
    success_url = reverse_lazy('home')
class ProductEdit(UpdateView):
    model = Product
    template_name = 'main/edit.html'
    fields = '__all__'
    success_url = reverse_lazy('home')

def add_to_cart(request, pk):
    product = get_object_or_404(Product, pk=pk)
    cart = request.session.get('cart',{})
    # print("add befor",cart)
    product_id = str(pk)
    if product_id in cart:
        cart[product_id] += 1
    else:
        cart[product_id] = 1
    request.session['cart'] = cart
    request.session.save()
    # print("add after",request.session['cart'])
    return redirect(request.META.get('HTTP_REFERER','home'))
def cart_view(request):
    cart = request.session.get('cart',{})
    products = []
    for product_id, quantity in cart.items():
        product = Product.objects.get(id=product_id)
        products.append({
            'product': product,
            'quantity': quantity,
            'total': product.price * quantity,
        })
    # print('Products',products)
    return render(request, 'main/cart.html', {'products': products})
