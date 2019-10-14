from django.test import Client, TestCase

from .models import Participant

class ReviewTestCase(TestCase):

    def setUp(self):
        Participant.objects.create(name="Amanda Ruby", age=207, has_siblings=True)

    def testDefault(self):
        tp = Participant.objects.get(name="Amanda Ruby")
        self.assertEqual(tp.review_status, "Not Reviewed")

    def testReview(self):
        c = Client()
        c.post('/participants/list/review/1/Reviewed - Accepted/')
        self.assertEqual(Participant.objects.get(name="Amanda Ruby").review_status, "Reviewed - Accepted")
