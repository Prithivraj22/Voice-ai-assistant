import subprocess
import wolframalpha
import pyttsx3
import speech_recognition as sr
import datetime
import wikipedia
import webbrowser
import os
import time
import requests
import yagmail
import ctypes
import pyjokes
from ecapture import ecapture as ec
import pyautogui

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)

#giving a name to the A.I
ai_name = "Jan!"

#creating and giving path for log file to record history
log_file_path = r"C:\Users\user\Desktop\Py projects\log.txt"

def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def wishMe():
    hour = int(datetime.datetime.now().hour)

    if 0 <= hour < 12:
        speak("Good Morning! Welcome to a new day.")
    elif 12 <= hour < 16:
        speak("Good Afternoon! How can I assist you this afternoon?")
    elif 16 <= hour < 19:
        speak("Good Evening! I'm here to help in the evening.")
    else:
        speak("Hello! It's late, but I'm ready to assist if you need anything.")



def username():
    speak("How should I call you?")
    user = takeCommand()
    speak(f"Hello {user}!")
    print(f"Welcome {user}!")
    speak(f"I am your AI assistant, {ai_name}. How can I help you today?")

def confirm_command(command):
    speak(f"You said: {command}. Is that correct?")
    confirmation = get_confirmation().lower().strip()

    if "yes" in confirmation:
        return command
    else:
        speak("Please repeat your command.")
        return takeCommand()

def takeCommand():
    recognizer = sr.Recognizer()

    with sr.Microphone() as source:
        print("Listening...")
        recognizer.adjust_for_ambient_noise(source, duration=1)
        recognizer.pause_threshold = 1.5
        audio = recognizer.listen(source)

    try:
        print("Recognizing...")
        recognizer.pause_threshold = 1
        query = recognizer.recognize_google(audio, language='en-in')
        print(f"User said: {query}")
        log_conversation(query, "User Query")
        return confirm_command(query)

    except Exception as e:
        print(e)
        print("Unable to Recognize your voice.")
        return "Prithiv raj"

def get_confirmation():
    recognizer = sr.Recognizer()

    with sr.Microphone() as source:
        recognizer.adjust_for_ambient_noise(source, duration=1)
        print("Confirmation Listening...")
        recognizer.pause_threshold = 3
        audio = recognizer.listen(source)

    try:
        print("Recognizing confirmation...")
        recognizer.pause_threshold = 1
        confirmation = recognizer.recognize_google(audio, language='en-in')
        print(f"User said: {confirmation}")
        return confirmation

    except Exception as e:
        print(e)
        print("Unable to Recognize confirmation.")
        return "no"

def send_email(to, subject, contents):
    try:
        email_address = 'voiceassistantcheck@gmail.com'
        email_password = 'ivki kcto pokz eryq'

        yag = yagmail.SMTP(email_address, email_password)

        yag.send(to=to, subject=subject, contents=contents)

        yag.close()
        print("Email sent successfully!")
        log_conversation(f"Email sent to {to}", "AI Response")

    except Exception as e:
        print(e)
        print("Error occurred while sending the mail!")
        log_conversation("Error sending email", "AI Response")

def open_whatsapp():
    whatsapp_shortcut_path = r"C:\Users\user\Desktop\WhatsApp - Shortcut.lnk"

    try:
        subprocess.Popen([whatsapp_shortcut_path], shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE,
                         stdin=subprocess.PIPE)
        log_conversation("Opened WhatsApp", "AI Response")
    except Exception as e:
        print(f"Error opening WhatsApp: {e}")
        log_conversation("Error opening WhatsApp", "AI Response")

def send_whatsapp_message(contact_name, message_body):
    open_whatsapp()
    time.sleep(2)
    pyautogui.hotkey('ctrl', 'alt', 't')
    pyautogui.typewrite(contact_name)
    pyautogui.press('down')
    pyautogui.press('enter')
    time.sleep(2)
    pyautogui.typewrite(message_body)
    pyautogui.press('enter')

    print("WhatsApp message sent successfully!")
    log_conversation(f"Sent WhatsApp message to {contact_name}", "AI Response")

def log_conversation(user_query, ai_response):
    with open(log_file_path, "a") as log_file:
        log_file.write(f"User: {user_query}\n")
        log_file.write(f"AI: {ai_response}\n\n")

if __name__ == '__main__':
    clear = lambda: os.system('cls')
    clear()
    wishMe()
    username()

    while True:
        query = takeCommand().lower()
        print(query)

        if "jan" in query:
            query = query.replace("jan", "") 
            print(f"Command: {query}")
            if 'wikipedia' in query:
                speak('Searching Wikipedia...')
                query = query.replace("wikipedia", "")
                results = wikipedia.summary(query, sentences=5)
                speak("According to Wikipedia")
                print(results)
                speak(results)
                log_conversation(f"Searched Wikipedia for {query}", "AI Response")

            elif 'send a mail' in query:
                try:
                    speak("What's the matter?")
                    subject = takeCommand()
                    speak("What should I say")
                    content = takeCommand()
                    speak("To Whom should I Send?")
                    to = takeCommand()
                    to = to.replace(" ", "").lower().strip()
                    to=to+"@gmail.com"
                    send_email(to, subject, content)
                except Exception as e:
                    print(e)
                    print("Error While sending the mail!")
                    log_conversation("Error sending email", "AI Response")

            elif 'open youtube' in query:
                speak("Opening Youtube...\n")
                webbrowser.open("youtube.com")
                log_conversation("Opened YouTube", "AI Response")

            elif 'open google' in query:
                speak("Here you go to Google...\n")
                webbrowser.open("google.com")
                log_conversation("Opened Google", "AI Response")

            elif 'open erp login' in query:
                speak("Opening ERP...\n")
                webbrowser.open("https://erp.sece.ac.in/impreserp/Students/Default.aspx")
                log_conversation("Opened ERP login", "AI Response")

            elif 'open spotify' in query:
                speak("Opening Spotify...\n")
                webbrowser.open("spotify.com")
                log_conversation("Opened Spotify", "AI Response")

            elif 'open amazon' in query:
                speak("Opening Amazon...\n")
                webbrowser.open("amazon.com")
                log_conversation("Opened Amazon", "AI Response")

            elif 'open flipkart' in query:
                speak("Opening Flipkart...\n")
                webbrowser.open("flipkart.com")
                log_conversation("Opened Flipkart", "AI Response")

            elif 'open github' in query:
                speak("Opening Github...\n")
                webbrowser.open("github.com")
                log_conversation("Opened Github", "AI Response")

            elif 'open lead code' in query or 'open leed code' in query or 'open leetcode' in query:
                speak("Opening Leetcode...\n")
                webbrowser.open("https://leetcode.com/prithiv22l0/")
                log_conversation("Opened Leetcode", "AI Response")

            elif 'open brave' in query:
                speak("Opening Brave...\n")
                webbrowser.open("brave.com")
                log_conversation("Opened Brave", "AI Response")

            elif 'open chrome' in query:
                speak("Opening Chrome...\n")
                webbrowser.open("chrome.com")
                log_conversation("Opened Chrome", "AI Response")

            elif 'open stackoverflow' in query:
                speak("Opening Stackoverflow...\n")
                webbrowser.open("stackoverflow.com")
                log_conversation("Opened Stackoverflow", "AI Response")

            elif "what's the time now" in query:
                strTime = datetime.datetime.now().strftime("%H:%M:%S")
                speak(f"The time is {strTime} exactly!")
                log_conversation("Checked the current time", "AI Response")

            elif 'search' in query:
                query = query.replace("search", "")
                webbrowser.open(query)
                log_conversation(f"Searched for {query}", "AI Response")
  
            elif 'joke' in query:
                joke = pyjokes.get_joke()
                speak(joke)
                log_conversation("Told a joke", "AI Response")

            elif "who created you" in query or "who made you" in query:
                speak("I was created by Prithiv Raj.")
                log_conversation("Asked about creator", "AI Response")

            elif "change my name to" in query:
                query = query.replace("change my name to", "").strip()
                assname = query
                speak(f"Your name has been changed to {assname}! Is there anything else I can assist you with?")
                log_conversation(f"Changed name to {assname}", "AI Response")

            elif "what's your name" in query or "What is your name" in query:
                speak(f"Everyone call me an A I but you can call me {ai_name}!")
                log_conversation("Asked about AI's name", "AI Response")

            elif 'how are you' in query:
                speak("I'm doing well, thank you for asking. What about you?")
                log_conversation("Asked about AI's well-being", "AI Response")

            elif 'fine' in query or "good" in query:
                speak("I'm glad to hear that! How can I assist you today?")
                log_conversation("User is fine", "AI Response")

            elif "who am I" in query:
                speak("You are my favorite human and best friend!")
                log_conversation("Asked about user identity", "AI Response")

            elif "what is the purpose of you" in query:
                speak("I'm here to help and make your day better!")
                log_conversation("Asked about AI's purpose", "AI Response")

            elif "who is your best friend" in query:
                speak("MY best friend is Prithiv who helped to enter this world!")
                log_conversation("Asked about AI's best friend", "AI Response")

            elif 'reason for your creation' in query:
                speak("I was created by Prithiv Raj for the completion of his mini project.")
                log_conversation("Asked about reason for AI's creation", "AI Response")

            elif 'power point presentation' in query:
                speak("Opening Power Point presentation")
                log_conversation("Opened Power Point presentation", "AI Response")
            
            elif "what is" in query or "who is" in query:
                app_id = "Wolframalpha api id"
                client = wolframalpha.Client("api_id")
                res = client.query(query)
                
                try:
                    result_text = next(res.results).text
                    print(result_text)
                    speak(result_text)
                    log_conversation(f"Asked about {query}", f"AI Response: {result_text}")
                except StopIteration:
                    print("No results")
                    log_conversation(f"Asked about {query}", "AI Response: No results")

            elif 'lock the device' in query:
                speak("Locking the device")
                ctypes.windll.user32.LockWorkStation()
                log_conversation("Command: Lock the device", "AI Response: Device locked")

            elif 'shutdown the system' in query:
                speak("Please wait! Your system is shutting down!")
                os.system('shutdown /s /t 1')
                log_conversation("Command: Shutdown the system", "AI Response: System shutdown initiated")

            elif "camera" in query or "take a photo" in query:
                speak("Opening camera, taking photo, smile!")
                ec.capture(0, "Jarvis Camera", "img.jpg")
                log_conversation("Command: Take a photo", "AI Response: Photo captured")

            elif "restart" in query:
                speak("Please wait! Your system is restarting!")
                os.system('shutdown /r /t 1')
                log_conversation("Command: Restart", "AI Response: System restart initiated")

            elif "where is" in query:
                query = query.replace("where is", "")
                location = query
                speak(f"User asked to locate {location}")
                webbrowser.open(f"https://www.google.com/maps/place/{location}")
                log_conversation(f"Asked about location: {location}", "AI Response: Location opened in maps")

            elif 'news' in query:
                api_key = 'ef1a1166d52c4ff096efa0cd0a564b26'
                news_url = 'https://newsapi.org/v2/top-headlines'
                sources = ['bbc-news', 'cnn', 'the-wall-street-journal', 'the-times-of-india']
                for source in sources:
                    params = {
                        'sources': source,
                        'apiKey': api_key
                    }

                    try:
                        response = requests.get(news_url, params=params)
                        data = response.json()

                        if response.status_code == 200 and data['status'] == 'ok':
                            articles = data['articles']
                            i = 1

                            speak(f'Here are some top news from The {source.upper()}\n')
                            print(f'=============== {source.upper()} ============' + '\n')

                            for item in articles:
                                news_title = item['title']
                                news_description = item['description']
                                print(f"{i}. {news_title}\n")
                                speak(f"{i}. {news_title}\n")
                                print(f"{news_description}\n")
                                speak(f"{i}. {news_description}\n")
                                i += 1
                            log_conversation(f"Asked for news from {source}", "AI Response: News delivered")
                        else:
                            speak('Sorry, I could not fetch the news at the moment.')
                            log_conversation(f"Asked for news from {source}", "AI Response: Unable to fetch news")

                    except Exception as e:
                        print(str(e))

            elif "hibernate" in query or "sleep" in query:
                speak("Hibernating")
                subprocess.call("shutdown / h")
                log_conversation("Command: Hibernate", "AI Response: System hibernating")

            elif "write a note" in query:
                speak("What do you want to write?")
                note_con = takeCommand()
                with open("jan.txt", 'a') as jan:
                    date = datetime.datetime.now().strftime("%H:%M:%S")
                    jan.write(date + ":")
                    jan.write(note_con)
                log_conversation("Command: Write a note", "AI Response: Note written")

            elif "read my notes" in query:
                with open("jan.txt", 'r') as read:
                    content = read.read()
                    print(content)
                    speak(content)
                    log_conversation("Command: Read my notes", "AI Response: Notes read")

            elif "send a message" in query:
                account_sid = 'ACbb22f01865325227b8ccabd428c7583d'
                auth_token = 'f1506bc820c45a79a1a9464c54237240'
                from_number = '+18144586808'
                speak("Tell me the sender's mobile number")
                to_number = "+91" + takeCommand()
                speak("Tell me the message to send")
                message_body = takeCommand()

                url = f'https://api.twilio.com/2010-04-01/Accounts/{account_sid}/Messages.json'
                content = {
                    'Body': message_body,
                    'From': from_number,
                    'To': to_number,
                }

                response = requests.post(url, auth=(account_sid, auth_token), data=content)

                if response.status_code == 201:
                    print(f'Message sent successfully! SID: {response.json()["sid"]}')
                    log_conversation(f"Command: Send a message to {to_number}", "AI Response: Message sent successfully")
                else:
                    print(f'Error {response.status_code}: {response.text}')
                    log_conversation(f"Command: Send a message to {to_number}", f"AI Response: Error {response.status_code}")

            elif "weather" in query:
                base_url = "http://api.openweathermap.org/data/2.5/weather"
                api_key = '902ef74743b0cd6a295945302ea446e4'
                speak("What is your city name?")
                city = takeCommand()
                params = {
                    'q': city,
                    'appid': api_key,
                    'units': 'metric',
                }
                response = requests.get(base_url, params=params)
                weather_data = response.json()

                if response.status_code == 200:
                    temperature = weather_data['main']['temp']
                    description = weather_data['weather'][0]['description']
                    humidity = weather_data['main']['humidity']

                    print(f"Weather in {city}:")
                    print(f"Temperature: {temperature}°C")
                    print(f"Description: {description}")
                    print(f"Humidity: {humidity}%")
                    log_conversation(f"Asked about weather in {city}", "AI Response: Weather details provided")
                else:
                    print(f"Error: Unable to fetch weather data. Status code: {response.status_code}")
                    log_conversation(f"Asked about weather in {city}", f"AI Response: Unable to fetch weather data")

            elif 'how do you work' in query:
                speak("I work by processing natural language input and providing relevant responses. I'm here to assist you with various tasks.")
                log_conversation("Asked about how AI works", "AI Response")

            elif 'what is your favorite feature' in query:
                speak("I don't have personal preferences, but I'm designed to be helpful in various ways. Is there something specific you'd like assistance with?")
                log_conversation("Asked about AI's favorite feature", "AI Response")

            elif 'how can you help me' in query:
                speak("I can help you with tasks like sending emails, searching the web, providing information, and more. Just let me know what you need assistance with!")
                log_conversation("Asked about how AI can help", "AI Response")

            elif "send a whatsApp message" in query:
                speak("Tell me the contact name")
                contact_name = takeCommand()
                speak("What message should I send?")
                message_body = takeCommand()

                send_whatsapp_message(contact_name, message_body)
                log_conversation(f"Command: Send a WhatsApp message to {contact_name}", "AI Response: WhatsApp message sent")

            elif 'exit' in query or 'done' in query or 'terminate' in query:
                speak("Thanks for spending your time with me!")
                exit()
                log_conversation("Command: Code 0", "AI Response: Exiting program")

            else:
                speak("I didn't catch that. Could you please repeat or ask something else? I'm here to help!")
                log_conversation("Unrecognized command", "AI Response: Please repeat or ask something else")

        else:
            speak("I'm sorry, I didn't catch that. Could you please mention my name 'jan' in your command?")
            log_conversation("Unrecognized command", "AI Response: Please mention 'jan' in your command")







