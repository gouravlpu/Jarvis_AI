import pyttsx3
engine=pyttsx3.init('sapi5')
voices=engine.getProperty('voices')
engine.setProperty('voice',voices[1].id)

import datetime
import speech_recognition as sr
import wikipedia
import webbrowser
import os
import random
import smtplib

def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def wishme():
    hour=int(datetime.datetime.now().hour)
    if(hour>=0 and hour<12):
        speak("Good Morning")
    elif(hour>=12 and hour<18):
        speak("Good Afternoon")
    else:
        speak("Good Evening")
    speak("Sir, I am Jarvis. How may I help you")
    speak("I am a new version with chatgpt you can also get answer from there")

def takeCommand():
    #It takes microphone input from the user returns string output
    r=sr.Recognizer()
    with sr.Microphone() as source:
        print("Listning....")
        r.pause_threshold=1
        audio=r.listen(source)
    try:
        print("Recognizing....")
        query=r.recognize_google(audio,language='en-in')
        print(f"User said: {query}\n")
    except Exception as e:
        print(e)  # error not print by coomenting it
        print("Say that again Please!")
        return "None"
    return query



if __name__=='__main__':
    wishme()
    while(True):
        query=takeCommand().lower()
        if 'wikipedia' in query:
            speak("Searching wikipedia...")
            query=query.replace("wikipedia","")
            results=wikipedia.summary(query,sentences=2)
            speak("According to Wikipedia...")
            print(results)
            speak(results)
        elif 'youtube' in query:
            webbrowser.open("youtube.com")
        elif 'google' in query:
            webbrowser.open("google.com")
        elif 'stack overflow' in query:
            webbrowser.open("stackoverflow.com")
        elif 'time' in query:
            srttime = datetime.datetime.now().strftime("%H:%M:%S") 
            speak(f"The time is {srttime}")
            print(f"The time is {srttime}")
        elif 'play music' in query:
            musicdir='C:\\Users\\ADMIN\\Music\\songs'
            songs=os.listdir(musicdir)
            print(songs)
            songsno=random.randint(0,1034)
            os.startfile(os.path.join(musicdir,songs[songsno]))
        elif 'vs code' in query:
            paths='C:\\Users\\ADMIN\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe'
            os.startfile(paths)
        elif 'chat gpt' in query:
            webbrowser.open("chatgpt.com")
        
        elif 'stop' in query:
            quit()





