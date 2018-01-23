from django.test import TestCase
from rest_framework.test import APIClient
from rest_framework import status
from django.core.urlresolvers import reverse
from models import  MenteeRequestNewMentorshipField

class ModelTestCase(TestCase):
    '''
    This class defines tests suites for the Mentee Request model
    '''
    def setup(self):
        self.menteerequestnewmentorshipfield = {'mentee_name':'Mary Jane','requested_mentorship_field':'python', 'request_status':False}
        self.menteerequestnewmentorshipfield_missingparameters = {'mentee_name':'Mary Jane','requested_mentorship_field':'', 'request_status':False}
        self.menteerequestnewmentorshipfield_duplicateentry = {'mentee_name':'Mary Jane','requested_mentorship_field':'python', 'request_status':False}
        self.menteerequestNewMentorship = MenteeRequestNewMentorshipField(self.menteerequestnewmentorshipfield)
        self.menteerequestNewMentorship_MissingParameters = MenteeRequestNewMentorshipField(self.menteerequestnewmentorshipfield_missingparameters)
        self.menteerequestNewMentorship_DuplicateEntry = MenteeRequestNewMentorshipField(self.menteerequestnewmentorshipfield_duplicateentry)


    
    '''
    Tests edge cases for a mentee requesting for a new mentorship field
    '''
    def tests_adding_new_mentee_request(self):
        self.menteerequestNewMentorship.save()
        old_count = MenteeRequestNewMentorshipField.objects.count()
        new_count = MenteeRequestNewMentorshipField.objects.count()
        self.assertNotEqual(old_count, new_count)


    def test_missing_parameters_in_mentee_request(self):
        old_count = MenteeRequestNewMentorshipField.objects.count()
        self.menteerequestNewMentorship_MissingParameters.save()
        new_count = MenteeRequestNewMentorshipField.objects.count()
        self.assertEqual(old_count, new_count)


    def test_similar_mentee_request(self):
        old_count = MenteeRequestNewMentorshipField.objects.count()
        self.menteerequestNewMentorship_DuplicateEntry.save()
        new_count = MenteeRequestNewMentorshipField.objects.count()
        self.assertEqual(old_count, new_count)

class ViewTestCase(TestCase):
    """Test suite for the api views."""
    def setup(self):
        """Define the test client and other test variables."""
        self.client = APIClient()
        self.menteerequestnewmentorshipfield = {'mentee_name':'Mary Jane','requested_mentorship_field':'python', 'request_status':False}
        self.menteerequestnewmentorshipfield_missingparameters = {'mentee_name':'Mary Jane','requested_mentorship_field':'', 'request_status':False}
        self.menteerequestnewmentorshipfield_duplicateentry = {'mentee_name':'Mary Jane','requested_mentorship_field':'python', 'request_status':False}
        self.response1 = self.client.post(self.menteerequestnewmentorshipfield, format="json")
        self.response2 = self.client.post(self.menteerequestnewmentorshipfield_missingparameters, format="json")
        self.response3 = self.client.post(self.menteerequestnewmentorshipfield_duplicateentry, format="json")



    def test_adding_new_mentee_request(self):
        pass
    def test_missing_parameters_in_mentee_request(self):
        pass
    def test_similar_mentee_request(self):
        pass

