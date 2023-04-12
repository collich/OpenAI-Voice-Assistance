"""
Method for recognising speech. Basically asking for user confirmation.
"""
# pylint: disable=trailing-whitespace

import speech_recognition as sr
import pyttsx3

r = sr.Recognizer()

engine = pyttsx3.init()

def record_audio():
    """
    Record audio using microphone
    """
    with sr.Microphone() as source:
        print('Listening...')
        audio = r.listen(source, timeout=5)
        return audio

def recognize_speech(retry_count = 4):
    """
    Method starts here
    """
    
    # Conditional to check retry counter
    if retry_count is not 4:
        print(f"You have {retry_count} retries left.")
        engine.say(f"You have {retry_count} retries left.")
        engine.runAndWait()
    # Using microphone to listen to user input
    audio = record_audio()
        
    try:
        query = r.recognize_google(audio)
        print(f"You've said {query}? Is that correct? Please answer yes or no")
        engine.say(f"You've said {query}? Is that correct? Please answer yes or no")
        engine.runAndWait()
        
        confirmation_audio = record_audio()
        
        try:
            confirmation_query = r.recognize_google(confirmation_audio)
            if "yes" in confirmation_query:
                print(confirmation_query)
                return query
            
            if retry_count > 1:
                print('Please say your query again.')
                engine.say('Please say your query again.')
                engine.runAndWait()
                return recognize_speech(retry_count=retry_count-1)
            
            print("Sorry, you've used up all your retries.")
            engine.say("Sorry, you've used up all your retries.")
            engine.runAndWait()
            return None
        
        except sr.UnknownValueError:
            print("Sorry, I didn't understand that.")
            engine.say("Sorry, I didn't understand that.")
            engine.runAndWait()
        
        except sr.RequestError as request_error:
            print(f"Could not request results from Google Speech Recognition service; {0}"
                .format(request_error))
            engine.say(f"Could not request results from Google Speech Recognition service; {0}"
                .format(request_error))
            engine.runAndWait()
            
    except sr.UnknownValueError:
        print("Sorry, I didn't understand that.")
        engine.say("Sorry, I didn't understand that.")
        engine.runAndWait()
        
    except sr.RequestError as request_error:
        print(f"Could not request results from Google Speech Recognition service; {0}"
                   .format(request_error))
        engine.say(f"Could not request results from Google Speech Recognition service; {0}"
                   .format(request_error))
        engine.runAndWait()

        