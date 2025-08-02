from errors import errors

books_file_path = './books.txt'

"""
Concerned with storing and retrieving a book from a csv file.

format: name,read\n
"""

def find_book(title):
  books = list_all_books()
  for book in books:
    if book['title'] == title:
      return book
  raise errors.NotFoundError('Book not found')


def create_book_file():
  with open(books_file_path, 'w') as file:
    pass

def list_all_books():
  try:
    with open(books_file_path, 'r') as file:
      lines = [line.strip().split(',') for line in file.readlines()]
    # lines = [[title, read], [title, read]]
    books = [
      {'title': line[0], 'read': line[1]}
      for line in lines
    ]

    return books
  except FileNotFoundError:
    create_book_file()


def add_book(book):
  with open(books_file_path, 'a') as file:
    file.write(f"{book['title']},{book['read']}\n")


def mark_book_as_read(title):
  books = list_all_books()
  for book in books:
    if book['title'] == title:
      book['read'] = True
  _save_all_books(books)


def delete_book(title):
  books = list_all_books()
  new_books = [ book for book in books if book['title'] != title ]
  _save_all_books(new_books)


def _save_all_books(books):
  """
  This is a private function, it is supose to be used only inside the module
  """
  with open(books_file_path, 'w') as file:
    for book in books:
      file.write(f"{book['title']},{book['read']}\n")