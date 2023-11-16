import tkinter
from tkinter import *
from tkinter import messagebox
from PIL import Image
import tkinter as tk
import pyttsx3
import PyPDF2
import datetime
import speech_recognition as sr
import pyaudio
import wikipedia
import pyjokes
import webbrowser
from tkinter.filedialog import *
import subprocess
import pywhatkit

def ask_here():
    def takeCommand():
        r = sr.Recognizer()
    
        with sr.Microphone() as source:
            print('Listening')
        
            r.pause_threshold = 0.8
            audio = r.listen(source)
	 
            try:
                print('Recognizing')
                Query = r.recognize_google(audio)
                print("the command is ", Query)
	    
            except Exception as e:
                print(e)
                print("I am sorry couldn't perform the task you specified")
                return "None"
	
            return Query

    def speak(audio):
        engine = pyttsx3.init()
        voices = engine.getProperty('voices')
        engine.setProperty('voice', voices[1].id)
        engine.say(audio)
        engine.runAndWait()

    def tellDay():
        day = datetime.datetime.today().weekday() + 1
        Day_dict = {1: 'Monday', 2: 'Tuesday',
				3: 'Wednesday', 4: 'Thursday',
				5: 'Friday', 6: 'Saturday',
				7: 'Sunday'}
        if day in Day_dict.keys():
            day_of_the_week = Day_dict[day]
            print(day_of_the_week)
            speak("The day is " + day_of_the_week)

    def tellTime():
        time = str(datetime.datetime.now())
        print(time)
        hour = time[11:13]
        min = time[14:16]
        speak("The time is sir" + hour + "Hours and" + min + "Minutes")

    def Hello():
        speak(" Tell me how may I help you ")

    def Take_query():
        Hello()
        while(True):
            query = takeCommand().lower()
            if "youtube" in query:
                query = query.replace("from youtube search", "")
                youtube = query
                speak('playing ' + query)
                webbrowser.open("https://www.youtube.com/results?search_query=" + youtube + "")
                break
            elif "google" in query:
                query = query.replace("from google search", "")
                search = query
                speak('searching ' + query)
                webbrowser.open("https://www.google.dz/search?q=" + search + "")
                break
            elif "day" in query:
                tellDay()
                break
            elif "time"in query:
                tellTime()
                break
            elif "from wikipedia search" in query:
                speak("Checking the wikipedia ")
                query = query.replace("wikipedia search", "")
                result = wikipedia.summary(query, sentences=4)
                speak("According to wikipedia")
                speak(result)
                break
            elif "tell me your name" in query:
                speak("I am Della. Your deskstop Assistant")
                break
            elif "joke" in query:
                speak(pyjokes.get_joke())
                break
            elif "write a note" in query:
                speak("What should i write")
                note = takeCommand()
                file = open('della.txt', 'w')
                speak("Should i include time")
                snfm = takeCommand()
                if 'yes' in snfm or 'sure' in snfm:
                    strTime = datetime.datetime.now().strftime("%H:%M:%S")
                    file.write(strTime)
                    file.write(" :- ")
                    file.write(note)
                else:
                    file.write(note)
                break    
            elif "weather" in query:
                query = query.replace("weather of", "")
                weather = query
                speak('weather of' + query)
                webbrowser.open("https://www.msn.com//en-in//weather//today//" + weather + "")
                break
            elif 'news' in query:
                speak("Here are some headlines from the Times of India,Happy reading")
                webbrowser.open("https://timesofindia.indiatimes.com//home//headlines")
                break
            elif "log off" in query or "sign out" in query:
                speak("Ok , your pc will log off in 10 sec make sure you exit from all applications")
                subprocess.call(["shutdown", "/l"])
                break
            elif 'play' in query:
                query = query.replace('play', '')
                speak('playing ' + query)
                pywhatkit.playonyt(query)
                break
            elif "where is" in query:
                query = query.replace("where is", "")
                location = query
                speak("User asked to Locate")
                speak(location)
                webbrowser.open("https://www.google.com/maps/place/" + location + "")
                break
            elif "tell me what can you do" in query or "what can you do" in query:
                speak("I can do lots of things, for example you can ask me time, date, weather in your city,place, news headlines .I can open websites for you, log off, tell a joke, create a note and much more .")
                break
            elif 'exit' in query or "bye" in query:
                speak("Thanks for giving me your time")
                exit()
            else:
                speak("I am sorry couldn't perform the task you specified")
                break
                 
                
    if __name__ == '__main__':
        Take_query()
        

def open_file():
    browse_text.set("loading...")
    listener = sr.Recognizer()
    engine = pyttsx3.init()
    voices = engine.getProperty('voices')
    engine.setProperty('voice', voices[1].id)
    book = askopenfilename()
    pdfreader = PyPDF2.PdfFileReader(book)
    pages = pdfreader.numPages

    for num in range(0, pages):
        page = pdfreader.getPage(num)
        text = page.extractText()
        player = pyttsx3.init()
        player.say(text)
        player.runAndWait()

root = tkinter.Tk()
root.title("DELLA")
root.geometry("750x700")
root.config(background="#f3e9fc")
root.resizable(0, 0)

img1 = PhotoImage(file="final.png")

labelimage = Label(root, image = img1, background ="#f3e9fc")
labelimage.pack()

labeltext = Label(root, text = "Della - A Virtual Assistant", fg="#ba81ee" ,font = ("times",20,"italic bold"), background = "#f3e9fc")
labeltext.pack()

listen_text = tk.StringVar()       
listen_btn = tk.Button(root, textvariable=listen_text, font = ("times",10,"italic bold"), bg="#ba81ee", fg="white", height=2, width=15, command=lambda:ask_here())
listen_text.set("Ask a Query")
listen_btn.pack(pady=10)

browse_text = tk.StringVar()       
browse_btn = tk.Button(root, textvariable=browse_text, command=lambda:open_file(), font = ("times",10,"italic bold"), bg="#ba81ee", fg="white",height=2, width=15)
browse_text.set("Browse a PDF")
browse_btn.pack(pady=10)

btn1 = Button(root, text = 'Quit!', command = root.destroy,font = ("times",10,"italic bold"), bg="#ba81ee", fg="white", height=2, width=15)
btn1.pack(pady=10)

root.mainloop()
