from django.shortcuts import render, redirect, get_object_or_404
from .models import Animal, Donation, Volunteer
from .forms import AnimalForm, DonationForm, VolunteerForm
from django.contrib.auth.decorators import login_required
from django.views.generic import TemplateView
from django.contrib.auth.decorators import login_required
from .forms import CustomSignupForm, CustomLoginForm
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout


# Home page view
def home(request):
    animals = Animal.objects.all()
    return render(request, 'home.html', {'animals': animals}) # Direct reference to home.html


class AboutPageView(TemplateView):
    template_name = 'about.html'


@login_required
def report_animal(request):
    if request.method == 'POST':
        form = AnimalForm(request.POST, request.FILES)
        if form.is_valid():
            animal = form.save(commit=False)
            animal.added_by = request.user  # Set the user who added the animal
            animal.save()
            return redirect('animal_details', animal_id=animal.id)  # Redirect to animal details page
    else:
        form = AnimalForm()
    return render(request, 'report_animal.html', {'form': form})


# Donation view
@login_required
def donate(request):
    if request.method == 'POST':
        form = DonationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = DonationForm()
    return render(request, 'donate.html', {'form': form})  # Direct reference to donate.html


# Volunteer signup view
@login_required
def volunteer(request):
    if request.method == 'POST':
        form = VolunteerForm(request.POST)
        if form.is_valid():
            volunteer = form.save(commit=False)
            volunteer.user = request.user  # Associate the volunteer with the logged-in user
            volunteer.save()
            return redirect('home')
    else:
        form = VolunteerForm()
    return render(request, 'volunteer.html', {'form': form})  # Direct reference to volunteer.html


def animal_details(request, animal_id):
    animal = get_object_or_404(Animal, id=animal_id)
    return render(request, 'animal_details.html', {'animal': animal})


def signup(request):
    if request.method == 'POST':
        form = CustomSignupForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
    else:
        form = CustomSignupForm()
    return render(request, 'signup.html', {'form': form})


# Login view
def login_view(request):
    if request.method == 'POST':
        form = CustomLoginForm(data=request.POST)
        if form.is_valid():
            return redirect('home')
    else:
        form = CustomLoginForm()
    return render(request, 'login.html', {'form': form})


def logout_view(request):
    logout(request)
    messages.success(request, "You have successfully logout")
    return redirect("/")
