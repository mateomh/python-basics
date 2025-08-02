from database_connection import DatabaseConnection
from errors import errors

books_data_file = './data.db'

def find_book(title):
  with DatabaseConnection(books_data_file) as connection:
    cursor = connection.cursor()
    book = cursor.execute("SELECT * FROM books WHERE title = ?", (title,)).fetchall()
    return book


def create_book_table():
  with DatabaseConnection(books_data_file) as connection:
    cursor = connection.cursor()
    cursor.execute("CREATE TABLE IF NOT EXISTS books(title text primary key, read boolean)")


def list_all_books():
  with DatabaseConnection(books_data_file) as connection:
    cursor = connection.cursor()
    books = cursor.execute("SELECT * FROM books").fetchall()
    books = [{'title': book[0], 'read': book[1]} for book in books]
    return books


def add_book(book):
  with DatabaseConnection(books_data_file) as connection:
    cursor = connection.cursor()
    cursor.execute("INSERT INTO books VALUES(?, ?)", (book['title'], book['read']))


def mark_book_as_read(title):
  with DatabaseConnection(books_data_file) as connection:
    cursor = connection.cursor()
    cursor.execute("UPDATE books SET read = 1 WHERE title = ?", (title, ))


def delete_book(title):
  with DatabaseConnection(books_data_file) as connection:
    cursor = connection.cursor()
    cursor.execute("DELETE FROM books WHERE title = ?", (title,))
