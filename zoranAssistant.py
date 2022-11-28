import pyttsx3  #pip install pyttsx3
import speech_recognition as sr #pip install speechRecognition
import datetime
import wikipedia #pip install wikipedia
import webbrowser
import os
import smtplib

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
# print(voices[1].id)
engine.setProperty('voice', voices[1].id)


def speak(audio):
    engine.say(audio)
    engine.runAndWait()


def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        speak("Good Morning!")

    elif hour>=12 and hour<18:
        speak("Good Afternoon!")   

    else:
        speak("Good Evening!")  

    speak(" I am Zoran your personal assistant, how may I help you")

def takeCommand():
    #It takes microphone input from the user and returns string output

    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source)

    try:
        print("Recognizing...")    
        query = r.recognize_google(audio, language='en-in')
        print(f"User said: {query}\n")

    except Exception as e:
        # print(e)    
        print("Say that again please...")
        #speak("Say that again please")
        return "None"
    return query

def sendEmail(to, content):
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.login('shabbeirshaik1234@gmail.com', 'Shehzadi123$')
    server.sendmail('shabbeirshaik1234@gmail.com', to, content)
    server.close()

if __name__ == "__main__":
    wishMe()
    while True:
    # if 1:
        query = takeCommand().lower()

        # Logic for executing tasks based on query
        if 'wikipedia' in query:
            speak('Searching Wikipedia...')
            query = query.replace("wikipedia", "")
            results = wikipedia.summary(query, sentences=2)
            speak("According to Wikipedia")
            print(results)
            speak(results)

        elif 'open youtube' in query:
            speak("yes Sir opening you tube")
            webbrowser.open("https://www.youtube.com")

        elif 'open google' in query:
            webbrowser.open("https://www.google.co.in/")
            speak("what you want me to search")

        elif 'open stack overflow' in query:
            webbrowser.open("stackoverflow.com")
        elif 'open udemy' in query:
            speak("opening udemy sir")
            webbrowser.open("https://cognizant.udemy.com/organization/home/")
        elif 'open work playlist in udemy' in query:
            webbrowser.open("https://cognizant.udemy.com/course/spring-springboot-jpa-hibernate-zero-to-master/learn/lecture/30676944#overview")
            speak("opening your play list window sir")
        elif "check for social media messages" in query:
            speak("  checking for messages sir")
            webbrowser.open("https://www.linkedin.com/feed/")
            speak("Nothing much with messages sir do you want anything to open sir")



        elif 'play music' in query:
            speak("which song you want to listen sir")
            speak("opening your song sir")
            webbrowser.open("https://www.youtube.com/watch?v=_xuI60USDjw")


        elif 'the time' in query:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")    
            speak(f"Sir, the time is {strTime}")

        elif 'open vs code' in query:
            codePath = "C:\\Users\\Dell\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe"
            os.startfile(codePath)
            speak("opening your application window sir")
        elif 'boring' in query:
            speak("can i play some music sir")
        elif "open new tab" in query:
            webbrowser.open_new_tab("https://www.google.co.in/")
        elif "send message" in query:
            speak("In which social media you want to send messages")
            if "whatsapp" in query:
                webbrowser.open("https://web.whatsapp.com/")

        elif 'email to harry' in query:
            try:
                speak("What should I say?")
                content = takeCommand()
                to = "harryyourEmail@gmail.com"    
                sendEmail(to, content)
                speak("Email has been sent!")
            except Exception as e:
                print(e)
                speak("Sorry my friend harry bhai. I am not able to send this email")