from django.http import HttpResponse
from django.shortcuts import render, redirect
from .forms import UserForm
from .models import User
from django.contrib import messages

# Create your views here.
def registerUser(request):
    #return HttpResponse('hi')
    
    if request.method == 'POST':
        #print(request.Post)
        form = UserForm(request.POST)
        #create user by form
        if form.is_valid():
           # password = form.cleaned_data['password']
           # user = form.save(commit=False)
           # user.set_password(password)
           # user.role = User.CUSTOMER
           # form.save()
            # Create the user using create_user method
            first_name = form.cleaned_data['first_name']
            last_name = form.cleaned_data['last_name']
            username = form.cleaned_data['username']
            email = form.cleaned_data['email']
            password = form.cleaned_data['password']
            user = User.objects.create_user(first_name=first_name, last_name=last_name, username=username, email=email, password=password)
            user.role = User.CUSTOMER
            user.save()
            messages.success(request,'horaeee your contact added')
            return redirect('registerUser')
            print('user saved')

    else:
        form = UserForm()
    context = {
        'form': form,
    }
    return render(request, 'accounts/registerUser.html', context)
