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

    def test_init(self):
        '''
        Assert that the instance methods were created successfully
        '''
        self.assertEqual(self.user1.user_name, 'Jdoe')
        self.assertEqual(self.user1.password, 'password')
        self.assertEqual(self.first_credential.user_name, 'Jdoe')
        self.assertEqual(self.first_credential.platform_name, 'instagram')
        self.assertEqual(
            self.first_credential.platform_password, 'ig_password')

    def test_saved_items(self):
        '''
        Assert that the user and credentials instances have been saved successfully
        '''
        self.user1.save_user()
        self.first_credential.save_credential()

        self.assertEqual(len(User.user_list), 1)
        self.assertEqual(len(Credential.credential_list), 1)

    def test_add_existing_credentials(self):
        '''
        Assert that a user with new credentials can save their credentials
        '''
        self.first_credential.add_existing_credentials('facebook', 'fb_password')
        self.assertEqual(len(Credential.credential_list), 1)


    def test_generate_credentials(self):
        self.assertEqual(len(Credential.generate_credentials()), 10)

        
if __name__ == '__main__':
    unittest.main()
