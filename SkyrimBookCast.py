from bookScraper import scrape, Book
from gtts import gTTS
import os

def find_file(name: str, path: str) -> list:
  result = []
  for root, dir, files in os.walk(path):
    if name in files:
      result.append(os.path.join(root, name))
  return result

def book_to_audio(book: Book) -> None:
  contents = f"{book['title']} {book['contents']}"
  filename = f"{book['filename']}.mp3"
  files = find_file(filename, './')
  if len(files) == 0:
    audio = gTTS(contents, lang='en', slow=False)
    audio.save(filename)
  return filename

books = scrape()
for book in books[1:2]:
  audio_filename = book_to_audio(book)
  os.system(f"start {audio_filename}")