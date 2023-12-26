from django.shortcuts import render


from django.shortcuts import render, redirect
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm

from django.contrib.auth.models import User 

from .models import Profile
from .forms import SignUpForm

# Create your views here.
def register(request):
 
    if request.method != 'POST':
        # Display blank registration form. 
        form = SignUpForm()
    else:
        # Process completed form.
        form = SignUpForm(data=request.POST)
        
        if form.is_valid():
            new_user = form.save()  

            new_user.save()

            login(request, new_user)
            return redirect('main:home')
    context = {'form': form}
    return render(request, 'registration/register.html', context)

def logout_page(request):
    return render(request, 'registration/logged_out.html')

