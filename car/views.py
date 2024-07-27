from django.shortcuts import render


def home(request):
    return render(request, 'home.html')


def contacts(request):
    return render(request, 'contacts.html')


def cars(request):
    return render(request, 'cars.html')


def profile(request):
    return render(request, 'profile.html')
