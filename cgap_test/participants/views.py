from django.http import HttpResponse
from django.shortcuts import render

from . import forms

# Create your views here.

def participants_form(request):
    if request.method == 'GET':
        return render(request, 'participants/participant_form.html', {'form': forms.ParticipantForm()})
    else:
        f = forms.ParticipantForm(request.POST)
        f.save()
        return render(request, 'participants/participant_form.html', {'form': forms.ParticipantForm()})