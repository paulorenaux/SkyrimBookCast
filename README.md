# Skyrim Book Cast

Scrapes Books from Skyrim into texts, then converts the texts to audio.

# Usage

After installing python, run `python SkyrimBookCast.py`.

# Testing

## Execute tests
To re-run book scraper tests, run `pytest bookScraperTest.py`.

## Test coverage
To re-calculate code coverage, run `coverage run .\bookScraper.py`

For a better presentation of the coverage output, run `coverage html`

### Testing `_get_books_uesp`
To test this method, it is verified that the scraping methods are called and the output.
_To ensure the scraping methods are called, concepts of mocking are used._