"""
ASSIGNMENT 3 - ITI9136 - INTRODUCTION TO PYTHON
Name                    : Fajar Witama Wijaya
Student ID              : 33452784
Creation Date           : November 15th, 2022
Last Modified Date      : November 27th, 2022
"""
class Book:
    def __init__(self, title = "", author = "", release_date = "", last_update_date = "", language = "", producer = "", book_path = ""):
        self.title = title
        self.author = author
        self.release_date = release_date
        self.last_update_date = last_update_date
        self.language = language
        self.producer = producer
        self.book_path = book_path

    def __str__(self):
        string = f"{self.title};;;{self.author};;;{self.release_date};;;{self.last_update_date};;;{self.language};;;{self.producer};;;{self.book_path}"
        return string
