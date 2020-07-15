import subprocess
from gtts import gTTS

mytext = "Book a Villa in New York"

language = 'en'

myobj = gTTS(text=mytext, lang=language)

myobj.save("Welcome.mp3")

subprocess.call(['mpg321', "Welcome.mp3", '--play-and_exit'])