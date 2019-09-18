from django.shortcuts import render, redirect
import bcrypt
from django.contrib import messages
from .models import User


def signup(request):
    return render(request, "login_app/index.html")
def success(request):
    return render(request, 'login_app/success.html')

def createUser(request):
    if request.method == "POST":
        errors = User.objects.basicValidator(request.POST)
        if len(errors) > 0:
            for key, value in errors.items():
                messages.error(request, value)
        # if request.POST['email'] == User.object.filter(email)
        #         messages.error(request, value)
            return redirect("/")

        User.objects.create(
            first = request.POST["first"],
            last = request.POST["last"],
            email = request.POST["email"].lower(),
            password = request.POST['password']
        )

        messages.success(request, "New user created")
        return redirect("/")

def login(request):
    if request.method == "POST":
        errors = User.objects.loginValidator(request.POST)
        if len(errors) > 0:
            for key, value in errors.items():
                messages.error(request, value, extra_tags="login")
            return redirect('/')
        else:
            user = User.objects.get(email=request.POST['email'])
            request.session['logged_in'] = user.first
            request.session['user_id'] = user.id
            return redirect('/dashboard')


def logout(request):
    try:
        del request.session['logged_in']
    except KeyError:
        pass
    return redirect ("/")