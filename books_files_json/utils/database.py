import json
from errors import errors
"""
Concerned with storing and retrieving a book from a csv file.

format: {'title': 'title', 'read': 'read'}
"""
books_file_path = './books.json'

def find_book(title):
  books = list_all_books()
  for book in books:
    if book['title'] == title:
      return book
  raise errors.NotFoundError('Book not found')


def create_book_file():
  with open(books_file_path, 'w') as file:
    json.dump([], file)

def list_all_books():
  with open(books_file_path, 'r') as file:
    return json.load(file)


def add_book(book):
  books = list_all_books()
  books.append(book)
  _save_all_books(books)


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
    json.dump(books, file)