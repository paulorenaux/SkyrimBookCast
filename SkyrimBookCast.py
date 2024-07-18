from bookScraper import scrape
from gtts import gTTS
import time
import os

books = scrape()
for book in books[0:1]:
  audio = gTTS(text = f"{book['title']} {book['contents']}", lang='en', slow=False)
  filename = f"{book['title']}.mp3"
  audio.save(filename)
  os.system(f'start {filename}')