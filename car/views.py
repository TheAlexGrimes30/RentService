from django.http import HttpResponseNotFound
from django.shortcuts import render, redirect

from car.forms import CarForm


def home(request):
    return render(request, 'home.html')


def contacts(request):
    return render(request, 'contacts.html')


def cars(request):
    return render(request, 'cars.html')


def profile(request):
    return render(request, 'profile.html')


def page_not_found(request, exception):
    return HttpResponseNotFound("<h1>Страница не найдена</h1>")


def add_car(request):
    if request.method == 'POST':
        form = CarForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('cars')
    else:
        form = CarForm()

    return render(request, 'car_form.html', {'form': form})
