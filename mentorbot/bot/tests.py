from django.test import TestCase
from rest_framework.test import APIClient
from rest_framework import status
from django.core.urlresolvers import reverse
from models import MentorshipFields, MentorDetails, MenteeRequestNewMentorshipField, NewMentorshipFieldRequest

# Create your tests here.
class ModelTestCase(TestCase):
    '''
    This class defines tests suites for the mentorbot models
    '''
    def setup(self):
        '''define test variables'''
        self.mentordetails = {'name':'Joan Awinja', 'phone_number':'0725792909', 'email':'joan.awinja@andela.com','stack':'python'}
        self.mentorshipfieldname = {'name':'java'}
        self.menteerequestnewmentorshipfield = {'mentee_name':'Mary Jane','requested_mentorship_field':'python', 'request_status':False}
        self.newmentorshipfieldrequest = {'Jane Doe','approved','scala'}
        self.newmentorshipfieldrequestunapproved = {'jerry kurata', 'unapproved','javascript'}
        self.mentordetails = MentorDetails(self.mentordetails)
        self.mentorshipfield = MentorshipFields(self.mentorshipfieldname)
        self.menteerequestNewMentorship = MenteeRequestNewMentorshipField(self.menteerequestnewmentorshipfield)
        self.newmentorshipfieldrequest = NewMentorshipFieldRequest(self.newmentorshipfieldrequest)
        self.newmentorshipfieldrequestunapproved = NewMentorshipFieldRequest(self.newmentorshipfieldrequestunapproved)

    
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
        self.missingmentordetails = {'Jessica Brown', '0789554433', 'jessica.brown@jessica.com'}
        MentorDetails(self.missingmentordetails).save()
        new_count = MentorDetails.objects.count()
        self.assertEqual(old_count, new_count)

    def test_adding_an_existing_mentor(self):
        self.mentordetails.save()
        old_count = MentorDetails.objects.count()
        self.newmentordetails = {'Joan Awinja', '0725792909', 'joan.awinja@andela.com','python'}
        MentorDetails(self.newmentordetails).save()
        new_count = MentorDetails.objects.count()
        self.assertEqual(old_count, new_count)

    def test_deleting_a_mentor_account(self):
        self.mentordetails.save()
        old_count = MentorDetails.objects.count()
        self.newmentordetails = {'Joan Awinja Ingari', '0725792909', 'joan.awinja@andela.com','python'}
        MentorDetails(self.newmentordetails).delete()
        new_count = MentorDetails.objects.count()
        self.assertNotEqual(old_count, new_count)   
    '''
    Tests edge cases for a mentor requesting to mentor a field that does not exist in the Database
    '''
    def test_adding_a_new_mentorship_field(self):
        old_count = NewMentorshipFieldRequest.objects.count()
        self.newmentorshipfieldrequest.save()
        new_count = NewMentorshipFieldRequest.objects.count()
        self.assertNotEqual(old_count, new_count)

    def test_unapproved_mentor_requesting(self):
        old_count = NewMentorshipFieldRequest.objects.count()
        self.newmentorshipfieldrequestunapproved.save()
        new_count = NewMentorshipFieldRequest.objects.count()
        self.assertEqual(old_count, new_count)
    
    '''
    Tests edge cases for a mentee requesting for a new mentorship field
    '''
    def tests_requesting_new_mentorshipfield(self):
        old_count = MenteeRequestNewMentorshipField.objects.count()
        self.menteerequestNewMentorship.save()
        new_count = MenteeRequestNewMentorshipField.objects.count()
        self.assertNotEqual(old_count, new_count)

    class ViewTestCase(TestCase):
        """Test suite for the api views."""
        def setup(self):
            """Define the test client and other test variables."""
            self.client = APIClient()
            self.mentordetails = {'name':'Joan Awinja', 'phone_number':'0725792909', 'email':'joan.awinja@andela.com','stack':'python'}
            self.mentorshipfieldname = {'java'}
            self.menteerequestnewmentorshipfield = {'Mary Jane','python'}
            self.newmentorshipfieldrequest = {'Jane Doe','approved','scala'}
            self.newmentorshipfieldrequestunapproved = {'jerry kurata', 'unapproved','javascript'}
            self.response1 = self.client.post(self.mentordetails, format="json")
            self.response2 = self.client.post(self.mentorshipfieldname, format="json")
            self.response3 = self.client.post(self.menteerequestnewmentorshipfield, format="json")
            self.response4 = self.client.post(self.newmentorshipfieldrequest, format="json")
            self.response5 = self.client.post(self.newmentorshipfieldrequestunapproved, format="json")


        '''
        Tests edge cases for adding, searching, editing, deleting a mentor ussing the API
        '''
        def test_api_can_add_new_mentor(self):
            self.assertEqual(self.response1.status_code, status.HTTP_201_CREATED)
        
        def test_api_adding_a_mentor_missing_fields(self):
            self.missingmentordetails = {'Jessica Brown', '0789554433', 'jessica.brown@jessica.com'}

        def test_api_adding_an_existing_mentor(self):
            self.existingmentordetails = {'name':'Joan Awinja', 'phone_number':'0725792909', 'email':'joan.awinja@andela.com','stack':'python'}
        
        def test_api_editing_mentor_details(self):
            self.editedmentordetails = {'name':'Joan Awinja Ingari', 'phone_number':'0725792909', 'email':'joan.awinja@andela.com','stack':'python'}
        
        def test_api_deleting_a_mentor_account(self):
            self.deletmentordetails = {'name':'Joan Awinja', 'phone_number':'0725792909', 'email':'joan.awinja@andela.com','stack':'python'}

        '''
        Tests edge cases for a mentor requesting to mentor a field that does not exist in the Database
        '''
        def test_api_adding_a_new_mentorship_field(self):
            self.assertEqual(self.response2.status_code, status.HTTP_201_CREATED)
        
        def test_api_unapproved_mentor_requesting(self):
            pass

        '''
        Tests edge cases for a mentee requesting for a new mentorship field
        '''
        def test_api_requesting_new_mentorshipfield(self):
            self.assertEqual(self.response.status_code, status.HTTP_201_CREATED)
    