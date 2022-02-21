from random import choice
import string

class Credential:
    '''
    Credentials class to describe saved credantials
    '''

    # A list of created/store credentials
    credential_list = []

    def __init__(self, user, platform_name, platform_password) -> None:
        '''
        credential class initialiser method
        '''
        self.user = user
        self.platform_name = platform_name
        self.platform_password = platform_password

    def save_credential(self):
        '''
        Add the created credential instatnce to the class variable credential_list
        '''
        Credential.credential_list.append(self)

    @staticmethod
    def generate_credentials():
        '''
        A method to auto-generate user credentials
        '''
        auth_string = string.ascii_uppercase + string.digits + string.ascii_lowercase
        auth_credential = ''.join(choice(auth_string) for item in range(10))
        return auth_credential

    # @classmethod
    # def display_credentials(cls, login):
    #     '''
    #     Display a list of saved credentials
    #     '''
    #     credentials = [credential for credential in cls.credential_list if credential.user == login]
    #     return credentials

    