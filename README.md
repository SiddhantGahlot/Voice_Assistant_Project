**🗣️ Custom Voice Assistant - Buddy**

**🚀 Project Overview**

Buddy is a Python-based Voice Assistant designed to automate and simplify daily tasks using voice commands. The assistant can play music from YouTube, provide the current time, search the web, tell jokes, and manage system functions like opening applications or shutting down the computer.

**✨ Features**
- **(a)** Voice Recognition: Utilizes the PocketSphinx (CMU Sphinx) library to capture and interpret voice commands.
- **(b)** Text-to-Speech: Uses the pyttsx3 library to convert text responses into speech, with a male voice configuration.
- **(c)** YouTube Integration: Opens YouTube search results for requested songs or videos.
- **(d)** Time Announcement: Provides the current time in a human-readable format.
- **(e)** Wikipedia Search: Fetches and reads out summaries for "Who is" queries.
- **(f)** Joke Telling: Delivers a random joke using the pyjokes library.
- **(g)** Web Search: Automates web searches and provides instant results.
- **(h)** System Control: Capable of opening applications, restarting, or shutting down the system via voice commands.

**🛠️ Technologies Used**
- **(a) Python: The core programming language for developing the assistant.
- **(b)** PocketSphinx: For capturing and recognizing voice input.
- **(c)** pyttsx3: For converting text to speech.
- **(d)** webbrowser: For integrating YouTube and web search functionalities.
- **(e)** Wikipedia API: For fetching information from Wikipedia.
- **(f)** pyjokes: For generating and reading out random jokes.
- **(g)** OS Module: For executing system-level commands like opening applications or shutting down the computer.

**📂 Project Structure**
   
    ├── voice_assistant.py    # Main Python script for the voice assistant
    └── README.md             # Project documentation

**🚀 How to Run the Project**

**1.Clone the Repository:-**
   
    git clone https://github.com/SiddhantGahlot/Voice_Assistant_Project.git
    cd Voice_Assistant_Project

**2.Install the Required Libraries:-**

Create a requirements.txt file with the following content:

`SpeechRecognition`, `pyttsx3`, `webbrowser`, `wikipedia`, `pyjokes`

Then install the libraries:
  
    pip install -r requirements.txt

**3.Run the Voice Assistant:-**
    
    python voice_assistant.py

**4.Use Voice Commands:-**
- **(a)** Say "Play [song name]" to open YouTube search results for a song.
- **(b)** Ask "What is the time?" to get the current time.
- **(c)** Say "Who is [person's name]?" to get a brief summary from Wikipedia.
- **(d)** Use "Tell me a joke" to hear a random joke.
- **(e)** Try "Search [query]" to perform a web search.
- **(f)** Say "Open [application name]" to open a program.
- **(g)** Use "Shutdown" or "Restart" to control the system.

**📝 Contribution Guidelines**

Feel free to fork this repository, make changes, and submit a pull request. Any contributions are greatly appreciated!

**📧 Contact**

If you have any questions or suggestions, feel free to reach out:
- **Email:** sg9407176@gmail.com or gahlotsiddhant03@gmail.com
- **LinkedIn:** https://linkedin.com/in/siddhant-gahlot-b91929308

**📜 License**

This project is licensed under the MIT License - see the LICENSE file for details.
