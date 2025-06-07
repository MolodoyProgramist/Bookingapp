from django.urls import path
from . import views
from django.contrib.auth import views as auth_views  # импорт стандартных auth views

urlpatterns = [
    path('', views.index, name='home'),
    path('auth/', views.auth_view, name='login'),
    path('profile/', views.profile, name='profile'),
    path('bookings/', views.bookings, name='bookings'),
    path('bookings/', views.all_bookings, name='all_bookings'),
    path('rooms/', views.rooms, name='rooms'),
    path('logout/', auth_views.LogoutView.as_view(next_page='home'), name='logout'),
]



