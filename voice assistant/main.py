import speech_recognition as sr
import webbrowser
import time
import pyttsx3

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[2].id)
r = sr.Recognizer()


def record_audio():
    with sr.Microphone() as source:  # we are using microphone as our source
        audio = r.listen(source)  # we are recording what we will say in the microphone in the audio variable
        voice_data = ''
        try:
            voice_data = r.recognize_google(audio)  # this will understand our voice
        except sr.UnknownValueError:  # this is error is when he can't understand what we said
            bitSpeak("Sorry, did not get that")
        except sr.RequestError:
            bitSpeak("Sorry, my speech servers are down")
        return voice_data


def respond(voice_data):
    if 'wake up' in voice_data:
        print(voice_data)
        bitSpeak('Here you go sir i\'m on')
        print('Here you go sir i\'m on')
    elif 'what is your name' in voice_data:
        print(voice_data)
        bitSpeak("My name is rocky")
        print("My name is rocky")
    elif 'what time is it' in voice_data:
        print(voice_data)
        bitSpeak(time.ctime())
        print(time.ctime())
    elif 'go to my college site' in voice_data:
        print(voice_data)
        bitSpeak('Ok sir as you wish')
        print('Ok sir as you wish')
        webbrowser.get().open('https://www.fermimn.edu.it/')
    elif 'search' in voice_data:
        print(voice_data)
        bitSpeak("what should i search for")
        print("what should i search for")
        item = record_audio()
        print(item)
        url = 'http://google.com/search?q=' + item
        webbrowser.get().open(url)
        bitSpeak("Here is what i found for " + item)
        print("Here is what i found for " + item)
    elif 'location' in voice_data:
        print(voice_data)
        bitSpeak("which place do you what to see?")
        print("which place do you what to see?")
        location = record_audio()
        print(location)
        url = 'http://google.it/maps/place/' + location + '/&amp'
        webbrowser.get().open(url)
        bitSpeak("Here you go, this is what i found this for " + location)
        print("Here you go, this is what i found this for " + location)
    elif 'play music' in voice_data:
        print(voice_data)
        bitSpeak('Here you go!')
        print('Here you go!')
        webbrowser.get().open('https://www.youtube.com/watch?v=HBOSxNEtBPc')
#   elif 'connect to the call' in voice_data:
#        bitSpeak("which call do you want to connect")
#        print("which call do you want to connect")
#        voice_data = record_audio()
#        if 'lunedi prima ora' in voice_data:
#            bitSpeak("ok sir i'm connecting")
#            print("ok sir i'm connecting")
    elif 'go to sleep' in voice_data:
        print(voice_data)
        bitSpeak("As you wish sir")
        print("As you wish sir")
        exit()
    elif '' in voice_data:
        print('say something')
    else:
        print(voice_data)
        bitSpeak("I didn't pick up the command")
        print("I didn't pick up the command")


def bitSpeak(audio):
    engine.say(audio)
    engine.runAndWait()


time.sleep(1)
while 1:
    voice_data = record_audio()
    respond(voice_data)
