import pyttsx3 as p
import randfacts
import speech_recognition as sp
import newsapi
import selinum
import youtube
import ss
from datetime import datetime

engine = p.init()
rate = engine.getProperty('rate')
engine.setProperty('rate',120)
voices = engine.getProperty('voices')
engine.setProperty("voice",voices[1].id)
def speak (text):
      engine.say(text)
      engine.runAndWait()
r=sp.Recognizer()

speak("hello sir ! this is your voice Assistant, How are U")

with sp.Microphone() as source:
    r.energy_threshold = 10000
    r.adjust_for_ambient_noise(source,1.2)
    print("listing.....")
    audio = r.listen(source)
    text = r.recognize_google(audio)
    print(text)
if "i am good " or "i am fine" in text:
    speak("What can i do for u ?")

with sp.Microphone() as source:
    r.energy_threshold = 10000
    r.adjust_for_ambient_noise(source,1.2)
    print("listing.....")
    audio = r.listen(source)
    text2 = r.recognize_google(audio)
    print(text2)
if "information " in text2:
    speak("you need information realted to which topic sir")
    with sp.Microphone() as source:
        r.energy_threshold = 10000
        r.adjust_for_ambient_noise(source, 1.2)
        print("listing.....")
        audio = r.listen(source)
        infor = r.recognize_google(audio)
    if __name__ == "__main__":
        search_term =infor
        print("opening {} on Wikipedia".format(infor))
        speak("opening {} on Wikipedia".format(infor))
        searcher = selinum.WikipediaSearcher(search_term)
        searcher.search()
elif "play" and "video" in text2:
    speak("which video you want to play")

    with sp.Microphone() as source:
        r.energy_threshold = 10000
        r.adjust_for_ambient_noise(source, 1.2)
        print("listing.....")
        audio = r.listen(source)
        song = r.recognize_google(audio)
        print("playing {} on youtube".format(song))
        speak("playing {} on youtube".format(song))
    if __name__ == "__main__":
        search_term1 = song
        searcher = youtube.you_tube(search_term1)
        searcher.search_you()
elif "headlines" in text2:
    speak("searching latest Headlines for you")
    if __name__ == "__main__":
        api_key = ss.key  # Replace with your actual NewsAPI key

        news_reader = newsapi.NewsAPIReader(api_key)
        headlines = news_reader.headq()
        print(headlines)

        if headlines:
            newsapi.read_out_headlines(headlines)
            news_reader.display_headlines_in_browser(headlines)
        else:
            speak("No headlines to display.")
elif "fact" in text2:
    speak("reading random fact for You")
    x = randfacts.get_fact()
    print(x)
    speak(x)
elif "time" in text2:
    current_date_time = datetime.now()
    formatted_date_time = current_date_time.strftime("%H:%M:%S")
    print(f"Current  Time: {formatted_date_time}")
    speak(f"Current  Time: {formatted_date_time}")
elif "date" in text2:
    current_date_time = datetime.now()
    formatted_date_time = current_date_time.strftime("%Y-%m-%d ")
    print(f"Current Date : {formatted_date_time}")
    speak(f"Current Date : {formatted_date_time}")
elif "quit" in text2:
    quit()
else:
    speak("i cant understand,can you please say again")
    with sp.Microphone() as source:
        r.energy_threshold = 10000
        r.adjust_for_ambient_noise(source, 1.2)
        print("listing.....")
        audio = r.listen(source)
        text2 = r.recognize_google(audio)
        print(text2)