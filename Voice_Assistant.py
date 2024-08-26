import speech_recognition as sr
import pyttsx3
import webbrowser
import urllib.parse
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
    command = ""
    try:
        with sr.Microphone() as source:
            print('Listening...')
            listener.adjust_for_ambient_noise(source)
            audio = listener.listen(source)
            # Recognize speech using PocketSphinx
            command = listener.recognize_sphinx(audio).lower()
    except sr.UnknownValueError:
        talk("Sorry, I didn't catch that. Please repeat.")
    except sr.RequestError:
        talk("Sorry, I am having trouble connecting to the service.")
    except Exception as e:
        talk("An error occurred. Please try again.")
        print(f"Error: {e}")
    return command

# Function to play a song on YouTube
def play_song(command):
    song = command.replace('play', '').strip()
    talk(f'Playing {song} on YouTube')
    
    # Encode the song name for URL
    query = urllib.parse.quote(song)
    
    # Construct the YouTube search URL
    url = f"https://www.youtube.com/results?search_query={query}"
    
    # Open the URL in the web browser
    webbrowser.open(url)

# Function to report the current time
def tell_time():
    time = datetime.datetime.now().strftime('%I:%M %p')
    talk(f'Current time is {time}')

# Function to search for information on Wikipedia
def who_is(command):
    person = command.replace('who is', '').strip()
    try:
        info = wikipedia.summary(person, sentences=1)
        talk(info)
    except wikipedia.exceptions.DisambiguationError as e:
        talk("There are multiple entries for this. Please be more specific.")
        print(f"DisambiguationError: {e}")
    except wikipedia.exceptions.PageError:
        talk("Sorry, I couldn't find information on that person.")
    except Exception as e:
        talk("Sorry, something went wrong while fetching information.")
        print(f"Error: {e}")

# Function to tell a joke
def tell_joke():
    joke = pyjokes.get_joke()
    talk(joke)

# Function to search the web
def search_web(command):
    query = command.replace('search', '').strip()
    talk(f'Searching for {query}')
    webbrowser.open(f"https://www.google.com/search?q={urllib.parse.quote(query)}")

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
    talk("Goodbye! See you next time.")
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
    talk("Hello! I'm Buddy. How can I assist you today?")
    while True:
        run_buddy()

