import speech_recognition as sr
import pyttsx3
import pywhatkit
import datetime
import wikipedia
import pyjokes
import os
import sys

# Initialize the speech engine and set the voice properties
listener = sr.Recognizer()
engine = pyttsx3.init(driverName='sapi5')  # Use 'sapi5' for Windows
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)  # Set to male voice

# Function to make the assistant speak
def talk(text):
    engine.say(text)
    engine.runAndWait()

# Function to take and process the voice command
def take_command():
    try:
        with sr.Microphone() as source:
            print('Listening...')
            listener.adjust_for_ambient_noise(source)
            audio = listener.listen(source)
            command = listener.recognize_google(audio).lower()
            if 'buddy' in command:
                command = command.replace('buddy', '').strip()
                print(command)
                return command
    except sr.UnknownValueError:
        talk("Sorry, I didn't catch that. Please repeat.")
    except sr.RequestError:
        talk("Sorry, I am having trouble connecting to the service.")
    return ""

# Function to play a song on YouTube
def play_song(command):
    song = command.replace('play', '').strip()
    talk(f'Playing {song}')
    pywhatkit.playonyt(song)

# Function to report the current time
def tell_time():
    time = datetime.datetime.now().strftime('%I:%M %p')
    talk(f'Current time is {time}')

# Function to search for information on Wikipedia
def who_is(command):
    person = command.replace('who is', '').strip()
    info = wikipedia.summary(person, sentences=1)
    talk(info)

# Function to tell a joke
def tell_joke():
    joke = pyjokes.get_joke()
    talk(joke)

# Function to search the web
def search_web(command):
    query = command.replace('search', '').strip()
    talk(f'Searching for {query}')
    pywhatkit.search(query)

# Function to open applications
def open_app(command):
    app = command.replace('open', '').strip()
    talk(f'Opening {app}')
    os.system(f'start {app}')

# Function to handle shutdown
def shutdown_system():
    talk('Shutting down the system')
    os.system('shutdown /s /t 1')

# Function to handle restart
def restart_system():
    talk('Restarting the system')
    os.system('shutdown /r /t 1')

# Function to stop the assistant
def stop_assistant():
    talk("Goodbye!")
    sys.exit()

# Main function to run the assistant
def run_buddy():
    command = take_command()
    if not command:
        return

    if 'play' in command:
        play_song(command)
    elif 'time' in command:
        tell_time()
    elif 'who is' in command:
        who_is(command)
    elif 'joke' in command:
        tell_joke()
    elif 'search' in command:
        search_web(command)
    elif 'open' in command:
        open_app(command)
    elif 'shutdown' in command:
        shutdown_system()
    elif 'restart' in command:
        restart_system()
    elif 'stop' in command:
        stop_assistant()
    else:
        talk("I'm not sure what you mean. Could you please repeat?")

# Keep the assistant running in a loop
if __name__ == '__main__':
    while True:
        run_buddy()
