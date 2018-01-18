from django.test import TestCase
from models import MentorshipFields, MentorDetails, MenteeRequestNewMentorshipField, NewMentorshipFieldRequest

# Create your tests here.
class ModelTestCase(TestCase):
    '''
    This class defines tests suites for the mentorbot models
    '''
    def setup(self):
        pass
    '''
    Tests edge cases for adding, searching, editing, deleting a mentor 
    '''
    def test_adding_a_new_mentor(self):
        pass
    def test_adding_a_mentor_missing_fields(self):
        pass
    def test_adding_an_existing_mentor(self):
        pass
    def test_editing_mentor_details(self):
        pass
    def test_deleting_a_mentor_account(self):
        pass
    def test_approving_a_mentor_using_valid_token(self):
        pass
    def test_approving_a_mentor_using_invalid_token(self):
        pass

    '''
    Tests edge cases for Mentorship field, where all the mentoship fields are contained
    '''
    def tests_search_for_an_existing_field(self):
        pass
    def tests_searching_for_a_nonexistent_field(self):
        pass
    
    '''
    Tests edge cases for a mentor requesting to mentor a field that does not exist in the Database
    '''
    def test_adding_a_new_mentorship_field(self):
        pass
    def test_unapproved_mentor_requesting(self):
        pass
    
    '''
    Tests edge cases for a mentee requesting for a new mentorship field
    '''
    def tests_requesting_new_mentorshipfield(self):
        pass

    
    
    