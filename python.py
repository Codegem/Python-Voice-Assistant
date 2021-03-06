import speech_recognition as sr
import pyttsx3
import spotify
import pywhatkit
import wikipedia
import datetime
import pyjokes
import spotify

engine = pyttsx3.init()

# voice female
voices = engine.getProperty('voices')
engine.setProperty('voices', 'english+f')
# engine.setProperty('voice', 'english')

#voice speed
rate = engine.getProperty('rate')
engine.setProperty('rate', 160)


#hello text 
engine.say('hello my name is alexa and i can help you with these commands')
engine.runAndWait()
listener = sr.Recognizer()

def talk(text):
  engine.say(text)
  engine.runAndWait()

def take_command():
  try:
    with sr.Microphone() as source:
      print('Say')
      audio = listener.listen(source)
      voice = listener.recognize_google(audio)
      voice = voice.lower()
      if 'alex' in voice:
        voice = voice.replace('alexa', '')

  except sr.UnknownValueError:
    print('sorry i did not get that')
  except sr.RequestError:
    print('Sorry speach service is down')
  return voice

def run_alexa():
  voice = take_command()
  if 'play' in voice:
    song = voice.replace('play', '')
    talk('playing' + song)
    pywhatkit.playonyt(song)
  elif 'time' in voice:
    time = datetime.datetime.now().strftime('%H:%M')
    talk('Current time is' + time)
  elif 'tell me about' in voice:
    person = voice.replace('tell me about', '')
    info = wikipedia.summary(person, 1)
    talk(info)
  elif 'tell me a joke' in voice:
    talk(pyjokes.get_joke())

while True:
  run_alexa()


