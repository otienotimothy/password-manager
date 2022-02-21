
class User:
    '''
    A User class that describes a user of the system
    '''

    user_list = []

    def __init__(self, login, password) -> None:
        '''
        init method that is ran on each instance of the class
        '''
        self.login = login
        self.passwod = password

    def save_user(self):
        '''
        Functionality to add the created instance to the class variable user_list
        '''
        User.user_list.append(self)
    