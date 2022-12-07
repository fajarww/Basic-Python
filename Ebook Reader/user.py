"""
ASSIGNMENT 3 - ITI9136 - INTRODUCTION TO PYTHON
Name                    : Fajar Witama Wijaya
Student ID              : 33452784
Creation Date           : November 15th, 2022
Last Modified Date      : November 27th, 2022
"""
class User:
    """
    Contains all the information about a user. Has four attribute defining a user which is
    user_id (unique), user_name (unique), user_password, and user_role. Has overriding method
    for formatted string.
    """

    def __init__(self, user_id = 0, user_name = "", user_password = "", user_role = "reader"):
        """
        Constructs a user object. Defines four attributes of a user which is user_id, user_name,
        user_password, and user_role.
        """
        self.user_id        = user_id          # unique 10 digit number
        self.user_name      = user_name
        self.user_password  = user_password
        self.user_role      = user_role

    def __str__(self):
        """
        Return all the attributes of a user as a formatted string
        """
        string = f"{self.user_id};;;{self.user_name};;;{self.user_password};;;{self.user_role}"
        return string