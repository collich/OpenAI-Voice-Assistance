"""
Method for recognising speech. Basically asking for user confirmation.
"""
# pylint: disable=trailing-whitespace

import speech_recognition as sr
import pyttsx3

r = sr.Recognizer()

engine = pyttsx3.init()

def recognize_speech():
    """
    Method starts here
    """
    
    # Using microphone to listen to user input
    with sr.Microphone() as source:
        audio = r.listen(source)
        
    try:
        query = r.recognize_google(audio)
        engine.say(f"You've said {0}?".format(query))
        engine.runAndWait()
        
        with sr.Microphone() as source:
            confirmation_audio = r.listen(source)
        
        try:
            query = r.recognize_google(confirmation_audio)
            if "yes" in query:
                return query
            
            engine.say('Please say your query again.')
            engine.runAndWait()
            return recognize_speech()
        
        except sr.UnknownValueError:
            print("Sorry, I didn't understand that.")
        
        except sr.RequestError as request_error:
            print(f"Could not request results from Google Speech Recognition service; {0}"
                .format(request_error))
            
    except sr.UnknownValueError:
        print("Sorry, I didn't understand that.")
        
    except sr.RequestError as request_error:
        print(f"Could not request results from Google Speech Recognition service; {0}"
            .format(request_error))
        