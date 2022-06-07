from django.test import TestCase
from projects.models import Contact, Skill


class TestModels(TestCase):

    def setUp(self):
        self.project1 = Contact.objects.create(
            email = 'test@test.pl',
            subject = 'testtext',
            message = 'testmessage'
        )

    def test_contact_is_assigned_on_creation(self):
        self.assertEqual(self.project1 , 'Contact.email')