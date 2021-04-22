import requests
import json
import time

def speak(str):
    from win32com.client import Dispatch
    speak = Dispatch("SAPI.SpVoice")
    speak.Speak(str)

if __name__ == "__main__":
    news_url = "" #Enter api key here from https://newsapi.org
    news = requests.get(news_url).text
    parsed = json.loads(news)
    arts = (parsed["articles"])
    speak("Today's News headlines")

    for article in arts:
        time.sleep(1)
        print(article["title"])
        print(article["url"])
        speak(article["title"])
