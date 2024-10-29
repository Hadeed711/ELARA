import speech_recognition as sr
import os
import win32com.client as spk
import webbrowser
# import openai  # only usable when you have at least 5$ other than university fee
import datetime
import pywhatkit as kit
import re
import requests
import json

speaker = spk.Dispatch("SAPI.SpVoice")
# At the beginning of your code, after initializing speaker
voices = speaker.GetVoices()  # Get all available voices
for index, voice in enumerate(voices):
    print(f"Voice {index}: {voice.GetDescription()}")  # List available voices

# Set a specific voice (replace `1` with the index of the voice you want to use)
speaker.Voice = voices[1]  # Change index to select a different voice


def say(text):
    speaker.speak(f"{text}")

def takecmd():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        r.pause_threshold = 2
        print("Listening...")
        audio = r.listen(source)
        try:
            print("Recognizing...")
            query = r.recognize_google(audio, language='en')
            print(f"User said: {query}")
            return query
        except sr.UnknownValueError:
            say("Sorry, I didn't get that.")
            return ""

def make_whatsapp_call():
    say("Please say the phone number you want to call on WhatsApp.")
    phone_number = takecmd()
    
    # Extract numbers only, ignoring any additional words
    phone_number = re.sub(r'\D', '', phone_number)
    
    # Automatically add '0' at the start if the number has only 10 digits
    if len(phone_number) == 10:
        phone_number = '0' + phone_number
    
    # Check if phone number has a valid local format of 11 digits
    if len(phone_number) != 11 or not phone_number.startswith('0'):
        say("The number seems incomplete or invalid. Please try again.")
        return
    
    # Add the country code prefix (for example, "+92" for Pakistan)
    full_phone_number = f"+92{phone_number[1:]}"  # Replace starting '0' with '+92'
    
    # Get the message from the user
    say("Please say the message you want to send.")
    message = takecmd()

    # Repeat until a clear confirmation is received
    for _ in range(3):  # Limit to 3 attempts
        say(f"You said: {message}. Should I send this message? Say 'Yes, send' or 'No, cancel'.")
        confirmation = takecmd().lower()

        if "yes" in confirmation or "send" in confirmation:
            say(f"Sending your message to {full_phone_number} on WhatsApp.")
            kit.sendwhatmsg_instantly(full_phone_number, message, 15, True, 10)
            return  # Exit after sending
        elif "no" in confirmation or "cancel" in confirmation:
            say("Message canceled.")
            return  # Exit if canceled

    say("I didn't receive a clear confirmation. Please try again.")

def news():
    say("What type of news would you like to hear?")
    news_type = takecmd()  # Capture voice input from the user
    url = f"https://newsapi.org/v2/everything?q={news_type}&from=2024-09-29&sortBy=publishedAt&language=en&apiKey=613f8f6b09104d2d8c19c792623e9ba8"
    
    try:
        r = requests.get(url)
        if r.status_code == 200:
            news = r.json()
            if "articles" in news and news["articles"]:
                say(f"Here are the latest news articles about {news_type}.")
                for article in news["articles"][:5]:  # Limit to first 5 articles for brevity
                    title = article["title"]
                    description = article["description"]
                    print(f"Title: {title}")
                    say(f"Title: {title}")
                    print(f"Description: {description}")
                    say(f"Description: {description}")
                    print("----------------------")
            else:
                say(f"Sorry, I couldn't find any news articles about {news_type}.")
        else:
            say("There was an error retrieving the news.")
            print(f"Error: {r.status_code}")
            print(r.json())  # Output API error message for debugging
    except Exception as e:
        say("An error occurred while fetching the news. Please try again later.")
        print(f"Exception: {e}")


if __name__ == '__main__':
    say("Hello, I am ELARA A I.")
    wake_up = False  # Starts in sleep mode

    while True:
        # Only listen for commands when ELARA is awake
        if wake_up:
            query = takecmd().lower()

            # Main functionality
            if query:
                # Websites opening functionality
                sites = [
                    ["youtube", "https://youtube.com"],
                    ["wikipedia", "https://wikipedia.com"],
                    ["google", "https://google.com"],
                    ["facebook", "https://facebook.com"],
                    ["instagram", "https://instagram.com"]
                ]
                
                for site in sites:
                    if f"open {site[0]}" in query:
                        say(f"Opening {site[0]}, Haddeed...")
                        webbrowser.open(site[1])
                        break  # Prevents further checking once a match is found

                # Open music
                if "open music" in query:
                    musicpath = "D:/Songs/Tourner-Dans-Le-Vide.mp3"
                    say("Playing your music.")
                    os.startfile(musicpath)

                # Announce the time
                elif "the time" in query:
                    hours = datetime.datetime.now().strftime("%H")
                    minutes = datetime.datetime.now().strftime("%M")
                    say(f"Haddeed, the time is {hours} hours and {minutes} minutes.")

                # Open camera
                elif "open camera" in query:
                    campath = "C:/Users/HP/Desktop/Camera.lnk"
                    say("Opening camera.")
                    os.startfile(campath)

                # WhatsApp call
                elif "call whatsapp" in query:
                    make_whatsapp_call()
                # Sleep command
                elif "sleep" in query:
                    wake_up = False
                    say("ELARA is now going to sleep.") 
                elif "news" in query:
                    news()
                else:
                    say("I'm sorry, I didn't understand that command.")

        # Listen for the wake-up command if ELARA is asleep
        else:
            query = takecmd().lower()
            if "wake up" in query:
                wake_up = True
                say("ELARA is now awake.")
