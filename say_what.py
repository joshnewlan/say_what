import speech_recognition as sr
import time
import json
import requests
import thread
import subprocess

SPLUNK_URL = "https://localhost"
# Splunk http event collector token
hec_token = ""

# IBM Speech to Text creds
IBM_USERNAME = ""
IBM_PASSWORD = ""

def translate(audio,r):
    # The translated output from IBM's Watson speech-to-text api
    # The r param is an instance of SpeechRecognition
    # Returns a dict because I plan on trying other speech-to-text tools

    results = {}
    text = False
    try:
        text = r.recognize_ibm(audio, username=IBM_USERNAME, password=IBM_PASSWORD)
        print("Results:" + text)
    except sr.UnknownValueError:
        # print("IBM Speech to Text could not understand audio")
        pass
    except sr.RequestError as e:
        print("Could not request results from IBM Speech to Text service; {0}".format(e))

    if text:
        results['text'] = text

    return results


def create_event(results):
    event = {
        "time": str(time.time()),
        "host": "localhost",
        "source": "say_what",
        "sourcetype": "_json",
        "index": "say_what",
        "event": {
            "minutes": results['text'],
        }
    }
    return event


def send_to_splunk(event):
    event_json = json.dumps(event)
    # Ignore ssl cert warning
    # requests.packages.urllib3.disable_warnings()
    try :
        r = requests.post("%s:8088/services/collector/event" % SPLUNK_URL,
            headers={"Authorization": "Splunk %s" % hec_token},
            data=event_json,
            verify=False)
        # print r.status_code
    except Exception, e:
        print e


def consumer(audio,r):
    # Received audio, now transcribe it and send to Splunk
    results = translate(audio,r)
    if 'text' in results:
        event = create_event(results)
        send_to_splunk(event)
    else:
        print "[--Silence--]"

    # Save audio to an AIFF file (UNFINISHED: Slow, blocking)
    # now = str(time.time())
    # with open("./audio/{}.aiff".format(now), "wb") as f:
    #     f.write(audio.get_aiff_data())


def main():
    # Spawn index/notify/play-wav script subprocess
    subprocess.Popen(['python','./say_my_name.py'])
    r = sr.Recognizer()
    while True:
        with sr.Microphone() as source:
            print("Listening...")
            audio = r.listen(source)
            thread.start_new_thread(consumer,(audio,r))

if __name__ == '__main__':
    main()
