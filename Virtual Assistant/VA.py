# text to speech library
import pyttsx3
# library convert audio into text
import speech_recognition as sr
# library to display Web-based documents to users
import webbrowser
# library to fetch current date and time
import datetime
import calendar
# library to fetch wikipedia information
import wikipedia
# library to play youtube video and perform google search
import pywhatkit
# library that is used to create one-line jokes
import pyjokes


# method to accept and recognize commands given by the user
def acceptCommands():
    # create speech_recognition
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print('Listening')
        r.pause_threshold = 0.8
        audio = r.listen(source)
        try:
            print("Recognizing")
            Query = r.recognize_google(audio, language='en-in')
            # print("the command is printed=", Query)
        except Exception as e:
            print(e)
            return "None"

        return Query


def speak(audio):
    engine = pyttsx3.init()
    voices = engine.getProperty('voices')
    engine.setProperty('voice', voices[0].id)
    engine.say(audio)
    engine.runAndWait()


def tellDay():
    day = datetime.date.today()
    speak(calendar.day_name[day.weekday()])
    '''Day_dict = {1: 'Monday', 2: 'Tuesday',
                3: 'Wednesday', 4: 'Thursday',
                5: 'Friday', 6: 'Saturday',
                7: 'Sunday'}

    if day in Day_dict.keys():
        day_of_the_week = Day_dict[day]
        print(day_of_the_week)
        speak("The day is " + day_of_the_week)'''


def tellTime():
    current_time = datetime.datetime.now().strftime("%I:%M %p")
    output = "Your current local time is " + current_time
    speak(output)
    '''time = str(datetime.datetime.now())
    print(time)
    hour = time[11:13]
    min = time[14:16]
    speak("The time is sir" + hour + "Hours and" + min + "Minutes")'''


def welcome():
    speak('Hello!!! I am Finxter - your desktop assistant.')


def Take_query():
    welcome()
    while (True):
        query = acceptCommands().lower()
        if "open youtube" in query:
            speak("Opening youtube ")
            webbrowser.open("www.youtube.com")
            continue

        elif "open browser" in query:
            speak("Opening Google Chrome ")
            webbrowser.open("www.google.com")
            continue

        elif "what day is it" in query:
            tellDay()
            continue

        elif "tell me the time" in query:
            tellTime()
            continue

        elif "goodbye" in query:
            speak("Good Bye Master!")
            exit()

        elif "from wikipedia" in query:
            speak("Checking the wikipedia ")
            query = query.replace("wikipedia", "")
            result = wikipedia.summary(query, sentences=4)
            speak("According to wikipedia")
            speak(result)

        elif "your name" in query:
            speak("I am Finxter. Your Virtual Assistant!")
            continue

        elif 'search web' in query:
            pywhatkit.search(query)
            speak("Searching Result in Google!")
            continue

        elif 'play' in query:
            speak('playing ' + query)
            pywhatkit.playonyt(query)
            continue

        elif 'joke' in query:
            speak(pyjokes.get_joke())
            continue


if __name__ == '__main__':
    Take_query()
