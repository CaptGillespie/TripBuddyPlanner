from django.shortcuts import render, redirect
from .models import Trip, User
from django.contrib import messages

def join(request, id):
    Trip.user.add(id=id)
    return redirect ("/dashboard")

def dashboard(request):
    if "logged_in" in request.session:
        context={
        "trips" : Trip.objects.all()
        }
        return render(request, "dashboard.html", context)
    else:
        return redirect ("/")

def new(request):
    if "logged_in" in request.session:
        return render(request,"new.html")
    else:
        return redirect ("/")

def view(request, id):
    if "logged_in" in request.session:
        context={
            "trip" : Trip.objects.get(id=id)
        }
        return render(request,"view.html", context)
    else:
        return redirect ("/")

def createtrip(request):
    if "logged_in" in request.session:
        currentUser = User.objects.get(first=request.session['logged_in'])
        Trip.objects.create(
            destination= request.POST["destination"],
            start_date=request.POST["start_date"],
            end_date= request.POST["end_date"],
            plan = request.POST["plan"],
            user= currentUser,
        )
        if request.method =="POST":
            errors = Trip.objects.jobValidator(request.POST)
        if len(errors) > 0:
            for key, value in errors.items():
                messages.error(request, value)
            return redirect("/new")
        else:
            return redirect("/dashboard")
    else:
        return redirect ("/")

def delete(request, id):
    d=Trip.objects.get(id=id)
    d.delete()
    return redirect ("/dashboard")

def edit(request, id):
    if "logged_in" in request.session:
        context = {
            "trip" : Trip.objects.get(id=id),
            "trips": Trip.objects.all()
        }
        return render(request,"edit.html", context)
    else:
        return redirect ("/")

def updatetrip(request, id):
    if "logged_in" in request.session:
        if request.method =="POST":
            errors = Trip.objects.jobValidator(request.POST)
        if len(errors) > 0:
            for key, value in errors.items():
                messages.error(request, value)
            return redirect('/edit/'+id)
        else:
            trip=Trip.objects.get(id=id)
            trip.destination=request.POST["destination"] 
            trip.start_date=request.POST["start_date"]
            trip.end_date=request.POST["end_date"] 
            trip.plan=request.POST["plan"]
            trip.save()
            return redirect("/dashboard")
    else:
        return redirect ("/")