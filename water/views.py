from django.http import HttpResponse, Http404, HttpResponseRedirect
from django.shortcuts import get_object_or_404, render
from django.urls import reverse
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from .models import Property, Profile
from .forms import PropertyCreateForm, UserCreateForm, LoginForm


def index(request):
    properties = Property.objects.all()
    users = User.objects.all()
    user = request.user
    context = {"properties": properties, "users":users, "user":user}
    return render(request, "water/index.html", context)

def property(request, property_id):
    property = get_object_or_404(Property, pk=property_id)
    return render(request, "water/property.html", {"property": property})

def property_create(request):
    user = request.user
    profile = Profile.objects.first()
    if request.method == "POST":
        form = PropertyCreateForm(request.POST)
        if form.is_valid():
            property_name = form.cleaned_data["property_name"]
            property = Property.objects.create(name=property_name)
            property.profiles.add(profile)
            property.save()
            return HttpResponseRedirect(reverse("water:index"))
    else:
        form = PropertyCreateForm()
        return render(request, "water/property_create.html", {"form":form})

def user(request, user_id):
    user = get_object_or_404(User, pk=user_id)
    return render(request, "water/user.html", {"user": user})

def profile(request, user_id):
    user = get_object_or_404(User, pk=user_id)
    return render(request, "water/profile.html", {"user": user})

def user_create(request):
    if request.method == "POST":
        form = UserCreateForm(request.POST)
        if form.is_valid():
            username= form.cleaned_data["username"]
            email= form.cleaned_data["email"]
            password= form.cleaned_data["password"]
            user = User.objects.create_user(username, email, password)
            user.save()
            return HttpResponseRedirect(reverse("water:index"))
    else:
        form = UserCreateForm()
        return render(request, "water/user_create.html", {"form":form})

def user_login(request):
    username = request.POST["username"]
    password = request.POST["password"]
    user = authenticate(request, username=username, password=password)
    if user is not None:
        login(request, user)
        return HttpResponseRedirect(reverse("water:index"))
    else:
        return HttpResponseRedirect(reverse("water:index"))

def logout_view(request):
    if request.method=="POST":
        logout(request)
        return HttpResponseRedirect(reverse("water:index"))

def residents(request, property_id):
    response = "You're looking at the residents of property %s."
    return HttpResponse(response % property_id)

def resident_add(request, property_id):
    return HttpResponse("You're adding resident to property %s." % property_id)


