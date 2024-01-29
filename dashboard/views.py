from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from django.contrib.auth import logout
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .models import Product, Order # To have access to the product model and work with it
from .forms import ProductForm, OrderForm # That was created in forms.py on same dashboard
from django.contrib.auth.models import User
# Create your views here.

@login_required(login_url='user-login') # You have to login first to access the page
def index(request):
    orders = Order.objects.all() # Logic to view d staff request on its page
    products = Product.objects.all()
    orders_count = orders.count()
    product_count = products.count()
    workers_count = User.objects.all().count()
    
    if request.method=='POST':
        form = OrderForm(request.POST)
        if form.is_valid():
            instance = form.save(commit=False) #if commit=false we havent saved it yet
            instance.staff = request.user # This provides the username on the order
            instance.save()
            return redirect('dashboard-index')
    else:
        form = OrderForm()
    context={
        'orders': orders,
        'form': form,
        'products': products,
        'product_count': product_count,
        'orders_count': orders_count,
        'workers_count': workers_count,
    }
    return render(request, 'dashboard/index.html', context)

@login_required(login_url='user-login')
def staff(request):
    workers = User.objects.all()
    workers_count = workers.count()  # To display the correct numbers on the dashboard
    orders_count = Order.objects.all().count()
    product_count = Product.objects.all().count()
    context={
        'workers':workers,
        'workers_count': workers_count,
        'orders_count': orders_count,
        'product_count': product_count,
    }
    return render(request, 'dashboard/staff.html', context)

# To activate the view button function
@login_required(login_url='user-login')
def staff_detail(request, pk):
    workers = User.objects.get(id=pk)
    context = {
        'workers': workers,
    }
    return render(request, 'dashboard/staff_detail.html', context)

@login_required(login_url='user-login')
def product(request):
    items = Product.objects.all() #To get d data 4rm d database using ORM
    product_count = items.count()
    #using sql, items = Product.objects.raw('SELECT * FROM dashboard_product') As far as django framework is concerned, if you want to touch on a particular table then you have to put up the name of the application_the name of the model e.g dashboard_product
    workers_count = User.objects.all().count()
    orders_count = Order.objects.all().count()
    if request.method == 'POST':
        form = ProductForm(request.POST)
        if form.is_valid():
            form.save()
            product_name = form.cleaned_data.get('name')
            messages.success(request, f'{product_name} has been added')
            return redirect('dashboard-product')
    else:
        form = ProductForm()
    context = {
        'items': items,
        'form': form,
        'workers_count': workers_count,
        'orders_count': orders_count,
        'product_count': product_count
    }
    return render(request, 'dashboard/product.html', context)

# Function to activate the delete button
@login_required(login_url='user-login')
def product_delete(request, pk):     # pk is the primary key of the particular item you want to grab and delete
    item = Product.objects.get(id=pk)     # To get a particular item
    if request.method=='POST':
        item.delete()
        return redirect('dashboard-product')
    return render(request, 'dashboard/product_delete.html')

# Function to activate the delete button
@login_required(login_url='user-login')
def product_update(request, pk):
    item = Product.objects.get(id=pk)
    if request.method=='POST':
        form = ProductForm(request.POST, instance=item)
        if form.is_valid():
            form.save()
            return redirect('dashboard-product')
    else:
        form = ProductForm(instance=item)
    context={
        'form':form,
    }
    return render(request, 'dashboard/product_update.html', context)

@login_required(login_url='user-login')
def order(request):
    orders = Order.objects.all()  # Using the ORM
    orders_count = orders.count()
    workers_count = User.objects.all().count()
    product_count = Product.objects.all().count()
    context = {
        'orders':orders,
        'workers_count':workers_count,
        'orders_count':orders_count,
        'product_count':product_count,
    }
    return render(request, 'dashboard/order.html', context)

@login_required(login_url='user-login')
def order_approve(request, id):
    order = get_object_or_404(Order, id=id)
    order.status = 1
    order.save(update_fields=['status'])
       
    return redirect('dashboard-order')

def order_disapprove(request, id):
    order = get_object_or_404(Order, id=id)
    order.status = 2
    order.save(update_fields=['status'])
       
    return redirect('dashboard-order')


def logout_view(request):
    logout(request)
    messages.info(request, "Your session has expired, Please login to continue")
    return redirect('login')

# def redirect_login(request):
#     return redirect