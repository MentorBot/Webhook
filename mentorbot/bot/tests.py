from django.test import TestCase
from rest_framework.test import APIClient
from rest_framework import status
from django.core.urlresolvers import reverse
from .models import Bot

class ModelTestCase(TestCase):
    '''
    This class defines tests suites for the mentorbot models
    '''
    def setup(self):
        '''define test variables'''
        self.name_of_field = {'name':'java'}
        self.nameoffield = Bot(self.name_of_field)
        
    class ViewTestCase(TestCase):
        """Test suite for the api views."""
        def setup(self):
            """Define the test client and other test variables."""
            self.client = APIClient()
            self.name_of_field = {'name':'java'}
            self.name_of_field_unavailable = {'name':'mango'}
            self.response1 = self.client.post(self.name_of_field, format="json")
            self.response2 = self.client.post(self.name_of_field_unavailable, format="json")


        '''
        Tests edge cases for a user requesting for a field using the bot
        '''
        def test_bot_searching_for_field(self):
            self.assertEqual(self.response1.status_code, status.HTTP_201_CREATED)

        def test_bot_searching_for_unavailable_field(self):
            self.assertEqual(self.response2.status_code, status.HTTP_404_NOT_FOUND)
    