import unittest
from credential import Credential
from user import User

class TestPasswordLocker(unittest.TestCase):
    '''
    Test class for the all password management functionality
    '''

    def setUp(self):
        '''
        set up method to set up a user instance and a credential instance
        '''
        self.user1 = User('Jdoe', 'password')
        self.first_credential = Credential(
            'Jdoe', 'password', 'instagram', 'ig_password')

    def tearDown(self):
        '''
        Tear down method to reset the class variables after each test
        '''

        User.user_list = []
        Credential.credential_list = []

