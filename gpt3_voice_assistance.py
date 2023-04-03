"""
This module contains functions for interacting with the OpenAI API.
"""

import os
import openai
import speech_recognition as sr
import pyttsx3
from dotenv import load_dotenv


# Initialize speech recognition engine
r = sr.Recognizer()

# Initialize text-to-speech engine
engine = pyttsx3.init()

"""
Define the main function that listens for user input and responds accordingly
"""

def main():
    # load the env file
    load_dotenv()
    # Configure OpenAI API credentials
    openai.api_key = os.getenv('OPENAI_API_KEY')
    
    engine.say("This is luke, how may i help you right now?")
    engine.runAndWait()
 
    with sr.Microphone() as source:
        print('Listening...')
        audio = r.listen(source)
        
    try:
        query = r.recognize_google(audio)
        print(f"You said {query}")
        response = openai.Completion.create(
            model= "gpt3-turbo",
            prompt= query,
            temperature=  0.5,
            max_tokens= 60,
            n=1,
            stop=None,
            timeout=5,
        )
        
        response_text = response.choices[0].text.strip()
        
        engine.say(response_text)
        engine.runAndWait()
        
    except sr.UnknownValueError:
        print("Sorry, I didn't understand that.")
    except sr.RequestError as request_error:
        print(f"Could not request results from Google Speech Recognition service; {0}".format(request_error))
    
    if __name__ == '__main__':
        engine.say("Start by saying 'Hey Luke' or Stop the program by saying 'Bye Luke'")
        engine.runAndWait()
        
        while True:
            with sr.Microphone() as source:
                audio = r.listen(source)
                
            try:
                command = r.recognize_google(audio)
                if 'hey luke' in command:
                    while True:
                        main()
                elif 'bye luke' in command:
                    engine.say('GoodBye!')
                    engine.runAndWait()
                    break
                else:
                    engine.say("Sorry, I didn't understand that.")
                    engine.runAndWait()
            
            except sr.UnknownValueError:
                engine.say("Sorry, I didn't understand that.")
                engine.runAndWait()
            except sr.RequestError as request_error:
                print(f"Could not request results from Google Speech Recognition service; {0}".format(request_error))
