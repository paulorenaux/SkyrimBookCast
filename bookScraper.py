from selenium import webdriver
from selenium.webdriver.common.by import By
from jsonFile import serialize, parse
import re
from typing import TypedDict

class Book(TypedDict):
  book_links_file = 'book_links.json'
  max_books = 533
  """File where link to each book is cached"""
  title: str
  file_name: str
  link: str
  contents: str

def _get_cached_books() -> dict: 
  try:
    return parse(Book.book_links_file)
  except:
    return None
def _save_cached_books(books) -> None: serialize(books, Book.book_links_file)
def _clean_file_name (file_name: str) -> str: return re.sub('[ ,:.]', '_', file_name)

def _get_books_uesp (limit = 5) -> list: # pragma: no cover
  """ Retrieving link to books from UESP, should return 533 links. """
  driver = webdriver.Chrome()
  driver.get('https://en.uesp.net/wiki/Skyrim:Books')

  table = driver.find_element(By.ID, 'collapsibleTable0')
  rows = table.find_elements(By.TAG_NAME, 'tr')

  books = []
  for row in rows:
    td = row.find_elements(By.TAG_NAME, 'td')

    if (len(td) == 0):
      continue

    anchor = td[1].find_element(By.TAG_NAME, 'a')
    book: Book = {
      'title': anchor.get_attribute('title'),
      'filename': _clean_file_name(anchor.get_attribute('title')),
      'link': anchor.get_attribute('href')
    }
    books.append(book)
    
  limit = limit if limit > Book.max_books else Book.max_books
  for book in books[0:limit]:
    # TODO: first letter in first paragraph is not a text, but an image
    driver.get(book['link'])
    book['contents'] = driver.find_element(By.CLASS_NAME, 'book').text
  return books
# end get_books

def get_books() -> dict:
  books = _get_cached_books()
  if books == None:
    books = _get_books_uesp()
    _save_cached_books(books)
  return books