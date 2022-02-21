
class User:
    '''
    A User class that describes a user of the system
    '''

    def __init__(self, login, password) -> None:
        '''
        init method that is ran on each instance of the class
        '''
        self.login = login
        self.passwod = password

    