"""
ASSIGNMENT 3 - ITI9136 - INTRODUCTION TO PYTHON
Name                    : Fajar Witama Wijaya
Student ID              : 33452784
Creation Date           : November 15th, 2022
Last Modified Date      : November 27th, 2022
"""
from user import User   # import User Class to make inheritance attributes to Reader Class

class Reader(User):
    """
    Contains all the information about a reader. Inherits the attribute of User Class
    with two extra attributes which is favourite book list and bookmark list.
    """
    def __init__(self, user_id, user_name, user_password, user_role, favourite_book_list = [], bookmark_list = [] ):
        """
        Constructs a reader object. Inherit the methods from User class. Adding new attribute such as
        favourite_book_list and bookmark_list.
        """
        super().__init__(user_id, user_name, user_password, user_role)  # calling User.__init__()
        self.favourite_book_list        = favourite_book_list   # adding two new attributes
        self.bookmark_list              = bookmark_list
    
    def __str__(self):
        """
        Return all the attributes of a reader as a formatted string
        """
        string = f"{self.user_id};;;{self.user_name};;;{self.user_password};;;{self.user_role};;;{self.favourite_book_list};;;{self.bookmark_list}"
        return string