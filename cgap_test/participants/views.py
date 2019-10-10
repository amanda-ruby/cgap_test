from django.http import HttpResponse
from django.shortcuts import render

from . import forms

# Create your views here.

def participants_form(request):
    return render(request, 'participants/participant_form.html', {'form': forms.ParticipantForm()})