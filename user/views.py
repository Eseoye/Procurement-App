from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm # For having a registration form
from .forms import CreateUserForm, UserUpdateForm, ProfileUpdateForm
from django.contrib import messages

# Create your views here.

# def login_user(request):
#     if request.method =='POST':
#         username = request.POST.get('username')
#         password = request.POST.get('password')
        
#         user = authenticate(request, username=username, password=password)
#         if user is not None and user.is_active:
#             login(request, user)

def register(request):
    #passing in a logic
    if request.method == 'POST':
        form = CreateUserForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'Account has been created for {username}. Continue to Login')
            return redirect('user-login')
    else:
        form = CreateUserForm()
    context = {
        'form':form
    }
    return render(request, 'user/register.html', context)  #This form is going to be accesible in the register page

def profile(request):
    return render(request, 'user/profile.html')

# To make the edit button in the profile page function
def profile_update(request):
    if request.method=='POST':
        user_form = UserUpdateForm(request.POST, instance=request.user) # The instance makes the textarea prefilled instead of empty
        profile_form = ProfileUpdateForm(request.POST, request.FILES, instance=request.user.profile)
        if user_form.is_valid() and profile_form.is_valid():
            user_form.save()
            profile_form.save()
            return redirect('user-profile')
    else:
        user_form = UserUpdateForm(instance=request.user)
        profile_form = ProfileUpdateForm(instance=request.user.profile)
    context = {
        'user_form': user_form,
        'profile_form': profile_form
    }
    return render(request, 'user/profile_update.html', context)