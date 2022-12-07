"""
ASSIGNMENT 3 - ITI9136 - INTRODUCTION TO PYTHON
Name                    : Fajar Witama Wijaya
Student ID              : 33452784
Creation Date           : November 15th, 2022
Last Modified Date      : November 27th, 2022
"""
import os
import re
import string
from book import Book
from reader import Reader
from reader_operation import Reader_Operation as RO

class BookOperation:
    """
    Contains all the operations related to a book.
    And below several class variable declaration that are used in this Class
    """
    book_title_list = []
    book_info_dict = {}
    start_end_pattern = r"\*\*\* START.*?\*\*\*\n(.*)(?:\*\*\* END)"
    book_chapter_pattern = r"contents\n\n( ..introduction.*?\n)\n|( .?chapter i.*?)\n\n|( letter 1.*?\n\n)|( I\. .*?\n II\. .*?\n\n\n\n\n)|contents\n\n\n(.*?\n\n\n\n\n)|contents.\n\n(chapter i.*?)\n\n\n"
    book_initial_folder = os.getcwd() #https://www.geeksforgeeks.org/python-os-chdir-method/ --> capture the current working directory
    book_folder_path = r"\data\books_data" # relative path for the folder path
    book_info_path = r"\data\result_data\books.txt" # relative path for the info path (books.txt) 
    os.chdir(book_initial_folder + book_folder_path)

    def extract_book_info():
        """
        Extracts book attributes from each book contained within a folder (i.e.,
        book_folder_path) and writes these as a formatted string in a given file
        (i.e, book_info_path).
        Returns Success if the script running well, False if there is an exception.
        Below are the patterns that will be used inside this extract_book_info function.
        """
        book_title_pattern = r"title:((?:.*|\s)*?(?:^\s*$))"
        book_author_pattern = r"author:((?:.*|\s)*?(?:^\s*$))"
        book_language_pattern = r"language:(.*)"
        book_producer_pattern = r"produce.*?(?:by:?).?(.*)" 
        book_release_date_pattern = r"release date:?(.*\d{4})\s" 
        book_last_update_pattern = r".*updated:?(.*\d{4})"
        try:
            index = 0
            # count = 0 # is used to test strategy of each attribute in this function
            with open (BookOperation.book_initial_folder + BookOperation.book_info_path, 'w', encoding="utf8") as each: # open the books.txt
                each.write(f"") # clear all the content inside the books.txt
            for file in os.listdir(): #https://stackoverflow.com/questions/35672809/how-to-read-a-list-of-txt-files-in-a-folder-in-python
                if file.endswith(".txt"): # to check if the files is in txt format
                    with open(file, encoding="utf8") as each: # open each file inside the directory
                        the_book = each.read() # read the file
                    the_book_title = re.search(book_title_pattern, the_book, re.IGNORECASE | re.MULTILINE) # search the pattern of the title
                    if the_book_title: # if the pattern of the book's title is found
                        try:
                            the_book_title_sub = re.sub("\n", "", the_book_title.group(1)) # make multilines title into a single line
                            the_book_title_sub = re.sub(" +", " ", the_book_title_sub) # clean the multi-spaces into a single space 
                            the_book_title_sub = the_book_title_sub.lstrip(":").strip() # clean the ":" that might be found and strip left and right whitespaces
                            BookOperation.book_title_list.append(the_book_title_sub) # store the title into a list named book_title_list
                        except AttributeError:
                            the_book_title_sub = "" 
                        # count += 1
                        # print(f"{count}. {the_book_title_sub}") # this is test strategy

                        the_book_author = re.search(book_author_pattern, the_book, re.IGNORECASE | re.MULTILINE) # search the pattern of the author
                        if the_book_author:
                            try:
                                the_book_author_sub = re.sub("\n", "", the_book_author.group(1))
                                the_book_author_sub = re.sub(" +", " ", the_book_author_sub)
                                the_book_author_sub = the_book_author_sub.lstrip(":").strip()
                            except AttributeError:
                                the_book_author_sub = "" # if there's Attribute Error, then left the author empty
                            # count += 1
                        else:
                            the_book_author_sub = "" # if there's no pattern found, then left the author empty
                        
                        the_book_release_date = re.search(book_release_date_pattern, the_book, re.IGNORECASE | re.MULTILINE) # search the pattern of the release date
                        if the_book_release_date:
                            try:
                                the_book_release_date_sub = re.sub("\n", "", the_book_release_date.group(1))
                                the_book_release_date_sub = re.sub(" +", " ", the_book_release_date_sub)
                                the_book_release_date_sub = the_book_release_date_sub.lstrip(":").strip()
                            except AttributeError:
                                the_book_release_date_sub = "" # if there's Attribute Error, then left the release date empty
                            # count += 1
                        else:
                            the_book_release_date_sub = "" # if there's no pattern found, then left the release date empty

                        the_book_last_update = re.search(book_last_update_pattern, the_book, re.IGNORECASE | re.MULTILINE) # search the pattern of the last update
                        if the_book_last_update:
                            try:
                                the_book_last_update_sub = re.sub("\n", "", the_book_last_update.group(1))
                                the_book_last_update_sub = re.sub(" +", " ", the_book_last_update_sub)
                                the_book_last_update_sub = the_book_last_update_sub.lstrip(":").strip()
                            except AttributeError:
                                the_book_last_update_sub = "" # if there's Attribute Error, then left the last update empty
                            # count += 1
                        else:
                            the_book_last_update_sub = "" # if there's no pattern found, then left the last update empty

                        the_book_language = re.search(book_language_pattern, the_book, re.IGNORECASE | re.MULTILINE) # search the pattern of the language
                        if the_book_language:
                            try:
                                the_book_language_sub = re.sub("\n", "", the_book_language.group(1))
                                the_book_language_sub = re.sub(" +", " ", the_book_language_sub)
                                the_book_language_sub = the_book_language_sub.lstrip(":").strip()
                            except AttributeError:
                                the_book_language_sub = "" # if there's Attribute Error, then left the language empty
                            # count += 1
                        else:
                            the_book_language_sub = "" # if there's no pattern found, then left the language empty
                        
                        the_book_producer = re.search(book_producer_pattern, the_book, re.IGNORECASE | re.MULTILINE) # search the pattern of the producer
                        if the_book_producer:
                            try:
                                the_book_producer_sub = re.sub("\n", "", the_book_producer.group(1))
                                the_book_producer_sub = re.sub(" +", " ", the_book_producer_sub)
                                the_book_producer_sub = the_book_producer_sub.lstrip(":").strip()
                            except AttributeError:
                                the_book_producer_sub = "" # if there's Attribute Error, then left the producer empty
                            # count += 1
                        else:
                            the_book_producer_sub = "" # if there's no pattern found, then left the producer empty

                        # count += 1
                        # print(f"{count}. {the_book_producer_sub}; File: {file}") # this is test strategy
                        file_name = f"\{file}" # to capture the name of the book's file
                        with open (BookOperation.book_initial_folder + BookOperation.book_info_path, 'a', encoding="utf8") as each: # open the book's file to append data (per line)
                            # write the data into books.txt
                            each.writelines(f"{BookOperation.book_title_list[index]};;;{the_book_author_sub};;;{the_book_release_date_sub};;;{the_book_last_update_sub};;;{the_book_language_sub};;;{the_book_producer_sub};;;{BookOperation.book_folder_path + file_name}\n")
                            index += 1 # increment the index to store the data into the book title list

                        os.chdir(BookOperation.book_initial_folder + BookOperation.book_folder_path) # change the working directory back to main.py working directory

            return True, f">>>>>>>>>> Extract Book Info Success...!"
        except ValueError:
            return False, f">>>>>>>>>> Extract Book Info Failed: Value Error!"
        except RuntimeError:
            return False, f">>>>>>>>>> Extract Book Info Failed: Runtime Error!"
        
    
    def load_book_info():
        """
        Loads all the book's information from a given file (i.e., book_info_path)
        into the book_info_dict dictionary and the book_title_list list.
        Returns Success if the script running well, False if there is an axception.
        And also return a return message to be display in main.py
        and a book dictionary containing book_title_list & list_of_objects to be
        used in another function.
        """
        # below are the patterns that are used to search the pattern of each attribute
        data_title_pattern = r"(.*?);;;"
        data_author_pattern = r";;;(.*?);;;"
        data_release_date_pattern = r";;;(?:.*?);;;(.*?);;;"
        data_last_update_pattern = r";;;(?:.*?);;;(?:.*?);;;(.*?);;;"
        data_language_pattern = r";;;(?:.*?);;;(?:.*?);;;(?:.*?);;;(.*?);;;"
        data_producer_pattern = r";;;(?:.*?);;;(?:.*?);;;(?:.*?);;;(?:.*?);;;(.*?);;;"
        data_path_pattern = r";;;(?:.*?);;;(?:.*?);;;(?:.*?);;;(?:.*?);;;(?:.*?);;;(.*?)\n"
        try: # to catch any error
            BookOperation.book_info_dict.clear() # make sure the dictionary is clear / no data left
            BookOperation.book_title_list = [] # make sure the list is clear / no data left
            with open (BookOperation.book_initial_folder + BookOperation.book_info_path, 'r', encoding="utf8") as book_info: # open the books.txt
                for line, value in enumerate(book_info): # iterate for each line and store the line number into variable line and its string per line into var value 
                    title = re.search(data_title_pattern, value, re.IGNORECASE) # search for tittle
                    BookOperation.book_title_list.append(title.group(1)) # store the title into book_title_list
                    the_book_author_sub = re.search(data_author_pattern, value, re.IGNORECASE) # search for author
                    the_book_author_sub = the_book_author_sub.group(1) # store the found author into variable the_book_autor_sub
                    the_book_release_date_sub = re.search(data_release_date_pattern, value, re.IGNORECASE)
                    the_book_release_date_sub = the_book_release_date_sub.group(1)
                    the_book_last_update_sub = re.search(data_last_update_pattern, value, re.IGNORECASE)
                    the_book_last_update_sub = the_book_last_update_sub.group(1)
                    the_book_language_sub = re.search(data_language_pattern, value, re.IGNORECASE)
                    the_book_language_sub = the_book_language_sub.group(1)
                    the_book_producer_sub = re.search(data_producer_pattern, value, re.IGNORECASE)
                    the_book_producer_sub = the_book_producer_sub.group(1)
                    the_book_path = re.search(data_path_pattern, value, re.IGNORECASE)
                    the_book_path = the_book_path.group(1)
                    
                    # store the found patterns into object named book_object 
                    BookOperation.book_object = Book(BookOperation.book_title_list[line], the_book_author_sub, the_book_release_date_sub, the_book_last_update_sub, the_book_language_sub, the_book_producer_sub, the_book_path)
                    # store the found patterns into book_info_dict dictionary with book title as key, and book object as value
                    BookOperation.book_info_dict.update({BookOperation.book_title_list[line]:BookOperation.book_object})
            return True, f">>>>>>>>>> Load Book Info Success...!" # print Load Book Info Success if no error found
        except FileNotFoundError:
            return False, f">>>>>>>>>> Load Book Info Failed: File Not Found!" # print File Not Found if FileNotFoundError is found
        except RuntimeError:
            return False, f">>>>>>>>>> Load Book Info Failed: Runtime Error!" # print Runtime Error if RuntimeError is found
        
    def get_counts(book_title) -> str:
        """
        This function has one positional argument named book_title.
        Return the number of chapters, words, and lines for the specified book_title.
        Requires one argument which is book_title.
        Returns a tuple of total_chapters, total_lines, total_words.
        """
        
        total_chapters = 0
        total_lines = 0
        total_words = 0
        chosen_book_path = BookOperation.book_initial_folder + BookOperation.book_info_dict[book_title].book_path # search the book using the path stored in book object
        with open (chosen_book_path, encoding="utf8") as chosen_book: # open the book that has been chosen by the user
            chosen_book_read = chosen_book.read()
        book_read = re.search(BookOperation.start_end_pattern, chosen_book_read, re.IGNORECASE and re.MULTILINE and re.DOTALL) # search the content of the book using pattern
        try:
            book_read = book_read.group(1) # capture the content of the book and store it to book_read variable
            total_lines = book_read.count("\n")  # count the lines of the book
            clean_lines = book_read.replace("-", " ") # replace the hyphen with whitespace
            # https://datagy.io/python-remove-punctuation-from-string/#:~:text=One%20of%20the%20easiest%20ways%20to%20remove%20punctuation,to%20remove%20punctuation%20from%20a%20string%20in%20Python
            clean_lines = clean_lines.translate(str.maketrans("","",string.punctuation)) # remove the punctuation
            total_words = len(clean_lines.split()) # count the words of the book

            # search the pattern of the chapter, and try to find the matched one
            chapter_search = re.findall(r'CHAPTER.*', book_read, re.IGNORECASE) 
            if chapter_search is None: # if the pattern is not found, then try to find with the other patterns
                chapter_search = re.findall(r'ACT.*', book_read, re.IGNORECASE)
                if chapter_search is None:
                    chapter_search = re.findall(r'CONTENTS.*', book_read, re.IGNORECASE)
                    if chapter_search is None:
                        chapter_search = re.findall(BookOperation.book_chapter_pattern, book_read, re.IGNORECASE and re.MULTILINE and re.DOTALL)
            total_chapters = len(chapter_search) # count the total chapter inside the book
        except AttributeError: 
            print(f">>>>>>>>>> Sorry, we can't open the book.") # if an AttributeError found, then print this line
        return (total_chapters, total_lines, total_words)
    
    def display_titles(page_number) -> int:
        """
        This function has one positional argumen named page_number.
        Display titles of the books listed in book_title_list list.
        returns book_title 
        """
        index = 0
        while True:
            output_str = f"--------------------------- List of Book Titles ---------------------------\n"
            if len(BookOperation.book_title_list) % 10: # if all the titles is remain zero when divided by 10, then the floor division of total pages will be added by 1
                total_pages = (len(BookOperation.book_title_list)//10) + 1
            else: # if the remainder is not zero, then the total pages will remain (length of the book_title_list divided by 10)
                total_pages = len(BookOperation.book_title_list)//10
            try:
                for index in range (10): # print 10 titles per page
                    index = index + ((page_number - 1)*10)
                    output_str += f"{index + 1}. {BookOperation.book_title_list[index]}\n"
            except IndexError:
                print("") # print blank line if IndexError is found
            output_str += f"\nCurrent page: {page_number}\n"
            output_str += f"Total pages: {total_pages}\n"
            output_str += f"---------------------------------- END ----------------------------------\n"
            print(output_str)
            
            #capture the input from the user to choose wether he/she wants to open next / previous / chooses a book / back to main menu
            title_opt = input(f"Input 'n' for next page, 'p' for previous page,'x' to go back to main menu,\nor input the book number if you want to select a book: ").strip()
            if title_opt.isdigit() and title_opt != "0": # if the user input is not digit and not zero, then convert it to int
                title_opt = int(title_opt)
                if title_opt <= len(BookOperation.book_title_list): # to handle if the input from user doesn't exceeds the total books available
                    book_title = BookOperation.book_title_list[title_opt - 1]
                    return book_title # return the chosen book by the user
                else:
                    print(">>>>>>>>>> Invalid input, please re-enter") # if the user inputs wrong format
            elif title_opt == "n" or title_opt == "N": # if the user wants to go to the next page
                if page_number < total_pages: # condition to handle if the last page is reached
                    page_number += 1
                else:
                    print(">>>>>>>>>> Page number cannot exceeds total pages!")
            elif title_opt == "p" or title_opt == "P": # if the user wants to go to the previous page
                if page_number > 1: # condition to handle if the first page is reached
                    page_number -= 1
                else:
                    print(">>>>>>>>>> Page number cannot be less than one!")
            elif title_opt == "x" or title_opt == "X": # back to main menu
                break
            else:
                print(">>>>>>>>>> Invalid input, please re-enter") # if the user inputs wrong format
    
    def show_book_content(book_title) -> str:
        """
        This function has one positional argument named book_title
        Display the book contents of a book for the specified book_title.
        Return the list of chapter in a book.
        """
        book_content = ""
        chosen_book_path = BookOperation.book_initial_folder + BookOperation.book_info_dict[book_title].book_path # search the book using the path stored in book object
        with open (chosen_book_path, encoding="utf8") as a_book_text: # open the book that has been chosen by the user
            whole_book_text = a_book_text.read()
        book_text = re.search(BookOperation.start_end_pattern, whole_book_text, re.IGNORECASE and re.MULTILINE and re.DOTALL) # search the content of the book using pattern

        # search the pattern of the chapter, and try to find the matched one
        try: # to handle the error
            clean_book_text = book_text.group(1) # capture the found pattern 
            chapter_search = re.findall(r'CHAPTER.*', clean_book_text, re.IGNORECASE)
            if chapter_search is None:  # if the pattern is not found, then try to find with the other patterns
                chapter_search = re.findall(r'ACT.*', clean_book_text, re.IGNORECASE)
                if chapter_search is None:
                    chapter_search = re.findall(r'CONTENTS.*', clean_book_text, re.IGNORECASE)
                    if chapter_search is None:
                        chapter_search = re.findall(BookOperation.book_chapter_pattern, clean_book_text, re.IGNORECASE and re.MULTILINE and re.DOTALL)
            num_of_chapters = len(chapter_search) # store the number of chapters found in the book
            book_content += f"Title: {book_title}\n" 
            book_content += f"Contents:\n"
            if num_of_chapters is None: # if there's no chapter found, then print No Contents
                book_content += f">>>>>>>>>> No Contents\n"
            else: # if the chapter is found, then print all the chapters of the book
                for chapter in chapter_search:
                    book_content += f"{chapter}\n"
        except RuntimeError: # handling error
            return f">>>>>>>>>> Runtime Error"
        
        return book_content # return the book_content 

        
    def show_book_text(book_title, page_number):
        """
        This function has 2 positional arguments: book_title and page_number
        Display the book text for the specified page of a book (15 lines per page).
        """
        args_tuple = tuple()
        line_counter = 0
        chosen_book_path = BookOperation.book_initial_folder + BookOperation.book_info_dict[book_title].book_path # search the book using the path stored in book object
        with open(chosen_book_path, "r", encoding="utf8") as a_book_text: # open the book that has been chosen by the user
            whole_book_text = a_book_text.read()
        search_text = re.search(BookOperation.start_end_pattern, whole_book_text, re.IGNORECASE and re.MULTILINE and re.DOTALL) # search the content of the book using pattern
        try:
            clean_text = search_text.group(1) # capture the found pattern
            book_lines  = clean_text.splitlines() # split the book per line
            if len(book_lines) % 15: # to find if the book remain is not 0 if divided by 15
                total_pages = len(book_lines) // 15 + 1 # if the remain is not 0, then the total page is floor divided by 15 and then added by 1 
            else:
                total_pages = len(book_lines) // 15 # if the remain is 0, then keep the total page as it is (equal to length of book_lines)
            try:
                while True:
                    # search the pattern of the chapter, and try to find the matched one
                    book_chapter = re.findall(r'CHAPTER.*', clean_text, re.IGNORECASE)
                    if book_chapter is None: # if the pattern is not found, then try to find with the other patterns
                        book_chapter = re.findall(r'ACT.*', clean_text, re.IGNORECASE)
                        if book_chapter is None:
                            book_chapter = re.findall(r'CONTENTS.*', clean_text, re.IGNORECASE)
                            if book_chapter is None:
                                book_chapter = re.findall(BookOperation.book_chapter_pattern, clean_text, re.IGNORECASE and re.MULTILINE and re.DOTALL)
                    if book_chapter: # if book_chapter pattern is found, then store it to variable chapter
                        chapter = book_chapter[0]
                    else:
                        chapter = "" # if book_chapter pattern is not found, then variable chapter will be empty
                    if page_number >= 1 and page_number <= total_pages: # to handle if the page_number (input by the user) is still in range of total_pages
                        print(f"\n---------------- {book_title} - {chapter} ----------------")
                        line_counter = ((page_number - 1)*15) # to count the line to be used to display the content of the book, 15 lines per page
                        try: # handle error if out of index error is found
                            for _ in range (15): # print 15 lines per page
                                print(book_lines[line_counter])
                                line_counter += 1 # increment the line_counter for the book_lines index
                        except IndexError:
                            print("") # if IndexError, print empty line 
                        print(f"----------------end page {str(page_number)} ----------------")
                        print(f"page {page_number} of {total_pages}")
                        print(f"Add New Bookmark (can handle multiple argument: 1 followed by page number i.e., 1 3 4 5)")
                        # print(f"to delete bookmark, enter: 2 3 6 (delete bookmark at row 3 and 6)")

                        #capture the input from the user to choose wether he/she wants to open next / previous / chooses a certain page number / back to main menu
                        text_opt = input("Enter 'n' for next page or 'p' for previous page or 'x' to back to main menu: ").strip()
                        try: # to handle error
                            if len(text_opt)>1:
                                args_list = text_opt.split()
                                for each in args_list:
                                    if each.isdigit():
                                        each = int(each)
                                        if each >= 1 and each <= total_pages:
                                            args_tuple = list(args_tuple)
                                            args_tuple.append(each)
                                            args_tuple = tuple(args_tuple)
                                    else:
                                        print(">>>>>>>>>> Wrong bookmark command")
                                return args_tuple
                            elif text_opt == "n" or text_opt == "N": # if the user chooses to open next page
                                if page_number >= 1 and page_number <= total_pages:    
                                    page_number += 1
                                else: # handle if the user has reached last page
                                    print(">>>>>>>>>> Page number cannot exceeds total pages")
                            elif text_opt == "p" or text_opt == "P": # if the user chooses to open previous page
                                if page_number >= 1 and page_number <= total_pages:    
                                    page_number -= 1
                                else: # handle if the user has reached first page
                                    print(">>>>>>>>>> Page number cannot be less than one")
                            elif text_opt == "x" or text_opt == "X":
                                break
                            else:
                                print(">>>>>>>>>> Invalid input. Please re-enter!") 
                        
                        # blocks to capture errors that might be found
                        except ValueError:
                            print(">>>>>>>>>> Invalid input. Please re-enter!")
                    elif page_number > total_pages:
                        print(">>>>>>>>>> Page number cannot exceeds total pages")
                        break
                    elif page_number < 1:
                        print(">>>>>>>>>> Page number cannot be less than one")
                        break
            except RuntimeError:
                print(">>>>>>>>>> Runtime Error!")
        except AttributeError:
            print(">>>>>>>>>> Sorry, we're unable to load the book :(")
    
    def get_book_by_author(author_name):
        """
        This function has one positional argument named author_name.
        Display all the book titles belonging to the specified author.
        """
        author_counter = 0
        author_search_result = ""
        for file in BookOperation.book_info_dict.keys(): # iterate for each keys from book_info_dict (book title as the key)
            the_author = BookOperation.book_info_dict[file].author # find the author from the book_object
            the_author = re.search(f"(.*{author_name}.*)", the_author, re.IGNORECASE) # search the_author name (input from user) and store it into a group
            if the_author: # if the name of the author is found, then the name of the author will be displayed
                author_counter += 1
                the_author = the_author.group(1)
                author_search_result += f"{author_counter}. Author name: {the_author}; Title: {file}\n"
        if not author_counter: # if the author name (input from user) is not found, then return Author name is not found
            author_search_result = f">>>>>>>>>> Author name is not found!\n"
        return author_search_result
    
    def get_book_release_year():
        """
        Display the total number of books for the following release year
        ●  before 1990 (year < 1990)
        ●  between 1990 and 2000 (1990 <= year <= 2000)
        ●  after 2000 (2000 < year)
        """
        cat_1990 = 0
        cat_1990_2000 = 0
        cat_2000 = 0
        output_str = ""
        for title in BookOperation.book_info_dict.keys(): # iterate for each keys from book_info_dict (book title as the key)
            release_year = re.search(r"(\d{4})", BookOperation.book_info_dict[title].release_date, re.IGNORECASE) # search the pattern of the release year
            if release_year: # if the pattern is found, then categorize it into 3 categories: before 1990, between 1990-2000, and after 2000
                try:
                    release_year = int(release_year.group(1).strip())
                    if release_year < 1990:
                        cat_1990 += 1
                    elif release_year >= 1990 and release_year <= 2000:
                        cat_1990_2000 += 1
                    elif release_year > 2000:
                        cat_2000 += 1
                except ValueError: # to handle the Value Error
                    return False
        output_str += f"----------------- Total Number of Books -----------------\n"
        output_str += f"Number of books released before 1990: {cat_1990}\n"
        output_str += f"Number of books released between 1990 and 2000 : {cat_1990_2000}\n"
        output_str += f"Number of books released after 2000: {cat_2000}\n"
        return output_str