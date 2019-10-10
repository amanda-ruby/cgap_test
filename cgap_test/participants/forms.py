from django.forms import  ModelForm

from . import models

class ParticipantForm(ModelForm):
    class Meta:
        model = models.Participant
        exclude = ['review_status']