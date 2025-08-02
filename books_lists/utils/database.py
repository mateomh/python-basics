from errors import errors

books = []


def find_book(title):
  for book in books:
    if book['title'] == title:
      return book
  raise errors.NotFoundError('Book not found')


def list_all_books():
  return books


def add_book(book):
  books.append(book)


def delete_book(title):
  # book = find_book(title)
  # books.remove(book)
  global books # uses the variable of the global scope instead of creating a local books variable
  books = [ book for book in books if book['title'] != title ]


def mark_book_as_read(title):
  for book in books:
    if book['title'] == title:
      book['read'] = True