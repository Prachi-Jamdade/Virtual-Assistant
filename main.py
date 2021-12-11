import speech_recognition as sr
import pyttsx3
import pyjokes
import wikipedia
import pywhatkit
import datetime

listener = sr.Recognizer()
engine = pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)  # 1 for female voice and 0 for male voice

def talk(text):
    engine.say(text)
    engine.runAndWait()

intro = "Hello! I'm your Alexa. \nI'll be doing what you tell me to do."
talk(intro)
print(intro)

def take_command():
    try:
        with sr.Microphone() as source:
            print("Listening...")
            listener.adjust_for_ambient_noise(source, duration=0.3)
            voice = listener.listen(source)
            command = listener.recognize_google(voice)
            command = command.lower()
            if 'alexa' in command:
                command = command.replace('alexa', '')
    except:
        print('Exception Occurred...')
    return command

def run_alexa():
    command = take_command()
    print(command)
    if 'hi' in command:
        talk('Hello. What can I do for you?')
    elif 'play' in command:
        song = command.replace('play', '')
        talk('Playing ' + song)
        pywhatkit.playonyt(song)  # plays on youtube
    elif 'time' in command:
        time = datetime.datetime.now().strftime('%I:%M %p')
        print('Current time is ' + time)
        talk('Current time is ' + time)
    elif 'search' in command:
        topic = command.replace('search', '')
        talk('Searching ' + topic)
        pywhatkit.search(topic)
    elif 'info' in command:
        topic = command.replace('info', '')
        talk('Searching ' + topic)
        info = pywhatkit.info(topic, lines=5)
        talk(info)
    elif 'who the heck is' in command:
        person = command.replace('who the heck is', '')
        # wikipedia.set_lang('hi')  # set language hindi
        info = wikipedia.summary(person, 2)
        print(info)
        talk(info)
    elif 'joke' in command:
        if 'tongue' in command:
            # tongue-twister joke in en-english
            joke = pyjokes.get_joke(language='en', category='neutral')
            talk(joke)
        else:
            talk(pyjokes.get_joke())
    elif 'bye' in command:
        talk('Bye...')
        return 1
    else:
        talk('Please say the command again.')

while True:
    run_alexa()
