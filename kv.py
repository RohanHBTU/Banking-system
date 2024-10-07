import pyttsx3
import engineio
import datetime
import webbrowser
import speech_recognition as sr
import wikipedia
import random
import mysql.connector
import time

engineio = pyttsx3.init('sapi5')
voices = engineio.getProperty('voices')
rate=engineio.getProperty('rate')
engineio.setProperty('rate',200)
engineio.setProperty('voice',voices[0].id)
vol=engineio.getProperty('volume')
engineio.setProperty('volume',1)
command=['hey','hello','yo']
reply=['welcome','hello',"what 's app"]
db=mysql.connector.connect(host='localhost',user='root',passwd='user')
con=db.cursor()
def speak(text):
    engineio.say(text)
    engineio.runAndWait()

def wishme():
    hour=int(datetime.datetime.now().hour)
    if hour<=0 and hour>12:
        speak("Good morning Sir")
    elif hour>=12 and hour<18:
        speak("Good afternoon  Sir")
    else:
        speak("good evening Sir")
    speak("mera nam hae jarvis")
    speak("how can i help you ")
    
def takecommand():
    r=sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold=1
        audio=r.listen(source)
    try:
        print("Recogizing...")
        query=r.recognize_google(audio,language="en-in")
        print(f"user Said {query}\n")
    except Exception as e:
        speak("Say It again please")
        return "None"
    return query
    
if __name__=="__main__":
    wishme()
    while True:
        query=takecommand().lower()
        if "wikipedia" in query.lower():
            speak("Seaching please wait")
            query=query.replace("wikipedia","")
            results=wikipedia.summary(query,sentences=2)
            speak("According to Wikipedia")
            speak(results)
        elif "open youtube" in query:
            webbrowser.open('youtube.com')
        elif "open google" in query.lower():
            webbrowser.open("google.com")
        elif "play music" in query:
            print()
        elif "current time" in query:
            speak(datetime.datetime.now())
        elif "open stackoverflow" in query:
           webbrowser.open("stackoverflow.com")
        elif "open mail" in query:
            webbrowser.open_new("gmail.com")
        elif query in command:
            w=random.randint(0,2)
            speak(reply[w])
        elif "search from database" in query:
            speak("which database sir")
            database=takecommand().lower()
            con.execute(f"use {database}")
            speak("say table name")
            table=takecommand().lower()
            try:
                con.execute(f"select * from {table}")
                re=con.fetchall()
                for c in re:
                    print(c)
            except:
                speak("table not found")
        elif "wait" in query:
            time.sleep(10)
        elif "open " in query:
            speak("which app sir")
            app=takecommand().lower()
            open(app)
            
