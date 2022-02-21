from random import choice
import string

from user import User

class Credential(User):
    '''
    Credentials class to describe saved credantials
    '''

    # A list of created/store credentials
    credential_list = []

    def __init__(self, user_name, password, platform_name, platform_password = "") -> None:
        '''
        credential class initialiser method
        '''
        super.__init__(user_name, password)
        self.user = user_name
        self.platform_name = platform_name
        self.platform_password = platform_password

    def save_credential(self):
        '''
        Add the created credential instatnce to the class variable credential_list
        '''
        Credential.credential_list.append(self)

    def add_existing_credentials(self, auth_plaftform, auth_password):
        '''
        Add an existing credential to credential list variable class
        '''
        self.platform_name = auth_plaftform
        self.platform_password = auth_password
        self.save_credential()

    @staticmethod
    def generate_credentials():
        '''
        A method to auto-generate user credentials
        '''
        auth_string = string.ascii_uppercase + string.digits + string.ascii_lowercase
        auth_credential = ''.join(choice(auth_string) for item in range(10))
        return auth_credential

    @classmethod
    def display_credentials(cls, login):
        '''
        Display a list of saved credentials
        '''
        credentials = [credential for credential in cls.credential_list if credential.user == login]
        return credentials

    @classmethod
    def delete_contact(cls, login):
        '''
        Delete a particular credential from the credential list class variable based a login user name
        '''
        for credential in cls.credential_list:
            if credential.user == login:
                cls.credential_list.remove(credential)
    