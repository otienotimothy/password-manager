
class User:
    '''
    A User class that describes a user of the system
    '''

    user_list = []

    def __init__(self, user_name, password):
        '''
        init method that is ran on each instance of the class
        '''
        self.user_name = user_name
        self.password = password

    def save_user(self):
        '''
        Functionality to add the created instance to the class variable user_list
        '''
        User.user_list.append(self)
    
    @classmethod
    def get_all_users(cls):
        '''
        Get a list of all save users
        '''
        return cls.user_list