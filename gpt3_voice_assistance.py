"""
This module contains functions for interacting with the OpenAI API.
"""
# pylint: disable=trailing-whitespace


import os
import openai
import speech_recognition as sr
import pyttsx3
from dotenv import load_dotenv


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
    engine.say("This is luke, how may i help you right now?")
    engine.runAndWait()
    
    # Use Microphone to pick up speech
    with sr.Microphone() as source:
        print('Listening...')
        audio = r.listen(source)
        
    # Try method
    try:
        query = r.recognize_google(audio)
        print(f"You said {query}")
        if 'send email' in query:
            pass
        elif 'open website' in query:
            pass
        elif 'search internet' in query:
            pass
        elif 'tell joke' in query:
            pass
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
            engine.say(response_text)
            engine.runAndWait()
            
    #   First except error method
    except sr.UnknownValueError:
        print("Sorry, I didn't understand that.")
        
    # Second except error method
    except sr.RequestError as request_error:
        print(f"Could not request results from Google Speech Recognition service; {0}"
              .format(request_error))

    # Program starts here
    if __name__ == '__main__':
        engine.say("Start by saying 'Hey Luke' or Stop the program by saying 'Bye Luke'")
        engine.runAndWait()
        
        # Start audio recording using microphone
        while True:
            with sr.Microphone() as source:
                audio = r.listen(source)
                
            # Try method
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
                    
            # First except error method
            except sr.UnknownValueError:
                engine.say("Sorry, I didn't understand that.")
                engine.runAndWait()
                
            # Second except error method
            except sr.RequestError as request_error:
                print(f"Could not request results from Google Speech Recognition service; {0}"
                      .format(request_error))
