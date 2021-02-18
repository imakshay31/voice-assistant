import speech_recognition as sr
from time import ctime
import time
import webbrowser as wb
import pyttsx3
import pyjokes
import cv2
import os
import requests as req
import datetime
from newsapi import NewsApiClient


engine = pyttsx3.init()
r = sr.Recognizer()

def record_audio():
    with sr.Microphone() as source:
        audio = r.listen(source)
        try:
            voice_data = r.recognize_google(audio)
            print(voice_data)
        except sr.UnknownValueError:
            print("Sorry I did not Understand that")
        except sr.RequestError:
            print("Sorry, cant reach servers right now")
        except:
            print("Try again")
        return voice_data


def respond(voice_data):
    if "your name" in voice_data:
        print("My name is Sushant")
        engine.say("My name is Sushant")
        engine.runAndWait()

    if "time" in voice_data:
        engine.say(ctime())
        engine.runAndWait()
    if "search" in voice_data:
        engine.say("What do you want to search for?")
        engine.runAndWait()
        google_search = record_audio()
        url = "https://google.com/search?q=" + google_search
        wb.get().open(url)
        engine.say("Here's what I found on Google for " + google_search)
        print("Here's what I found on Google for " + google_search)
        engine.runAndWait()
    if "YouTube" in voice_data:
        engine.say("What do you want to search in Youtube?")
        engine.runAndWait()
        yt_search = record_audio()
        url = "https://www.youtube.com/results?search_query=" + yt_search
        wb.get().open(url)
        engine.say("Here's what I found on YouTube.")
        engine.runAndWait()
        print("Here's what I found on YouTube.")
    if "location" in voice_data:
        engine.say("What is the location?")
        engine.runAndWait()
        location = record_audio()
        url = "https://www.google.com/maps/place/" + location + "/&amp;"
        wb.get().open(url)
        engine.say("Here's the Location")
        engine.runAndWait()
    if "weather" in voice_data:
        print("Yes please tell me city name")
        engine.say("Yes please tell me city name")
        engine.runAndWait()
        city = record_audio()
        api = "1a0ffacaf0739e625b9b4cbd7d4434a7"
        url = "https://api.openweathermap.org/data/2.5/weather?"
        answer = url + "appid=" + api + "&q=" + city
        response = req.get(answer)
        res = response.json()
        if res["cod"] != "404":
            x = res["main"]
            temprature = x["temp"]
            pressure = x["pressure"]
            humidity = x["humidity"]
            y = res["weather"]
            weather_description = y[0]["description"]
            temprature = round(temprature - 273.16, 2)
            engine.say("Following are weather description of city " + city)
            engine.runAndWait()
            print("temprature (in Celsius unit) : ", temprature)
            engine.say("temprature in Celsius unit is " + str(temprature))
            engine.runAndWait()
            print("atmospheric pressure(in hPa units): ", pressure)
            engine.say("atmospheric pressure " + str(pressure))
            engine.runAndWait()
            print(" humidity (in percentage) : ", humidity)
            engine.say("humidity percentage " + str(humidity))
            engine.runAndWait()
            print("Description: ", weather_description)
            engine.say("description" + str(weather_description))
            engine.runAndWait()
        else:
            print("Sorry I did not Understand that")
    if 'joke' in voice_data:
        engine.say(pyjokes.get_joke())
        engine.runAndWait()

    if "camera" in voice_data or "photo" in voice_data:
        cam = cv2.VideoCapture(0)

        cv2.namedWindow("test")

        img_counter = 0

        while True:
            ret, frame = cam.read()
            if not ret:
                print("failed to grab frame")
                break
            cv2.imshow("test", frame)

            k = cv2.waitKey(1)
            if k % 256 == 27:
                # ESC pressed
                print("Escape hit, closing...")
                break
            elif k % 256 == 32:
                # SPACE pressed
                img_name = "opencv_frame_{}.png".format(img_counter)
                cv2.imwrite(img_name, frame)
                print("{} written!".format(img_name))
                img_counter += 1

        cam.release()

        cv2.destroyAllWindows()

    if 'notepad' in voice_data:
        app = r"C:\WINDOWS\system32\notepad.exe"
        os.startfile(app)
    if 'zoom' in voice_data:
        app = r"C:\Users\rombo\AppData\Roaming\Zoom\bin\Zoom.exe"
        os.startfile(app)
    if 'steam' in voice_data:
        app = r"C:\Program Files (x86)\Steam\steam.exe"
        os.startfile(app)
    if "will you be my gf" in voice_data or "will you be my bf" in voice_data:
        engine.say("I'm not sure about, may be you should give me some time")
        engine.runAndWait()

    if "how are you" in voice_data:
        engine.say("I'm fine, glad you asked")
        engine.runAndWait()
    elif "i love you" in voice_data:
        engine.say("It's hard to understand")
        engine.runAndWait()

    if "note" in voice_data:
        engine.say("What should i write, sir")
        engine.runAndWait()
        note = record_audio()
        file = open('jarvis.txt', 'w')
        file.write(note)
        engine.say("Note taken")
        engine.runAndWait()


    if "show file" in voice_data:
        engine.say("Showing Notes")
        engine.runAndWait()
        file = open("jarvis.txt", "r")
        print(file.read())

    if "exit" in voice_data:
        print("Bye")
        engine.say("Bye")
        engine.runAndWait()
        exit()
    if "thank you" in voice_data:
        print("Bye")
        engine.say("Bye")
        engine.runAndWait()
        exit()

time.sleep(1)
engine.say("How can i help you?")
print("How can i help you?")
engine.runAndWait()
while 1:
    voice_data = record_audio()
    respond(voice_data)