# LibraryManagementSystem

# Steps to setup:
1. download the code and save it in a folder.
2. install all the required depencies of Python Django including REST Framework.
3. now run the server using command:
   python manage.py runserver
4. Test the Api on below endpoints

# Mentioning the main endpoints:

# User
1. users/ -> list and create user.
2. users/<int:pk> -> Get the details of user , update and delete

# Books
1. /backend/books/ -> listing and creation of books
2. /backend/books/<int:pk> -> Get the details of book , update and delete
3. /backend/books/3/borrow/ -> Borrow a book
4. /backend/books/3/submit_back/ -> Submit a bookback

