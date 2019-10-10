from django.db import models

# Create your models here.

PARTICIPANT_REVIEW_CHOICES = (
    ('Not Reviewed', 'Not Reviewed'),
    ('Reviewed - Accepted', 'Reviewed - Accepted'),
    ('Reviewed - Not Accepted', 'Reviewed - Not Accepted')
)

class Participant(models.Model):
    name = models.CharField(max_length=50, verbose_name="Name")
    age = models.IntegerField(verbose_name="Age")
    has_siblings = models.BooleanField(verbose_name="Siblings?")
    exposures = models.CharField(blank=True, max_length=500, verbose_name="Known Environmental Exposures")
    mutations = models.CharField(blank=True, max_length=500, verbose_name="Known Genetic Mutations")
    review_status  = models.CharField(blank=False, default='Not Reviewed',
        max_length=30, choices=PARTICIPANT_REVIEW_CHOICES, verbose_name="Review Status")
