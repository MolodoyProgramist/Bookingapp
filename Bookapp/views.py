from django.contrib.auth.decorators import login_required
from django.shortcuts import render



def index(request):
    return render(request, 'home.html')

def auth_view(request):
    return render(request, 'login.html')

@login_required
def profile(request):
    return render(request, 'profile.html')

@login_required
def bookings(request):
    # Здесь можно получить реальные данные бронирований из базы
    return render(request, 'bookings.html')

@login_required
def rooms(request):
    # Здесь можно получить реальные данные бронирований из базы
    return render(request, 'rooms.html')

def all_bookings(request):
    # пример: передаём список всех бронирований
    return render(request, 'all_bookings.html', {'bookings': bookings})



# Create your views here.
