# Q16. Library Book System

books = []

def add_book(book):
    books.append(book)

def remove_book(book):
    if book in books:
        books.remove(book)

def search_book(book):
    if book in books:
        print("Book Found")
    else:
        print("Book Not Found")

def display_books():
    print("Books:", books)

add_book("Python")
add_book("C Programming")
remove_book("Python")
search_book("C Programming")
display_books()