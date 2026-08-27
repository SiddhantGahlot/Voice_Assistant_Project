# 🎙️ Buddy – Your Personal Voice Assistant
Buddy is a Python-based voice assistant that can play music, tell jokes, fetch information from Wikipedia, open apps, search the web, and even manage system commands like shutdown or restart.

## 🚀 Features
- **🎵 Play songs on YouTube**
- **⏰ Tell the current time**
- **📚 Fetch quick info from Wikipedia**
- **😂 Tell jokes with PyJokes**
- **🌐 Search Google by voice**
- **💻 Open applications (customizable)**
- **🔒 Shutdown or restart your PC (with confirmation)**
- **👋 Smart greetings (Good morning/afternoon/evening)**
  
## 🛠️ Requirements

Make sure you have Python 3.8+ installed.
Install dependencies using pip:
```
   pip install SpeechRecognition pyttsx3 wikipedia pyjokes pyaudio
```

### ⚠️ PyAudio note (Windows users):
If installation fails, download the matching .whl file from here **https://www.lfd.uci.edu/~gohlke/pythonlibs/#pyaudio** 
 and install it with:
 ```
pip install path_to_downloaded_file.whl
```

## 📂 Project Structure
```
voice-assistant/
│── voice_assistant.py   # Main script
│── LICENSE     
│── README.md            # Project documentation
```

## ▶️ How to Run
1. **Open the project folder in VS Code (or terminal).**
2. **Run the script:**
```
python voice_assistant.py
```
3. **Speak into your microphone when Buddy says "Listening...".**

## 🎤 Example Commands
- **"What’s the time?" → Buddy tells current time**
- **"Play Shape of You" → Opens YouTube with the song**
- **"Who is Albert Einstein" → Fetches quick info from Wikipedia**
- **"Tell me a joke" → Random joke**
- **"Search Python tutorials" → Opens Google search**
- **"Open Chrome" → Launches Chrome (if path added)**
- **"Shutdown" → Shuts down system (after confirmation)**
- **"Stop" → Exits Buddy**

## ⚡Customization
**You can add more applications to the apps dictionary inside voice_assistant.py:**
```
apps = {
    "chrome": "C:\\Program Files\\Google\\Chrome\\Application\\chrome.exe",
    "vscode": "C:\\Users\\YOUR_USERNAME\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe",
    "notepad": "notepad.exe"
}
```

## 📌 Future Improvements
- **🎶 Spotify/YouTube API integration for direct playback**
- **📅 Calendar and reminders**
- **📧 Email/SMS support**
- **🌍 Weather updates**
- **📞 Call Support**

## 👨‍💻 Author
**Siddhant Kumar**
- **Email:- sg9407176@gmail.com**
- **LinkedIn:- https://linkdin.com/in/siddhant-gahlot-b91929308**
