from django.shortcuts import redirect, render

from . import forms


def participants_form(request):
    if request.method == 'GET':
        return render(request, 'participants/participant_form.html', {'form': forms.ParticipantForm()})
    else:
        f = forms.ParticipantForm(request.POST)
        f.save()
        return redirect('participants_list')

def participants_list(request):
    return render(request, 'participants/participant_list.html', {})