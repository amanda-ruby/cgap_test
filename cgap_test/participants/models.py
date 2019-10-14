from django.db import models

# Create your models here.

PARTICIPANT_REVIEW_CHOICES = (
    ('Not Reviewed', 'Not Reviewed'),
    ('Reviewed - Accepted', 'Reviewed - Accepted'),
    ('Reviewed - Not Accepted', 'Reviewed - Not Accepted')
)

class Participant(models.Model):
    """Attributes:
    name: CharField, the participant's name.
    age: IntegerField, the participant's age.
    has_siblings: BooleanField, whether or not the participant has siblings
    exposures: CharField (stored as JSON), list of particpant's known environmental exposures.
    mutations: CharField (stored as JSON), list of participant's known genetic mutations.
    review status: CharField, whether this information has been reviewed. Choices are stored
        in PARTICIPANT_REVIEW_CHOICES."""
    name = models.CharField(max_length=50, verbose_name="Name")
    age = models.IntegerField(verbose_name="Age")
    has_siblings = models.BooleanField(verbose_name="Siblings?")
    exposures = models.CharField(blank=True, max_length=500, verbose_name="Known Environmental Exposures",
        help_text="Comma-delimited list")
    mutations = models.CharField(blank=True, max_length=500, verbose_name="Known Genetic Mutations",
        help_text="Comma-delimited list")
    review_status  = models.CharField(blank=False, default='Not Reviewed',
        max_length=30, choices=PARTICIPANT_REVIEW_CHOICES, verbose_name="Review Status")
