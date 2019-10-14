from django.forms import modelformset_factory
from django.http import HttpResponse
from django.shortcuts import get_object_or_404, redirect, render

from . import forms
from . import models


def participants_form(request):
    if request.method == 'GET':
        return render(request, 'participants/participant_form.html', {'form': forms.ParticipantForm()})
    else:
        f = forms.ParticipantForm(request.POST)
        f.save()
        return redirect('participants_list')

def participants_list(request):
    ParticipantFormSet = modelformset_factory(models.Participant,
                                   fields=['name', 'age', 'has_siblings', 'exposures', 'mutations', 'review_status'],
                                   labels={'name':'', 'age':'', 'has_siblings': '', 'exposures': '', 'mutations':'', 'review_status':''},
                                   help_texts={'exposures': '', 'mutations': ''}
            )
    formset  = ParticipantFormSet()   
    return render(request, 'participants/participant_list.html', {'formset': formset})

def review_participant(request, id, rev_value):
    if request.method == 'POST':
        print("Made it to view")
        instance = get_object_or_404(models.Participant, id=id)
        instance.review_status = rev_value
        instance.save()
        return HttpResponse("{great success}")
    else:
        return redirect('participants_list')