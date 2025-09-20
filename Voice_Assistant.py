import speech_recognition as sr
import pyttsx3
import webbrowser
import urllib.parse
import datetime
import wikipedia
import pyjokes
import os
import sys
import subprocess

# Initialize the speech engine
listener = sr.Recognizer()
engine = pyttsx3.init(driverName='sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)  # You can change index for male/female voice

# Dictionary of apps (add more if needed)
apps = {
    "chrome": "C:\\Program Files\\Google\\Chrome\\Application\\chrome.exe",
    "vscode": "C:\\Users\\SiddhantKumar\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe",
    "notepad": "notepad.exe"
}

# Speak function
def talk(text):
    print(f"Buddy: {text}")  # For debugging
    engine.say(text)
    engine.runAndWait()

# Listen for command
def take_command():
    try:
        with sr.Microphone() as source:
            print("Listening...")
            listener.adjust_for_ambient_noise(source)
            audio = listener.listen(source)

            command = listener.recognize_google(audio).lower()
            print(f"You said: {command}")
            return command
    except sr.UnknownValueError:
        talk("Sorry, I didn’t catch that. Please repeat.")
    except sr.RequestError:
        talk("Sorry, I am having trouble connecting to the service.")
    except Exception as e:
        talk("An error occurred. Please try again.")
        print(f"Error: {e}")
    return ""

# Play a song on YouTube
def play_song(command):
    song = command.replace('play', '').strip()
    talk(f'Playing {song} on YouTube')
    query = urllib.parse.quote(song)
    url = f"https://www.youtube.com/results?search_query={query}"
    webbrowser.open(url)

# Tell time
def tell_time():
    time = datetime.datetime.now().strftime('%I:%M %p')
    talk(f'The current time is {time}')

# Wikipedia search
def who_is(command):
    person = command.replace('who is', '').strip()
    try:
        info = wikipedia.summary(person, sentences=1)
        talk(info)
    except wikipedia.exceptions.DisambiguationError:
        talk("There are multiple entries. Please be more specific.")
    except wikipedia.exceptions.PageError:
        talk("Sorry, I couldn’t find information on that person.")
    except Exception:
        talk("Sorry, something went wrong while fetching information.")

# Tell joke
def tell_joke():
    joke = pyjokes.get_joke()
    talk(joke)

# Google search
def search_web(command):
    query = command.replace('search', '').replace('google', '').strip()
    talk(f'Searching for {query}')
    webbrowser.open(f"https://www.google.com/search?q={urllib.parse.quote(query)}")

# Open apps
def open_app(command):
    app = command.replace('open', '').strip()
    if app in apps:
        talk(f"Opening {app}")
        subprocess.Popen(apps[app])
    else:
        talk("Sorry, I don’t know how to open that application.")

# Shutdown confirmation
def shutdown_system():
    talk('Are you sure you want to shutdown? Say yes or no.')
    confirm = take_command()
    if 'yes' in confirm:
        talk('Shutting down the system')
        os.system('shutdown /s /t 1')
    else:
        talk('Cancelled shutdown')

# Restart confirmation
def restart_system():
    talk('Are you sure you want to restart? Say yes or no.')
    confirm = take_command()
    if 'yes' in confirm:
        talk('Restarting the system')
        os.system('shutdown /r /t 1')
    else:
        talk('Cancelled restart')

# Stop assistant
def stop_assistant():
    talk("Goodbye! See you next time.")
    sys.exit()

# Run assistant
def run_buddy():
    command = take_command()
    if not command:
        return

    if 'play' in command:
        play_song(command)
    elif 'time' in command or "what's the time" in command:
        tell_time()
    elif 'who is' in command:
        who_is(command)
    elif 'joke' in command:
        tell_joke()
    elif 'search' in command or 'google' in command:
        search_web(command)
    elif 'open' in command:
        open_app(command)
    elif 'shutdown' in command:
        shutdown_system()
    elif 'restart' in command:
        restart_system()
    elif 'stop' in command or 'exit' in command or 'quit' in command:
        stop_assistant()
    else:
        talk("I’m not sure what you mean. Could you repeat?")

# Main loop
if __name__ == '__main__':
    hour = datetime.datetime.now().hour
    if hour < 12:
        greet = "Good morning"
    elif hour < 18:
        greet = "Good afternoon"
    else:
        greet = "Good evening"

    talk(f"{greet}! I'm Buddy. How can I assist you today?")
    while True:
        run_buddy()
