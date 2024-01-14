import speech_recognition as sr
import pyttsx3
import pywhatkit
import pyjokes

listener = sr.Recognizer()
engine = pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)


def talk(text):
    engine.say(text)
    engine.runAndWait()


def takeCommand():
    try:
        with sr.Microphone() as source:
            print('listening.....')
            voice = listener.listen(source)
            command = listener.recognize_google(voice)
            command = command.lower()
            if 'shreya' in command:
                command = command.replace('shreya', '')
                print(command)
    except:
        pass
    return command


def run_alexa():
    command = takeCommand()
    print(command)
    if 'play' in command:
        song = command.replace('play', '')
        talk('playing song' + song)
        #print(song)
        pywhatkit.playonyt(song)
    elif 'joke' in command:
        talk(pyjokes.get_joke())
    else:
        talk('please say it again')

while True:
    run_alexa()
