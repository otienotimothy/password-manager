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

    