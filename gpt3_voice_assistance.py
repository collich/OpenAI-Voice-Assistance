"""
This module contains functions for interacting with the OpenAI API.
"""
# pylint: disable=trailing-whitespace


import os
import sys
import openai
import speech_recognition as sr
import pyttsx3
from dotenv import load_dotenv
from helpers import send_email, open_website, search_internet, tell_joke
from recognize_speech import record_audio, recognize_speech

# Initialize speech recognition engine
r = sr.Recognizer()

# Initialize text-to-speech engine
engine = pyttsx3.init()

def main():
    """
    Listens for user input and responds accordingly.
    
    Recognizes user speech using the microphone as input,
    queries the OpenAI API to generate a response,
    and uses text-to-speech to output the response.
    
    If the response contains a command, it executes the corresponding task,
    (e.g. send email, open website, search internet, tell joke).
    """
    # load the env file
    load_dotenv()
    
    # Configure OpenAI API credentials
    openai.api_key = os.getenv('OPENAI_API_KEY')
    
    # TTS will start kicking in
    print("This is Vocalis, how may i help you right now? Send email, Open Website, Search Internet or ChatGPT? Say now.")
    engine.say("This is Vocalis, how may i help you right now? Send email, Open Website, Search Internet or ChatGPT? Say now.")
    engine.runAndWait()
    
    # Use Microphone to pick up speech
    main_audio = record_audio()
        
    # Try method
    try:
        query = r.recognize_google(main_audio)
        print(f"You said {query}")
        if 'goodbye' in query:
            print('Goodbye!')
            engine.say('Goodbye!')
            engine.runAndWait()
            sys.exit()
            
        elif 'send email' in query:
            send_email()
            
        elif 'open website' in query:
            print('Okay, so what site do you want me to search?')
            engine.say('Okay, so what site do you want me to search?')
            engine.runAndWait()
            site = recognize_speech()
            if site is not None:
                open_website(site)
                
        elif 'search internet' in query:
            print('What are you looking for? Please tell me in terms of search terms.')
            engine.say('What are you looking for? Please tell me in terms of search terms.')
            engine.runAndWait()
            search_term = recognize_speech()
            if search_term is not None:
                search_internet(search_term)
            
        elif 'tell joke' in query:
            tell_joke()
            
        else:
            response = openai.Completion.create(
                model= "gpt3-turbo",
                prompt= query,
                temperature=  0.5,
                max_tokens= 60,
                n=1,
                stop=None,
                timeout=5,
            )
            
            # Send response and close in on message
            response_text = response.choices[0].text.strip()
            
            # TTS will start
            print(response_text)
            engine.say(response_text)
            engine.runAndWait()
            
    #   First except error method
    except sr.UnknownValueError:
        print("Sorry, I didn't understand that.")
        engine.say("Sorry, I didn't understand that.")
        engine.runAndWait()
        
    # Second except error method
    except sr.RequestError as r_error:
        print(f"Could not request results from Google Speech Recognition service; {0}"
              .format(r_error))
        engine.say(f"Could not request results from Google Speech Recognition service; {0}"
              .format(r_error))
        engine.runAndWait()

    # Program starts here
if __name__ == '__main__':
    print("Start by saying 'Hello Vocalis' or Stop the program by saying 'GoodBye Vocalis'")
    engine.say("Start by saying 'Hello Vocalis' or Stop the program by saying 'GoodBye Vocalis'")
    engine.runAndWait()
        
        # Start audio recording using microphone
    while True:
        audio = record_audio()
                
            # Try method
        try:
            command = r.recognize_google(audio)
            if 'hello' in command:
                while True:
                    main()
            elif 'goodbye' in command:
                engine.say('GoodBye!')
                engine.runAndWait()
                break
            else:
                print("Sorry, I didn't understand that.")
                engine.say("Sorry, I didn't understand that.")
                engine.runAndWait()
                    
            # First except error method
        except sr.UnknownValueError:
            print("Sorry, I didn't understand that.")
            engine.say("Sorry, I didn't understand that.")
            engine.runAndWait()
                
            # Second except error method
        except sr.RequestError as request_error:
            print(f"Could not request results from Google Speech Recognition service; {0}"
                .format(request_error))
            engine.say(f"Could not request results from Google Speech Recognition service; {0}"
                .format(request_error))
            engine.runAndWait()
