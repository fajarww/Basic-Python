"""
ASSIGNMENT 3 - ITI9136 - INTRODUCTION TO PYTHON
Name                    : Fajar Witama Wijaya
Student ID              : 33452784
Creation Date           : November 15th, 2022
Last Modified Date      : November 27th, 2022
"""
import re       # used for searching pattern in string
import random   # used for generating unique random 10 digits user_id
import os       # used for change directories (up twice) after using open function with relative path
from user import User       # used to create a user object
from reader import Reader   # used to create a reader object

class UserOperation:
    """
    Contains all the operations related to a user.
    """
    user_info_path = "data/result_data/users.txt"
    user_info_list = []

    def load_user_info():
        """
        Loads all the registered users information from a given file (i.e., user_info_path class variable)
        into the user_info_list list. No arguments required and returns True if the load user info from
        users.txt succeeed, and will return False with a certain error message if any error happens.
        """
        favourite_book_list = []    # a container for favourite book list from users.txt
        bookmark_list = []          # a container for bookmark list from users.txt

        try:
            os.chdir('../../')      # workiing directories being back twice after used in Book Operation Class
            with open(UserOperation.user_info_path, 'r', encoding="utf8") as user_file:     # read users.txt file with relative path
                for _, value in enumerate(user_file):       # make a pair value of each line in users.txt with line number from 0 to the last line
                    user_info = re.search(r"^(.*?);;;(.*?);;;(.*?);;;(.*?);;;\[(.*?)\];;;\[(.*?)\]$", value, re.MULTILINE and re.DOTALL)    # read pattern in users txt wheter it is user object or reader object, can be identified with this pattern
                    if user_info:       # if the pattern has a result
                        if user_info.group(5) != "":        # if the result select a Reader object of favourite book list attribute
                            favourite_book_list = re.findall(r"'(.*?)'", user_info.group(5))    # identify each element of favourite book list of particular reader object
                        if user_info.group(6) != "":        # if the result select a Reader object of bookmark list attribute
                            bookmark_list = re.findall(r"\('(.*?)', '(.*?)'\)", user_info.group(6))     # identify each element of favourite book list of particular reader object
                        an_object = Reader(user_id = user_info.group(1),\
                                        user_name = user_info.group(2),\
                                        user_password = user_info.group(3),\
                                        user_role = user_info.group(4),\
                                        favourite_book_list = favourite_book_list,\
                                        bookmark_list = bookmark_list)               # Create a user object with existing data of favourite book list and bookmark list
                        UserOperation.user_info_list.append(an_object)          # insert reader object to user_info_list
                        favourite_book_list = []    # clear the list of favourite book list for the next user
                        bookmark_list = []          # clear the list of bookmark list for the next user
                    else:
                       user_info = re.search(r"^(.*?);;;(.*?);;;(.*?);;;(.*?)$", value, re.MULTILINE and re.DOTALL)     # if the pattern not a reader object, then select a User object with this pattern
                       if user_info:        # if the pattern has result
                        an_object = User(user_id = user_info.group(1),\
                                            user_name = user_info.group(2),\
                                            user_password = user_info.group(3),\
                                            user_role = user_info.group(4))     # create user object based on user pattern search in users.txt
                        UserOperation.user_info_list.append(an_object)      # insert reader object to user_info_list

            return True, f">>>>>>>>>> Load User Info Success...!"                           # return true if operation success
        except TypeError:
            return False, f">>>>>>>>>> Load User Info Failed: Type Error...!"               # return false with particular message if operation failed
        except AttributeError:
            return False, f">>>>>>>>>> Load User Info Failed: Attribute Error...!"
        except FileNotFoundError:
            return False, f">>>>>>>>>> Load User Info Failed: File Not Found Error...!"
        except RuntimeError:
            return False, f">>>>>>>>>> Load User Info Failed: Runtime Error...!"
    
    def user_registration(user_name, user_password, user_role = "Reader"):
        """
        Create a user object and save it in user_info_list list. Requires three arguments which is
        user_name, user_password, and user_role. If user role argument is not defined, it is a 
        'Reader' by default. Returns True if registration succeed, returns False with particular
        message if the registration Failed.
        """
        existing_id_list     = []   # a list for containing id list from user object
        existing_name_list   = []   # a list for containing name list from user object
        try:
            for index in range(len(UserOperation.user_info_list)):  # extract information from user object to container lists
                an_object = UserOperation.user_info_list[index]
                existing_id_list.append(an_object.user_id)          
                existing_name_list.append(an_object.user_name)
            
            user_id = random.randint(1000000000,9999999999) # generate a random 10 digit user_id
            while str(user_id) in existing_id_list :   
                user_id = random.randint(1000000000,9999999999) # if the generated user_id has duplicates, then generate another number
            
            if str(user_name) not in existing_name_list:    # if the username is unique from existing username
                user_object = User(user_id = user_id,\
                                    user_name = user_name,\
                                    user_password = user_password,\
                                    user_role = user_role)      # create a new User object
                UserOperation.user_info_list.append(user_object)    # insert the new user object to user info list
                return True, f">>>>>>>>>> You have successfully registered a user"      # return True if the user registration succeed
            else:
                return False, f">>>>>>>>>> That particular name has been taken. Try another user name."     # return False with particular error message if registration failed
        except AttributeError:
            return False, f">>>>>>>>>> Attribute Error"
        except RuntimeError:
            return False, f">>>>>>>>>> Runtime Error"
    
    def user_login(user_name, user_password):
        """
        Authenticate a user login attempt. Requires two argument to be matched which is user name and
        user password. Returns True if the user name and password us match, returns False if the user
        name and password did not match or some error happens with particular messages.
        """
        user_login_dict     = {}    # a dictionary container to match the user name and password

        try:
            for index in range(len(UserOperation.user_info_list)):  # extract from user info list, usernames and passwords, to dictionary
                an_object = UserOperation.user_info_list[index]
                user_login_dict.update({an_object.user_name:an_object.user_password})
                
            if str(user_name) in user_login_dict.keys():    # if the username is existed in dictionary
                if user_login_dict[user_name] == user_password:     # verify the username by password based on dictionary
                    return True, f">>>>>>>>>> You have successfully logged in"      # if username and password match, then returns True
                else:
                    return False, f">>>>>>>>>> Wrong password, try again"       # if username and password did not match, returns False with error messages
            else:
                return False, f">>>>>>>>>> Username does not exist. Please register a user."    # if username did not exist yet in the system, returns False with error message
        except AttributeError:
            return False, f">>>>>>>>>> Attribute Error"     # returns False with error message if user login fails
        except RuntimeError:
            return False, f">>>>>>>>>> Runtime Error"

    def write_user_info():
        """
        Write all the user's information provided in user_info_list class variable
        in the provided file located in user_info_path class variable. Requires no
        arguments. Returns true if the operation to write the data to users.txt
        succeeded. Returns False if the writing failed.
        """
        try:
            with open (UserOperation.user_info_path, 'w', encoding="utf8") as user_file:    # access the user.txt and write mode
                for index in range(len(UserOperation.user_info_list)):      # write every user or reader object to users.txt
                    user_file.write(str(UserOperation.user_info_list[index]) + '\n')    # every line in users.txt separated by newline character
            os.chdir('../../')      # working directory being back twice as the result of opening a file with relative path
        except TypeError:
            return False, f">>>>>>>>>> Type Error"  # return False with particular error messages if writing operation failed
        except FileNotFoundError:
            return False, f">>>>>>>>>> FileNotFound Error"
        except RuntimeError:
            return False, f">>>>>>>>>> Runtime Error"
        else:
            return True, f">>>>>>>>>> Write user info succeed..!"   # return True if writing operation succeed