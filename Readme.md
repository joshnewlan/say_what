# Say What?
This script listens to meetings I'm supposed to be paying attention to and pings me on hipchat when my name is mentioned.

It sends me a transcript of what was said in the minute before my name was mentioned and some time after. 

It also plays an audio file out loud 15 seconds after my name was mentioned which is a recording of me saying, "Sorry, I didn't realize my mic was on mute there."

Uses IBM's Speech to Text Watson API for the audio-to-text. 

Currently relies on Splunk as a data store, but can be extended to use an open-source tool instead.

Relies on Uberi's SpeechRecognition PyAudio and API wrapper: https://github.com/Uberi/speech_recognition

## Installation (OS X)

1. [Sign up for, install, and run Splunk Enterprise](http://www.splunk.com/en_us/download-5.html)
	* This has to be enterprise; the HTTP Event Collector feature used here doesn't exist in light
2. Add your credentials to ```CREDS``` in say\_my\_name.py
3. [Add an http event collector to Splunk](http://localhost:8000/en-US/manager/launcher/http-eventcollector) and enable it in global settings (but do not enable acknowledgement)
4. [Get a hipchat API token](https://[your company].hipchat.com/account/api) and update the hipchat fields in say\_my\_name.py
	* Your hipchat user id is the second number in your hipchat jabber info
5. Update ```name``` in say\_my\_name.py unless your name is Josh
6. [Create an IBM Bluemix account](https://console.ng.bluemix.net/registration/)
7. [Add a speech-to-text plan](https://new-console.ng.bluemix.net/catalog/services/speech-to-text/)
8. Add your credentials to say\_what.py for ```IBM_USERNAME``` and ```IBM_PASSWORD```
9. [Install Homebrew](http://brew.sh/)
10. ```brew install python```
11. ```brew install portaudio```
12. ```pip install pyaudio```
13. ```pip install SpeechRecognition```
14. ```pip install requests```

## Usage

1. Start Splunk
2. Run say_what.py

### TODO: Improve usage
