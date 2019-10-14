from django.forms import modelformset_factory
from django.http import HttpResponse
from django.shortcuts import get_object_or_404, redirect, render

from . import forms
from . import models


def participants_form(request):
    """No URL arguments.  GET requests bring up a Participant submit form. Post requests create
    a new participant."""
    if request.method == 'GET':
        return render(request, 'participants/participant_form.html', {'form': forms.ParticipantForm()})
    else:
        f = forms.ParticipantForm(request.POST)
        f.save()
        return redirect('participants_list')


def participants_list(request):
    """No URL arguments. Renders a list of ModelForms representing the Participants in the fatabase."""
    ParticipantFormSet = modelformset_factory(models.Participant,
                                   fields=['name', 'age', 'has_siblings', 'exposures', 'mutations', 'review_status'],
                                   labels={'name':'', 'age':'', 'has_siblings': '', 'exposures': '', 'mutations':'', 'review_status':''},
                                   help_texts={'exposures': '', 'mutations': ''},
                                   extra=False)
    formset  = ParticipantFormSet()
    return render(request, 'participants/participant_list.html', {'formset': formset})


def review_participant(request, id, rev_value):
    """Handles POST requests for altering the review_status value for an existing Participant.
    GET requests redirect to the particpants_list.

    Arguments (besides the request):
    id: int, the ID (primary key) of the Participant being edited.
    rev_value: str, the new review_status for the Participant.
    """
    if request.method == 'POST':
        instance = get_object_or_404(models.Participant, id=id)
        instance.review_status = rev_value
        instance.save()
        return HttpResponse("{great success}")
    else:
        return redirect('participants_list')