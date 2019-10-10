from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.

def participants_form(request):
    return render(request, 'participants/participant_form.html', {})