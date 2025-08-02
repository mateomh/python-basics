from utils import database

MENU_PROMPT = """
Enter:
- 'a' to add a new book
- 'l' to list all books
- 'r' to mark a book as read
- 'd' to delete a book
- 'q' to quit

Your choice: """

def menu():
  user_input = input(MENU_PROMPT)
  while user_input != 'q':
    if user_input == 'a':
      prompt_add_book()
    elif user_input == 'l':
      list_books()
    elif user_input == 'r':
      prompt_read_book()
    elif user_input == 'd':
      prompt_delete_book()
    else:
      print('Invalid option')

    user_input = input(MENU_PROMPT)


def prompt_add_book():
  book_title = prompt_book_title()
  book_read = input('Have you read the book (y/n): ')
  database.add_book({'title': book_title, 'read': book_read == 'y'})


def prompt_read_book():
  book_title = prompt_book_title()
  database.mark_book_as_read(book_title)


def prompt_delete_book():
  book_title = prompt_book_title()
  database.delete_book(book_title)


def prompt_book_title():
  return input('Enter the book title: ')


def list_books():
  books = database.list_all_books()
  for book in books:
    print(book)

menu()