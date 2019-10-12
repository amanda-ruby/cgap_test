from django.forms import  ModelForm

import json

from . import models

class ParticipantForm(ModelForm):
    class Meta:
        model = models.Participant
        exclude = ['review_status']

    def make_json(self, raw_string):
        return json.dumps([x.strip() for x in raw_string.split(',')])

    def clean_exposures(self):
        return self.make_json(self.cleaned_data['exposures'])

    def clean_mutations(self):
        return self.make_json(self.cleaned_data['mutations'])


class ParticipantListForm(ModelForm):

    class Meta:
        model = models.Participant
        fields = ['name', 'age', 'has_siblings', 'exposures', 'mutations']

    def disable_most_fields(self):
        for field in self.fields:
            if field.name != 'review_status':
                field.disabled = True
