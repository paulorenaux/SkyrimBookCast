from selenium import webdriver
from selenium.webdriver.common.by import By
from jsonFile import serialize, parse
import re

# File where link to each book is cached
_book_links_file = 'book_links.json'

def _get_cached_books() -> dict: return parse(_book_links_file)
def _save_cached_books(books: dict): serialize(books, _book_links_file)
def _clean_file_name (file_name: str) -> str: return re.sub('[ ,:.]', '_', file_name)

def _get_books_uesp () -> list:
  """ Retrieving link to books from UESP, should return 533 links. """
  url = 'https://en.uesp.net/wiki/Skyrim:Books'
  driver = webdriver.Chrome()
  driver.get(url)

  table = driver.find_element(By.ID, 'collapsibleTable0')
  rows = table.find_elements(By.TAG_NAME, 'tr')

  books = []
  for row in rows:
    td = row.find_elements(By.TAG_NAME, 'td')

    if (len(td) == 0):
      continue

    anchor = td[1].find_element(By.TAG_NAME, 'a')
    book = {
      'title': anchor.get_attribute('title'),
      'filename': _clean_file_name(anchor.get_attribute('title')),
      'link': anchor.get_attribute('href')
    }
    
    books.append(book)
    
  return books
# end get_books

def _get_books () -> dict:
  """if book title and url list is cached, retrieve from cache; retrieve from uesp otherwise."""
  books = _get_cached_books()
  if (books == None):
    books = _get_books_uesp(True)
    _save_cached_books(books)
  return books

def _get_book_contents_uesp(url):
  """Get book contents for each link."""
  """TODO: first letter in first paragraph is not a text, but an image"""
  driver = webdriver.Chrome()
  driver.get(url)
  book_contents = driver.find_element(By.CLASS_NAME, 'book')
  return book_contents.text
# end get_book_contents

def scrape():
  books =_get_books()
  for book in books[0:5]:
    if ('contents' not in book):
      book['contents'] = _get_book_contents_uesp(book['link'])
  _save_cached_books(books)
  return books