from django.shortcuts import render
from django.http import *
from django.views import *
from django.urls import reverse
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import AuthenticationForm

from .models import *
from .forms import *
from .signupauth import *

# Create your views here.
class HomeView(View):
    model = Room
    template_name = "core/index.html"

    def get(self, request):
        return render(request, self.template_name, { "rooms": self.model.objects.all() })
    
    def post(self, request):
        logout(request)
        return render(request, self.template_name, { "posts": self.model.objects.all()} )

class SignUpView(View):
    template_name = "core/signup.html"
    form_class = UserForm
    
    def get(self, request):
        if request.user.is_authenticated:
            return HttpResponseRedirect(reverse("HMS:index"))
        return render(request, self.template_name,)
    
    def post(self, request):
        username = request.POST["username"]
        password = request.POST["password"]
        first = request.POST["first"]
        last = request.POST["last"]
        email = request.POST["email"]
        form = self.form_class(request.POST)

        # signupauth
        valid = user_validation(False, username, password, first, last, email)

        if valid[0] and form.is_valid():
            try:
                User.objects.create_user(username=username, password=password, first_name=first, 
                                        last_name=last, email=email)
                user = authenticate(username=username, password=password)
            except:
                return render(request, self.template_name, {"message": "That username already exists."})
            else:
                login(request, user)
                return HttpResponseRedirect(reverse("HMS:index"))
        else:
            return render(request, self.template_name, {"message": valid[1]})   

class LoginView(View):
    template_name = "core/login.html"
    form_class = AuthenticationForm

    def get(self, request):
        if request.user.is_authenticated:
            return HttpResponseRedirect(reverse("HMS:index"))
        return render(request, self.template_name)

    def post(self, request):
        form = self.form_class(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                return HttpResponseRedirect(reverse("HMS:index"))
            return render(request, self.template_name, {
                "message": "We encountered an error while trying to login you in."
            })
        else:
            return render(request, self.template_name, { "message": "Invalid Credentials." })