"""
ASSIGNMENT 3 - ITI9136 - INTRODUCTION TO PYTHON
Name                    : Fajar Witama Wijaya
Student ID              : 33452784
Creation Date           : November 15th, 2022
Last Modified Date      : November 27th, 2022
"""

class Reader_Operation:
    """
    Contains all the operations related to a reader.
    """
    
    def add_bookmark(book_title, page, reader_object):
        """
        Add specified reader's bookmarked (i.e., title and page#) to the
        bookmark_list list. Requires three arguments which is book_title,
        page, and reader_object. Returns nothing only doing specific task.
        """
        reader_object.bookmark_list.append((book_title, page))      # inserting a tuple of book_title and page arguments to bookmark list of reader object
    
    def delete_bookmark(num, reader_object):
        """
        Delete the specified reader's bookmark based on the index from
        bookmark_list list. Requires two arguments which is num and 
        reader object. Returns nothing only doing specific task.
        """
        reader_object.bookmark_list.pop(num - 1)        # deleting a value in (num - 1) index in bookmark list of reader object
    
    def show_all_bookmarks(reader_object):
        """
        Display all Reader's bookmarks. Requires one argument which is
        reader_object. Return the string of list of all bookmarks from
        reader object
        """
        a_string = ""   # defines an empty string as a container

        if reader_object.bookmark_list:     # if the reader object has bookmark list
            for index in range(len(reader_object.bookmark_list)):   
                a_string += f"{index+1}. {reader_object.bookmark_list[index]}\n"    # append every bookmark in reader object to a formatted string
            return a_string
        else:   # if the reader object has no bookmark list
            return f">>>>>>>>>> No bookmarks exists"
    
    def save_favourite_book(book_title, reader_object):
        """
        Add the specified reader's favourite book (i.e., title) in 
        favourite_book_list list. Requires two arguments which is
        book_title and reader_object. Returns nothing only doing
        specific task.
        """
        reader_object.favourite_book_list.append(book_title)    # append book title argument to favourite book list of reader object
    
    def delete_favourite_book(num, reader_object):
        """
        Remove the specified reader's favourite book from 
        favourite_book_list list. Requires two arguments
        which is num and reader_object.  Returns nothing
        only doing specific task.
        """
        reader_object.favourite_book_list.pop(num - 1)      # deleting a value in (num - 1) index in favourite book list of reader object
    
    def show_all_favourite_book(reader_object):
        """
        Display all the Reader's favourite books. Requires one
        argument which us reader_object. Return the string of
        list of all favourite books from reader object
        """
        a_string = ""       # defines an empty string as a container

        if reader_object.favourite_book_list:       # if the reader object has favourite book list
            for index in range(len(reader_object.favourite_book_list)):
                a_string += f"{index+1}. {reader_object.favourite_book_list[index]}\n"      # append every favourite book in reader object to a formatted string
            return a_string
        else:        # if the reader object has no favourite book list
            return f">>>>>>>>>> No Favourite book exists"
    