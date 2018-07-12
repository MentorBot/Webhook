from django.test import TestCase
from rest_framework.test import APIClient
from rest_framework import status
from models import MentorRequests


class ModelTestCase(TestCase):
    '''
    This class defines tests suites for the mentorbot models
    '''

    def setup(self):
        '''define test variables'''
        self.mentorrequests = {'requester_name': 'Jane Doe',
                               'requester_approved': 'approved',
                               'requested_mentorship_field': 'scala',
                               'request_status': False}
        self.mentorrequests_unapproved = {'requester_name':
                                          'jerry kurata',
                                          'requester_approved': 'unapproved',
                                          'requested_mentorship_field':
                                          'javascript', 'request_status':
                                          False}
        self.mentorrequests = MentorRequests(self.mentorrequests)
        self.mentorrequests_unapproved = MentorRequests(
            self.mentorrequests_unapproved)

    '''
    Tests edge cases for a mentor requesting to mentor a field \
    that does not exist in the Database
    '''

    def test_adding_a_new_mentorship_field(self):
        old_count = MentorRequests.objects.count()
        self.mentorrequests.save()
        new_count = MentorRequests.objects.count()
        self.assertNotEqual(old_count, new_count)

    def test_unapproved_mentor_requesting(self):
        old_count = MentorRequests.objects.count()
        self.mentorrequests.save()
        new_count = MentorRequests.objects.count()
        self.assertEqual(old_count, new_count)


class ViewTestCase(TestCase):
    """Test suite for the api views."""

    def setup(self):
        """Define the test client and other test variables."""
        self.client = APIClient()
        self.mentorrequests = {'requester_name': 'Jane Doe',
                               'requester_approved': 'approved',
                               'requested_mentorship_field':
                               'scala', 'request_status': False}
        self.mentorrequests_unapproved = {'requester_name':
                                          'jerry kurata', 'requester_approved':
                                          'unapproved',
                                          'requested_mentorship_field':
                                          'javascript',
                                          'request_status': False}
        self.response1 = self.client.post(self.mentorrequests, format="json")
        self.response2 = self.client.post(
            self.mentorrequests_unapproved, format="json")

    '''
        Tests edge cases for a mentor requesting to mentor a field\
         that does not exist in the Database
        '''

    def test_api_mentor_requesting_new_field(self):
        self.assertEqual(self.response1.status_code, status.HTTP_201_CREATED)

    def test_api_unapproved_mentor_requesting(self):
        self.assertEqual(self.response2.status_code,
                         status.HTTP_401_UNAUTHORIZED)
