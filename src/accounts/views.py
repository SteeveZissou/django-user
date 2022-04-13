from multiprocessing import context
from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.

from accounts.models import CustomUser
from django.contrib.auth.forms import UserCreationForm

class CustomSignupForm(UserCreationForm):
    """
    replace auth.User by accounts.CustomUser
    """
    class Meta:
        model = CustomUser
        fields = UserCreationForm.Meta.fields

def signup(request):
    context = {}
        
    if request.method == "POST":
        form = CustomSignupForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponse("Bienvenue !")
        else:
            context["errors"] = form.errors
            
    form = CustomSignupForm()
    context["form"] = form
    return render(request, "accounts/signup.html", context=context)
        