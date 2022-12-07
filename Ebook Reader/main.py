"""
ASSIGNMENT 3 - ITI9136 - INTRODUCTION TO PYTHON
Name                    : Fajar Witama Wijaya
Student ID              : 33452784
Creation Date           : November 15th, 2022
Last Modified Date      : November 27th, 2022
"""

import re   # used to search string pattern
from book_operation     import BookOperation    as BO   # used for operation of book object
from user_operation     import UserOperation    as UO   # used for operation of user object
from reader             import Reader                   # used to create a reader object
from reader_operation   import Reader_Operation as RO   # used for operation of reader object

def login_reg_menu():
    """
    This page is the first page before the user use the application. The user can login
    to appilcation if already has a user. Register first if the user have not had one.
    Requires no argument, return the option which users made with its text, 
    """
    login_reg_display = ""  # a string container to create a menu
    login_reg_list = [
        "Login",
        "Register",
        "Exit Program"
    ]   # a list of string menu
    for each_menu in login_reg_list:
        login_reg_display += f"{(login_reg_list.index(each_menu)+1)}. {each_menu}\n"    # append formatted string to string container
    print(f"\n<<<<<<<<<<<<<<<<<< FINDLE >>>>>>>>>>>>>>>>>>")    # FINDLE application header
    print(f"____________built to read a book____________\n")
    print(f"{login_reg_display}")       # display list of string menu with a formatted string
    login_reg_opt = input(f"Select '1' to login, '2' to register, '3' to exit program: ")   # prompts user to input
    if login_reg_opt.isdigit():             # if users enter digit character
        login_reg_opt = int(login_reg_opt)  # convert string to int
        if login_reg_opt >= 1 and login_reg_opt <= 3:   # if the digits is between 1 to 3
            return login_reg_opt, login_reg_list[login_reg_opt - 1]     # returns the option which users made with its string
        else:
            print(f"Please input using number from the menu available!")    # print error message if the user did not enter value correctly
    else:
        print(f"Input is invalid. Please input using number from the menu available!")

def login_page():
    """
    This it the page where the user can input their username and password. If the username
    and password is not match, the access to the application will be denied. If the username
    and password is match, the user will be directed to main menu. Requires no arguments,
    returns True if the username and password is match, otherwise returns False with particular
    error message.
    """
    login_username = input(f"Enter your username: ")    # prompts the user to input username
    login_password = input(f"Enter your password: ")    # prompts the user to input password
    user_login_flag, login_message = UO.user_login(login_username, login_password)  # call user login method to verify the match
    if user_login_flag:             # if username and password match
        print(f"{login_message}")
        return True, login_username     # returns True
    else:
        print(f"{login_message}")       
        return False, login_username    # return False if username and password did not match or any error happens
   
def register_page():
    """
    This it the page where the user can register a new user to access the application.
    User will be prompt to insert a new username which should not be in the existing
    username, and should insert a particular password for that user, which is case-sensitive.
    Requires no arguments, returns True if the registration succeed, False if the registation
    Fails.
    """
    user_role_null = True   # a condition to make a while loop
    
    reg_username = input(f"Enter your new username: ")      # prompts the user to input username
    reg_password = input(f"Enter your password: ")          # prompts the user to input username
    while user_role_null:
        reg_user_role = input(f"(*optional, hit Enter if you want to skip) What is your role? a [1] Reader or an [2] Administrator: ")      # prompts the user to input user role
        if reg_user_role.isdigit():     # if user enter a value which is digits
            reg_user_role = int(reg_user_role)  # converts string to int
            if reg_user_role == 2: 
                reg_user_role = "Administrator" # user role as administrator if user enters 2
                user_reg_flag, reg_message = UO.user_registration(reg_username, reg_password, reg_user_role) # entering the username, password and role to register with user_registration method
                user_role_null = False  # break the loop
            else:
                user_reg_flag, reg_message = UO.user_registration(reg_username, reg_password)   # if the user did not enter the user role, use default value
                user_role_null = False  # break the loop
        elif reg_user_role.isalpha():   # if user enter a wrong input
            print(">>>>>>>>>> Wrong input, enter '1' or '2' or just hit Enter to skip")
        else:
            user_reg_flag, reg_message = UO.user_registration(reg_username, reg_password) #or if user enter a random number, use a default value of user role
            user_role_null = False      # break the loop
    if user_reg_flag:       # if the registration succeed
        print(f"{reg_message}")
        return True             # returns True
    else:
        print(f"{reg_message}")     # if the registration fails, returns False with particular error message
        return False

def menu():
    """
    This function is to display menu and capture the input from the user. Requires 
    no argument. Returns menu_opt and menu_list. 
    """
    while True:     # a condition to create a while loop
        menu_display = ""   # a container to contains strings
        menu_list = [
            "List of Book Titles",
            "Favourite Books Menu",
            "Bookmarks Menu",
            "Search by Book Authors",
            "Books by Year of Release",
            "Update Books Library",
            "Log Out User"
        ]       # a string of main menu
        for each_menu in menu_list:
            menu_display += f"{(menu_list.index(each_menu)+1)}. {each_menu}\n"  # appends to string container each main menu string with formatted string
        print(f"\n<<<<<<<<<<<<<<<<<< FINDLE >>>>>>>>>>>>>>>>>>")    # this is a application header
        print(f"____________built to read a book____________\n")
        print(f"{menu_display}")        # display main menu from string container
        menu_opt = input(f"Select menu: ").strip() # capture the input from user
        if menu_opt.isdigit():              # if the user input digits
            menu_opt = int(menu_opt)        # convert string to int
            if menu_opt >= 1 and menu_opt <= 7: # to make sure that the user input only from the available menu
                return menu_opt, menu_list[menu_opt - 1]    # returns menu opt with its string
            else:
                print(f">>>>>>>>>> Please input using number from the menu available!")     # return error message if user enters invalid input
        else:
            print(f">>>>>>>>>> Input is invalid. Please input using number from the menu available!")

def sub_menu_title(book_title) ->str :
    """
    This function is to display the sub menu of the program. Requires one argument which
    is book_title. Returns sub_menu_opt.
    """
    print(f"\n================ Book Title: {book_title} ================\n"
          "1. Read Book Info\n"
          "2. Read Book Contents\n"
          "3. Read Book Text\n"
          "4. Back to Menu"
         )          # display of submenu
    sub_menu_opt = input(f"Select menu: ").strip() #capture the input from the user
    if sub_menu_opt.isdigit() and sub_menu_opt != "0": # to handle the input from the user 
        sub_menu_opt = int(sub_menu_opt)
        if sub_menu_opt >= 1 and sub_menu_opt <= 4: # to make sure that the user input only from the available menu
            return sub_menu_opt #return if the user has chosen from the available menu
        else:
            print(f">>>>>>>>>> Please input using number from the menu available!")     # return error message if user enters invalid input
    else:
        print(f">>>>>>>>>> Input is invalid. Please input using number from the menu available!")

def read_book_info(book_title) -> str:
    """
    This function has one positional argument named book_title
    This funcition is to display book_info such as:
    1. Book Title
    2. Number of chapters
    3. Number of lines
    4. Number of words
    """
    try:
        book_info = BO.get_counts(book_title)       # book info as a tuple container from get_counts function
        print("\n--------------- Book Information --------------")
        print(f"Book Title:          {book_title}")
        print(f"Number of chapters:  {book_info[0]}")
        print(f"Number of lines:     {book_info[1]}")
        print(f"Number of words:     {book_info[2]}")
        print("--------------------- END ---------------------") # display of book info value to a formatted string
    except RuntimeError:        # an exception if any error happens
        print(">>>>>>>>>> Runtime Error")

def favourite_book_menu(reader_object):
    """
    This function is to display all favourite books. Requires one argument
    which is reader object. Returns nothing, just a display menu to navigate
    favourite book list
    """
    fb_menu_flag = True     # a condition to create a while loop
    args_tuple = tuple()    # a container to handle multi-argument statements to add or delete favourite books

    try:
        while fb_menu_flag:
            print(f"\n================ Favourite Books List ================")
            favorite_book = RO.show_all_favourite_book(reader_object)   # display existing favourite books from reader object
            print(favorite_book)
            print(f"\n================ Favourite Books Menu ================")
            print(f"1. Add New Favourite Book")
            print(f"2. Delete New Favourite Book (can handle multiple argument: 2 followed by row list i.e., 2 3 4 5)")
            print(f"3. Back to Main Menu")

            fb_menu_opt = input(f"Select menu: ").strip() #capture the input from the user
            if len(fb_menu_opt)>1:                          # if user using multi-argument to delete many favourite books
                args_list = fb_menu_opt.split()             # create a list of arguments, space as a separator
                for each in args_list:                      # process each arguments
                    if each.isdigit():                      # if argument is digits
                        each = int(each)                    # convert string to int
                        if each >= 1 and each <= len(reader_object.favourite_book_list):    # if the digits is between 1 and max favourite book list
                            args_tuple = list(args_tuple)
                            args_tuple.append(each)         # enter the argument to a tuple
                            args_tuple = tuple(args_tuple)
                    else:
                        print(">>>>>>>>>> Wrong bookmark command")  # if user input non digits character
                        args_tuple = list(args_tuple)               
                        args_tuple = []                     # clear tuples
                        args_tuple = tuple(args_tuple)
                if args_tuple[0] == 2:              # if the first element of tuple is '2' which is delete command
                    args_tuple = list(args_tuple)
                    args_tuple.pop(0)               # clear the command from the tuple
                    args_tuple = tuple(args_tuple)
                    if reader_object.favourite_book_list:   # if the reader object has favourite book list
                        for title_row_num in args_tuple:
                            print(f">>>>>>>>>> A book title of '{reader_object.favourite_book_list[title_row_num - 1]}' has been deleted from favourite book list")
                            RO.delete_favourite_book(title_row_num, reader_object)  # calling delete_favourit_book to delete certain favourite books
                        args_tuple = list(args_tuple)
                        args_tuple = []                 # clear tuple
                        args_tuple = tuple(args_tuple)
                    else:
                        print(f">>>>>>>>>> No favourite book exists")   # if the reader object has no favourite book list
                else:
                    print(">>>>>>>>>> Wrong bookmark command")
                    args_tuple = list(args_tuple)
                    args_tuple = []                 # clear tuple
                    args_tuple = tuple(args_tuple)
            else:                                   # if the user only use a single argument to add/delete
                if fb_menu_opt.isdigit():           # if user enters digit character
                    fb_menu_opt = int(fb_menu_opt)  # convert string to int
                    if fb_menu_opt >= 1 and fb_menu_opt <= 3: # to make sure that the user input only from the available menu
                        if fb_menu_opt == 1:    # if the user want to add favourite book
                            page_number = input(f"Enter the page number of the book's titles you want to display: ").strip()
                            if page_number.isdigit(): # to capture the input from the user (page number)
                                page_number = int(page_number) # convert to int
                                if len(BO.book_title_list) % 10: # to find the max_page using the sum of all titles
                                    max_page = (len(BO.book_title_list)//10) + 1
                                else:
                                    max_page = len(BO.book_title_list)//10
                                if page_number >= 1 and page_number <= max_page: # to handle if the user input is in the range of the page number
                                    book_title = BO.display_titles(page_number) # the chosen book will be stored in variable book_title to be used in sub menu
                                    if book_title:
                                        RO.save_favourite_book(book_title, reader_object)   # add favourite book by calling save_favourite_book method
                                        print(f">>>>>>>>>> A book title of '{book_title}' has been added to favorite list") # a message to tell the user certain book has been favourited
                        elif fb_menu_opt == 2:      # if the user want to delete favourite book
                            if reader_object.favourite_book_list:   # if the reader object already has favourite book list
                                del_favorite = input('Enter title number from the list to delete: ')    # ask user to input which book to delete from favourite book list
                                if del_favorite.isdigit(): # to capture the input from the user (book title numbering)
                                    del_favorite = int(del_favorite) # convert to int
                                    if del_favorite >= 1 and del_favorite <= len(reader_object.favourite_book_list):    # make sure the user input is in range of favourite book list
                                        print(f">>>>>>>>>> A book title of '{reader_object.favourite_book_list[del_favorite - 1]}' has been deleted from favorite list")
                                        RO.delete_favourite_book(del_favorite, reader_object)   # delete certain favourite book by calling delete_favourite_book method
                                    else:
                                        print(f">>>>>>>>>> wrong input title number.")  # error messages if user input incorrectly
                                else:
                                    print(f">>>>>>>>>> wrong input of title number. Enter digits only")
                            else:
                                print(f">>>>>>>>>> No favorite books exists")   # if reader object has no favourite books to delete
                        elif fb_menu_opt == 3:
                            fb_menu_flag = False # break the loop
                    else:
                        print(f">>>>>>>>>> Please input using number from the menu available!")     # error messages if user input incorrectly
                else:
                    print(f">>>>>>>>>> Please input using number from the menu available!")
    except IndexError:                                  # exceeption to handle any error when favourite book operation failures
        print(f"Something went wrong, try again")
    except AttributeError:
        print(f"Attribute Error")
    except RuntimeError:
        print(f"Runtime Error")


def bookmark_menu(reader_object):

    """
    This function is to display the bookmark menu. Requires one argument which is
    reader object. Returns nothing, just a display menu to navigate favourite book list
    """
    bm_menu_flag = True     # a condition to create a loop
    args_tuple = tuple()    # a container to handle multi-argument statements to add or delete bookmarks

    try:
        while bm_menu_flag:
            print(f"\n================ Bookmarks List ================")
            all_bookmarks = RO.show_all_bookmarks(reader_object)    # display existing bookmarks from reader object
            print(all_bookmarks)
            print(f"\n================ Bookmarks Menu ================")
            print(f"1. Add New Bookmark")
            print(f"2. Delete a Bookmark (can handle multiple argument: 2 followed by row list i.e., 2 3 4 5)")
            print(f"3. Back to Main Menu")

            bm_menu_opt = input(f"Select menu: ").strip() #capture the input from the user
            if len(bm_menu_opt)>1:                      # if user using multi-argument to delete many bookmarks
                args_list = bm_menu_opt.split()         # create a list of arguments, space as a separator
                for each in args_list:                  # process each arguments
                    if each.isdigit():                  # if argument is digits
                        each = int(each)                # convert string to int
                        if each >= 1 and each <= len(reader_object.bookmark_list):      # if the digits is between 1 and max bookmarks list
                            args_tuple = list(args_tuple)
                            args_tuple.append(each)         # enter the argument to a tuple
                            args_tuple = tuple(args_tuple)
                    else:
                        print(">>>>>>>>>> Wrong bookmark command")  # if user input non digits character
                        args_tuple = list(args_tuple)
                        args_tuple = []                     # clear tuples
                        args_tuple = tuple(args_tuple)
                if args_tuple[0] == 2:                      # if the first element of tuple is '2' which is delete command
                    args_tuple = list(args_tuple)
                    args_tuple.pop(0)                       # clear the command from the tuple
                    args_tuple = tuple(args_tuple)
                    if reader_object.bookmark_list:         # if the reader object has bookmark list
                        for title_row_num in args_tuple:
                            print(f">>>>>>>>>> A book title of '{reader_object.bookmark_list[title_row_num - 1][0]}' page number '{reader_object.bookmark_list[title_row_num - 1][1]}' has been deleted from bookmark list")
                            RO.delete_bookmark(title_row_num, reader_object)    # calling delete_bookmark to delete certain bookmarks
                        args_tuple = list(args_tuple)
                        args_tuple = []                 # clear tuple
                        args_tuple = tuple()
                    else:
                        print(f">>>>>>>>>> No bookmarks exists")         # if the reader object has no bookmarks list
                else:
                    print(">>>>>>>>>> Wrong bookmark command")
                    args_tuple = list(args_tuple)
                    args_tuple = []                     # clear tuple
                    args_tuple = tuple(args_tuple)
            else:                                       # if the user only use a single argument to add/delete
                if bm_menu_opt.isdigit():               # if user enters digit character
                    bm_menu_opt = int(bm_menu_opt)      # convert string to int
                    if bm_menu_opt >= 1 and bm_menu_opt <= 3: # to make sure that the user input only from the available menu
                        if bm_menu_opt == 1:        # if the user want to add bookmarks
                            page_number = input(f"Enter the page number of the book's titles you want to display: ").strip()
                            if page_number.isdigit(): # to capture the input from the user (page number)
                                page_number = int(page_number) # convert to int
                                if len(BO.book_title_list) % 10: # to find the max_page using the sum of all titles
                                    max_page = (len(BO.book_title_list)//10) + 1
                                else:
                                    max_page = len(BO.book_title_list)//10
                                if page_number >= 1 and page_number <= max_page: # to handle if the user input is in the range of the page number
                                    book_title = BO.display_titles(page_number) # the chosen book will be stored in variable book_title to be used in sub menu
                                    if book_title:  # if the user has chosen a book title
                                        chosen_book_path = BO.book_initial_folder + BO.book_info_dict[book_title].book_path # search the book using the path stored in book object
                                        with open(chosen_book_path, "r", encoding="utf8") as a_book_text: # open the book that has been chosen by the user
                                            whole_book_text = a_book_text.read()
                                        search_text = re.search(BO.start_end_pattern, whole_book_text, re.IGNORECASE and re.MULTILINE and re.DOTALL) # search the content of the book using pattern
                                        clean_text = search_text.group(1) # capture the found pattern
                                        book_lines  = clean_text.splitlines() # split the book per line
                                        if len(book_lines) % 15: # to find if the book remain is not 0 if divided by 15
                                            total_pages = len(book_lines) // 15 + 1 # if the remain is not 0, then the total page is floor divided by 15 and then added by 1 
                                        else:
                                            total_pages = len(book_lines) // 15 # if the remain is 0, then keep the total page as it is (equal to length of book_lines)
                                        page_number = input(f"Enter the page number of the book you want to read: ").strip() # capture the input from the user
                                        if page_number.isdigit():       # if the user enters digits character
                                            page_number = int(page_number)  # convert string to int
                                            if page_number >=1 and page_number<=total_pages:    # if the page number is within the range of 1 to total pages
                                                page_number = int(page_number)
                                                args_tuple = BO.show_book_text(book_title, page_number)  # show book text, returns a tuple of the page of bookmark which the user inputs
                                        else:       
                                            print(">>>>>>>>>> Please enter using number!")  # error message if the user put an incorrect input
                                        if args_tuple[0] == 1:  # evaluates the first element of tuple, if '1' then it is the command to add bookmark
                                            args_tuple = list(args_tuple)
                                            args_tuple.pop(0)   # removing command element from tuple
                                            args_tuple = tuple(args_tuple)
                                        for page in args_tuple: # for each bookmark page
                                            RO.add_bookmark(book_title, page, reader_object)    # add to bookmark list by calling add_bookmark method
                                            print(f">>>>>>>>>> A book title of '{book_title}' page number '{page}' has been added to bookmark list")    # additional information to user which books has been added to bookmark list
                                        args_tuple = list(args_tuple)
                                        args_tuple = []         # clear tuple
                                        args_tuple = tuple()
                        elif bm_menu_opt == 2:      # if the user wants to delete a bookmark
                            if reader_object.bookmark_list:     # if the reader object has existing bookmark list
                                del_bookmark = input('Enter title number from the list to delete: ')    # prompts the user to input which favourite book to delete
                                if del_bookmark.isdigit(): # to capture the input from the user (book title numbering)
                                    del_bookmark = int(del_bookmark) # convert to int
                                    if del_bookmark >= 1 and del_bookmark <= len(reader_object.bookmark_list):  # make sure the digits is still in range of 1 to bookmark list
                                        print(f">>>>>>>>>> A book title of '{reader_object.bookmark_list[del_bookmark - 1][0]}' page number '{reader_object.bookmark_list[del_bookmark - 1][1]}' has been deleted from bookmark list")
                                        RO.delete_bookmark(del_bookmark, reader_object)     # delete a particular bookmark by calling delete_bookmark method
                                    else:
                                        print(f">>>>>>>>>> wrong input title number.")  # error messages if user enter an incorrect inputs
                                else:
                                    print(f">>>>>>>>>> wrong input of title number. Enter digits only")
                            else:
                                print(f">>>>>>>>>> No bookmarks exists")   # if the reader object has no bookmarks to delete
                        elif bm_menu_opt == 3:
                            bm_menu_flag = False    # break the loop
                        else:
                            print(f">>>>>>>>>> Please input using number from the menu available!")     # error messages if user enter an incorrect inputs
                    else:
                        print(f">>>>>>>>>> Please input using number from the menu available!")
                else:
                    print(f">>>>>>>>>> Input is invalid. Please input using number from the menu available!")
    except IndexError:                                  # exception to handle if any error happens within the navigation of bookmark menu
        print(f"Something went wrong, try again")
    except AttributeError:
        print(f"Attribute Error")
    except RuntimeError:
        print(f"Runtime Error")

def book_authors_display(author_name) -> str:
    """
    This function has one positional argument named author_name
    This funcition is to display the name of specified author entered by the user
    """
    author_search_result = BO.get_book_by_author(author_name)
    print(f"---------------- Books by {author_name} ----------------")
    print(f"{author_search_result}")
    print(f"---------------------------- END ----------------------------")

def main():
    """
    This is main function to handle the logics and flows of the program
    """
    book_title = ""             # a string container
    menu_opt = ""               # a string container
    menu_name = ""              # a string container
    sub_menu_opt = ""           # a string container
    login_username = ""         # a string container
    program_running = True      # a condition to create a while loop
    login_success = False       # a condition to create a while loop
    args_tuple = tuple()        # a condition to handle multi-argument command

    print(">>>>>>>>> Initializing .... >>>>>>>>>")  # a message to the user to wait for initializing
    EBI_flag, EBI_msg = BO.extract_book_info() # extract the book info and store it into particular format in books.txt 
    LBI_flag, LBI_msg = BO.load_book_info() # load the book info from books.txt and store it to book_title_list and book_info_dict
    LUI_flag, LUI_msg = UO.load_user_info() # load user info from users.txt and store it in a user object
    print(f"{EBI_flag} {EBI_msg}\n{LBI_flag} {LBI_msg}\n{LUI_flag} {LUI_msg}")  # print the status of each initialitation

    while program_running:  
        login_reg_opt, login_reg_choice = login_reg_menu()  # user enter a login/registration menu
        print(f"You chose {login_reg_opt}: {login_reg_choice}") # to give info to the user
        if login_reg_opt == 1:  # user wants to login
            login_success, login_username = login_page()    # check whether the login is successful or not
        elif login_reg_opt == 2:    # user wants to register a new user
            register_page()         
        elif login_reg_opt == 3:    # user wants to exit the program
            WUI_flag, WUI_msg = UO.write_user_info()    # write the user object and or reader object in user info list to users.txt by calling write user info method
            print(WUI_flag, WUI_msg)    # print the status of write user info method
            print(f"Exiting Program...")
            program_running = False     # break the loop
            break

        while login_success: # to display the menu. This will be terminated if the user chooses to log out
            for index in range(len(UO.user_info_list)): # creates reader object after a user had successfully logged in
                if UO.user_info_list[index].user_name == login_username:    # try to match which user/reader object to use
                    if isinstance(UO.user_info_list[index], Reader):    # if the reader object is selected
                        insert_index = index
                        reader_object = Reader(UO.user_info_list[index].user_id, UO.user_info_list[index].user_name,\
                                                UO.user_info_list[index].user_password, UO.user_info_list[index].user_role,\
                                                UO.user_info_list[index].favourite_book_list, UO.user_info_list[index].bookmark_list)   # extract from user info list to create reader object
                    else:   # if a user object which has never been logged in, create a new reader object
                        insert_index = index
                        reader_object = Reader(UO.user_info_list[index].user_id, UO.user_info_list[index].user_name,\
                                                UO.user_info_list[index].user_password, UO.user_info_list[index].user_role) # extract from user info list to create a new reader object
                
            menu_opt, menu_name = menu()    # enter the main menu
            print(f"You chose menu {menu_opt}: {menu_name}") # to give info to the user
            if menu_opt == 1:   # user wants to navigate to a list of book titles
                page_number = input(f"Enter the page number of the book's titles you want to display: ").strip()
                if page_number.isdigit(): # to capture the input from the user (page number)
                    page_number = int(page_number) # convert to int
                    if len(BO.book_title_list) % 10: # to find the max_page using the sum of all titles
                        max_page = (len(BO.book_title_list)//10) + 1
                    else:
                        max_page = len(BO.book_title_list)//10
                    if page_number >= 1 and page_number <= max_page: # to handle if the user input is in the range of the page number
                        book_title = BO.display_titles(page_number) # the chosen book will be stored in variable book_title to be used in sub menu
                        if book_title:
                            print(f"You chose: {book_title}")
                            while True: # enter the sub menu once the user have chosen a book
                                sub_menu_opt = sub_menu_title(book_title)
                                if sub_menu_opt == 1: # if the user chose sub menu 1 then show the book info
                                    read_book_info(book_title)
                                elif sub_menu_opt == 2: # if the user chose sub menu 2 then show the book content
                                    print(BO.show_book_content(book_title))
                                elif sub_menu_opt == 3: # if the user chose sub menu 3 then show the content of the book
                                    page_number = input(f"Enter the page number of the book you want to read: ").strip() # capture the input from the user
                                    if page_number.isdigit() and page_number != "0":
                                        try:
                                            page_number = int(page_number)
                                            args_tuple = BO.show_book_text(book_title, page_number) # the user can add bookmarks while reading the book text. The bookmark page is insert to args_tuple (multiple arguments)
                                            if args_tuple[0] == 1:      # if the first element of tuple is '1', then it is add bookmark command
                                                args_tuple = list(args_tuple)
                                                args_tuple.pop(0)               # clear command element in tuple
                                                args_tuple = tuple(args_tuple)
                                            for page in args_tuple:         # for each page in args_tuple
                                                RO.add_bookmark(book_title, page, reader_object)    # add new bookmark by calling add_bookmark method
                                                print(f">>>>>>>>>> A book title of '{book_title}' page number '{page}' has been added to bookmark list")
                                            args_tuple = list(args_tuple)
                                            args_tuple = []         # clear tuples for the next user/operation
                                            args_tuple = tuple()
                                        except RuntimeError as e:   # handles any error within reading book operation
                                            print(f">>>>>>>>>> Runtime Error")
                                    else:
                                        print(">>>>>>>>>> Please enter using number!")
                                elif sub_menu_opt == 4: # exit from sub-menu
                                    break
                                else:
                                    print(">>>>>>>>>> Please enter using the number available!")
                    else:
                        print(f">>>>>>>>>> There are only 1 - {max_page} page numbers available!")
                else:
                    print(f">>>>>>>>>> Invalid input, please choose using the number available!")

            elif menu_opt == 2:
                favourite_book_menu(reader_object)  # user wants to navigate to favourite book menu
            elif menu_opt == 3:
                bookmark_menu(reader_object)        # user wants to navigate to bookmarks menu
            elif menu_opt == 4: # if the user chose menu 2 then ask for the name of the author that the user wants to search
                author_name = input(f"Input the name of the author you want to search: ").strip()
                book_authors_display(author_name)

            elif menu_opt == 5: # if the user chose menu 3 then show the release year
                print(BO.get_book_release_year())

            elif menu_opt == 6: # if the user chose menu 4 then extract and load the book info
                print(BO.extract_book_info())
                print(BO.load_book_info())
                    
            elif menu_opt == 7: # if the user chose menu 5 then log out from user
                UO.user_info_list.pop(insert_index)                     # Everytime the user log out, to handles duplicate, pop this reader object
                UO.user_info_list.insert(insert_index, reader_object)   # place the new updated reader object to the same index in user info list
                login_success = False   # break the loop
                break

    
if __name__ == '__main__':
    main()
