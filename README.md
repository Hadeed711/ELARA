ELARA AI
ELARA is a Python-based personal AI assistant capable of performing tasks such as fetching news, initiating WhatsApp calls, playing music, opening websites, and more. ELARA can listen to voice commands, process them, and respond appropriately. The assistant is designed to work with a range of tools, including Speech Recognition, NewsAPI, and PyWhatKit.

Features
Voice Interaction: ELARA uses Speech Recognition for capturing voice input and SAPI for generating voice responses.
News Updates: Retrieves the latest news articles based on user-defined topics.
WhatsApp Integration: Enables instant WhatsApp messaging using voice input.
Web Navigation: Opens commonly used websites (YouTube, Google, etc.) upon command.
Media Control: Plays locally stored music files.
Time Announcements: Provides the current time on request.
Sleep and Wake-Up Mode: ELARA can enter sleep mode and be reactivated by voice.
Getting Started
Prerequisites
Python 3.x: Ensure Python is installed on your system.
Libraries:
speech_recognition
win32com.client
pywhatkit
requests
datetime
json
NewsAPI: Sign up at NewsAPI and obtain an API key.
Install dependencies by running:

bash
Copy code
pip install speechrecognition pywhatkit requests pypiwin32
Hardware Requirements
Microphone for capturing voice commands.
Setup
API Key Setup:

Replace YOUR_NEWSAPI_KEY in the news() function URL with your NewsAPI key.
Voice Selection:

ELARA lists available voices during initialization. Set speaker.Voice to the preferred voice index.
Customize Paths:

Update the paths for your music file and camera shortcut to match your system's configuration.
Usage
Run the Program: Start the assistant by running the main script.

bash
Copy code
python elara.py
Available Commands:

"Wake up": Activates ELARA from sleep mode.
"Open [website]": Opens the specified website in a browser.
"Play music": Plays the music file located at the specified path.
"What’s the time": Announces the current time.
"Open camera": Opens the camera application.
"Call WhatsApp": Initiates a WhatsApp call.
"News": Provides the latest news on a specified topic.
"Sleep": Puts ELARA into sleep mode.
WhatsApp Call:

ELARA captures the phone number and message, confirms with the user, and sends the message.
Example Interactions
User: "Wake up"

ELARA: "ELARA is now awake."
User: "Open YouTube"

ELARA: "Opening YouTube, Haddeed..."
User: "News"

ELARA: "What type of news would you like to hear?"
Error Handling
Network Errors: ELARA will notify if there’s an issue connecting to external services.
Voice Recognition Errors: ELARA will ask for clarification if it cannot understand the voice input.
Future Enhancements
Expanded Commands: Adding functionalities like calendar integration or task reminders.
Customizable Wake Word: Allowing users to set a preferred wake word.
Enhanced Error Handling: Improving error detection and providing more specific feedback.
License
This project is licensed under the MIT License. See the LICENSE file for details.

Acknowledgments
NewsAPI for news data.
SpeechRecognition for voice capture.
PyWhatKit for WhatsApp messaging.
