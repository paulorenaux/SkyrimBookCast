import bookScraper
import os
from selenium.webdriver.chrome.webdriver import WebDriver

def test_get_books_uesp(mocker):
  mock_get_page = mocker.patch.object(WebDriver, 'get')
  mock_webdriver_find_element = mocker.patch.object(WebDriver, 'find_element')
  # TODO: find library and method to mock (library).WebElement.find_element
  # TODO: find library and method to mock (library).WebElement.find_elements
  # TODO: find library and method to mock (library).WebElement.get_attribute

  bookScraper._get_books_uesp()

  mock_get_page.assert_called()
  mock_webdriver_find_element.assert_called()
# end test_get_books_uesp

def test_get_books_force_uesp(mocker):
  # ensure the books aren't cached
  try:
    os.remove(bookScraper.Book.book_links_file)
  except:
    pass

  mocked_get_books_uesp = mocker.patch('bookScraper._get_books_uesp')
  mocked_save_cached_books = mocker.patch('bookScraper._save_cached_books')

  bookScraper.get_books()

  mocked_get_books_uesp.assert_called_once()
  mocked_save_cached_books.assert_called_once()
# end test_get_books_force_uesp

def test_get_books_force_cache(mocker):
  books = [{'title': 't', 'file_name': 'f', 'link': 'l', 'contents': 'c'}]
  bookScraper._save_cached_books(books)
  mocked_get_cached_books = mocker.patch('bookScraper._get_cached_books')

  bookScraper.get_books()

  mocked_get_cached_books.assert_called()
# end test_get_books_force_cache

def test_get_cached_books():
  books = [{'title': 't', 'file_name': 'f', 'link': 'l', 'contents': 'c'}]
  bookScraper._save_cached_books(books)

  cache = bookScraper._get_cached_books()
  
  assert len(cache) == len(books)
  assert cache[0]['title'] == books[0]['title']
  assert cache[0]['file_name'] == books[0]['file_name']
  assert cache[0]['link'] == books[0]['link']
  assert cache[0]['contents'] == books[0]['contents']
# end get_cached_books
