"""
Method for recognising speech. Basically asking for user confirmation.
"""
# pylint: disable=trailing-whitespace

import speech_recognition as sr
import pyttsx3

r = sr.Recognizer()

engine = pyttsx3.init()

def recognize_speech(retry_count = 3):
    """
    Method starts here
    """
    engine.say(f"You have {retry_count} retries left.")
    engine.runAndWait()
    # Using microphone to listen to user input
    with sr.Microphone() as source:
        audio = r.listen(source)
        
    try:
        query = r.recognize_google(audio)
        engine.say(f"You've said {query}? Is that correct?")
        engine.runAndWait()
        
        with sr.Microphone() as source:
            confirmation_audio = r.listen(source)
        
        try:
            confirmation_query = r.recognize_google(confirmation_audio)
            if "yes" in confirmation_query:
                return query
            
            engine.say('Please say your query again.')
            engine.runAndWait()
            
            if retry_count > 1:
                return recognize_speech(retry_count=retry_count-1)
            
            engine.say("Sorry, you've used up all your retries.")
            engine.runAndWait()
            return None
        
        except sr.UnknownValueError:
            engine.say("Sorry, I didn't understand that.")
            engine.runAndWait()
        
        except sr.RequestError as request_error:
            engine.say(f"Could not request results from Google Speech Recognition service; {0}"
                .format(request_error))
            engine.runAndWait()
            
    except sr.UnknownValueError:
        engine.say("Sorry, I didn't understand that.")
        engine.runAndWait()
        
    except sr.RequestError as request_error:
        engine.say(f"Could not request results from Google Speech Recognition service; {0}"
                   .format(request_error))
        engine.runAndWait()

        