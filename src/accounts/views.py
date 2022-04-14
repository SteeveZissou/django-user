
from django.http import HttpResponse
from django.shortcuts import redirect, render


# Create your views here.
from accounts.forms import UserRegistrationForm

def profile(request):
    return HttpResponse(f"{request.user.email}")

def home(request):
    return HttpResponse("Accueil du site")

def signup(request):
    context = {}
    
    if request.method == "POST":
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("home")
                
    form = UserRegistrationForm()
    context["form"] = form
    return render(request, "accounts/signup.html", context=context)
        