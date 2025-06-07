from django import forms
from .models import Booking, Room

class BookingForm(forms.ModelForm):
    class Meta:
        model  = Booking
        fields = ['room','start_date','end_date','email']
        widgets = {
            'start_date': forms.DateTimeInput(attrs={'type':'datetime-local'}),
            'end_date':   forms.DateTimeInput(attrs={'type':'datetime-local'}),
        }
