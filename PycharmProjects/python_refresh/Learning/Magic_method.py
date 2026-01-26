# Magic methods = Dunder methods __init__, __str__, __len__, etc.
#                 They are automatically called by many of python's built in operations
#                 They allow developers to define or customize the behavior of objects

class Book:

    def __init__(self, page, author, title):
        self.page = page
        self.author = author
        self.title = title

    

book1 = Book(300, "George", "Python Basics")
book2 = Book(150, "Alice", "Learn Java")

print(book1)  # <__main__.Book object at 0x7f8c2c4d9d60> ( This will give the memory address of the object)

# To make it more readable, we can use the __str__ magic method

class Book_with_str:

    def __init__(self, page, author, title):
        self.page = page
        self.author = author
        self.title = title

    def __str__(self):
        return f"'{self.title}' by {self.author}, {self.page} pages"
    
    # This one allows you to compare if if two books are equal based on number of pages
    def __eq__(self, other):
        return self.page == other.page
    
    # This one allows you to  compare if one book has more pages than the other
    def __gt__(self, other):  # gt = greater than
        return self.page > other.page
    
    def __lt__(self,other):   # ls  = less than
        return self.page < other.page
    
    # what if I want to add both books page together
    def __add__(self, other):
        return self.page + other.page
    
    # what if I want to find the keyword in the book

    def __contains__(self, keyword):
        return keyword in self.title or keyword in self.author
    
    def __getitem__(self, key):
        if key == 'title':
            return self.title

    
    
book_with_str1 = Book_with_str(371, "George", "Python Basics")
print(book_with_str1)  # 'Python Basics' by George, 371 pages   

book_with_str2 = Book_with_str(300, "Alice", "Learn Java")
book_with_str3 = Book_with_str(300, "Alice", "Learn Java")
print(book_with_str2 == book_with_str3)  # True because both have 300 pages

print(book_with_str1 > book_with_str2)  # True because 371 > 300
print(book_with_str1 < book_with_str2)  # False because 371 > 300

#Now we can add pages of both books
print(book_with_str1 + book_with_str2)  # 671 (371 + 300)

# Check if keyword is in the book title or author
print("Python" in book_with_str2)  # True

print(book_with_str1['title'])  # Python Basics