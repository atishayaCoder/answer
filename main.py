import speech_recognition as SpeechRecognition
import pyttsx3 

import wolframalpha as wolf
client = wolf.Client("2JP2VJ-87AX6AL666")

recogniser = SpeechRecognition.Recognizer()

import sys

engine = pyttsx3.init()

voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)

rate = engine.getProperty('rate')
engine.setProperty('rate',0)

engine.say('started')
engine.runAndWait()

while True:
    try:
        with SpeechRecognition.Microphone() as mic:
            recogniser.adjust_for_ambient_noise(mic, duration=0.2)
            audio = recogniser.listen(mic)

            text = recogniser.recognize_google(audio)
            text = text.lower()

            engine.say(f'I heard: {text}')
            engine.runAndWait()
        
            if text == 'stop': engine.say('stopping') and sys.exit()
            if text == 'you are stupid': engine.say('no you are stupid')

            try:
                query = str(text)
                result =  client.query(query)
                output = next(result.results).text

                engine.say(output)
                engine.runAndWait()

            except:
                engine.say('sorry didnt quite catch you')

            
    except SpeechRecognition.UnknownValueError:
        recogniser = SpeechRecognition.Recognizer()
        continue

