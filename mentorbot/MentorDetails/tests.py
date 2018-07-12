from django.test import TestCase
from rest_framework.test import APIClient
from rest_framework import status
from .models import MentorDetails


class ModelTestCase(TestCase):
    '''
    This class defines tests suites for the mentorbot models
    '''

    def setup(self):
        '''define test variables'''
        self.mentordetails = {'name': 'Joan Awinja',
                              'phone_number': '0725792909',
                              'email': 'joan.awinja@andela.com',
                              'stack': 'python'}
        self.mentordetails = MentorDetails(self.mentordetails)

    '''
    Tests edge cases for adding, searching, deleting a mentor in the models
    '''

    def test_adding_a_new_mentor(self):
        old_count = MentorDetails.objects.count()
        self.mentordetails.save()
        new_count = MentorDetails.objects.count()
        self.assertNotEqual(old_count, new_count)

    def test_adding_a_mentor_missing_fields(self):
        old_count = MentorDetails.objects.count()
        self.missingmentordetails = {'Jessica Brown',
                                     '0789554433', 'jessica.brown@jessica.com'}
        MentorDetails(self.missingmentordetails).save()
        new_count = MentorDetails.objects.count()
        self.assertEqual(old_count, new_count)

    def test_adding_an_existing_mentor(self):
        self.mentordetails.save()
        old_count = MentorDetails.objects.count()
        self.newmentordetails = {
            'Joan Awinja', '0725792909', 'joan.awinja@andela.com', 'python'}
        MentorDetails(self.newmentordetails).save()
        new_count = MentorDetails.objects.count()
        self.assertEqual(old_count, new_count)

    def test_deleting_a_mentor_account(self):
        self.mentordetails.save()
        old_count = MentorDetails.objects.count()
        self.newmentordetails = {'Joan Awinja Ingari',
                                 '0725792909',
                                 'joan.awinja@andela.com', 'python'}
        MentorDetails(self.newmentordetails).delete()
        new_count = MentorDetails.objects.count()
        self.assertNotEqual(old_count, new_count)


class ViewTestCase(TestCase):
    """Test suite for the api views."""

    def setup(self):
        """Define the test client and other test variables."""
        self.client = APIClient()
        self.mentordetails = {'name': 'Joan Awinja',
                              'phone_number': '0725792909',
                              'email': 'joan.awinja@andela.com',
                              'stack': 'python'}
        self.response1 = self.client.post(self.mentordetails, format="json")

    '''
        Tests edge cases for adding, searching,
         editing, deleting a mentor ussing the API
    '''

    def test_api_can_add_new_mentor(self):
        self.assertEqual(self.response1.status_code, status.HTTP_201_CREATED)

    def test_api_adding_a_mentor_missing_fields(self):
        self.missingmentordetails = {'Jessica Brown',
                                     '0789554433', 'jessica.brown@jessica.com'}
        self.response = self.client.post(
            self.missingmentordetails, format="json")
        self.assertEqual(self.response.status_code,
                         status.HTTP_400_BAD_REQUEST)

    def test_api_adding_an_existing_mentor(self):
        self.existingmentordetails = {
            'name': 'Joan Awinja', 'phone_number': '0725792909',
            'email': 'joan.awinja@andela.com', 'stack': 'python'}
        self.response = self.client.post(
            self.existingmentordetails, format='json')
        self.assertEqual(self.response.status_code, status.HTTP_403_FORBIDDEN)

    def test_api_editing_mentor_details(self):
        self.editedmentordetails = {'name': 'Joan Awinja Ingari',
                                    'phone_number': '0725792909',
                                    'email': 'joan.awinja@andela.com',
                                    'stack': 'python'}
        self.response = self.client.post(
            self.editedmentordetails, format="json")
        self.assertEqual(self.response.status_code, status.HTTP_200_OK)

    def test_api_deleting_a_mentor_account(self):
        self.deletmentordetails = {'name': 'Joan Awinja',
                                   'phone_number': '0725792909',
                                   'email': 'joan.awinja@andela.com',
                                   'stack': 'python'}
        self.response = self.client.post(
            self.deletmentordetails, format='json')
        self.assertEqual(self.response.status_code, status.HTTP_200_OK)
