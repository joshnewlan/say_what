# Say What?
This script listens to meetings I'm supposed to be paying attention to and pings me on hipchat when my name is mentioned.

It sends me a transcript of what was said in the minute before my name was mentioned and some time after. 

It also plays an audio file out loud 15 seconds after my name was mentioned which is a recording of me saying, "Sorry, I didn't realize my mic was on mute there."

Uses IBM's Speech to Text Watson API for the audio-to-text. 

Currently relies on Splunk as a data store, but can be extended to use an open-source tool instead.

Relies on Uberi's SpeechRecognition PyAudio and API wrapper: https://github.com/Uberi/speech_recognition

# Usage
Start Splunk

Run say_what.py
### TODO: Improve usage
