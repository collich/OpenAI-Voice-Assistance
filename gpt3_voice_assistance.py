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
from todo_list import connect_database, create_note, index_note, delete_note, show_note

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
    
    # Connect database
    connect_database()
    
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
            # Ask for input to the receiver
            print("To whom do you want send it to? Please type it in the input.")
            engine.say("To whom do you want send it to? Please type it in the input.")
            engine.runAndWait()
            to_personel = input("To: ")
            # Ask for subject from the user
            print("What is the subject of the email?")
            engine.say("What is the subject of the email?")
            engine.runAndWait()
            email_subject = recognize_speech()
            # Ask for the body of email
            print("What is your body of the your email message?")
            engine.say("What is your body of the your email message?")
            engine.runAndWait()
            email_body = recognize_speech()
            send_email(to_personel, email_subject, email_body)
            # Confirmation from the TTS
            print(f"Done, email sent to {to_personel}")
            engine.say(f"Done, email sent to {to_personel}")
            engine.runAndWait()
            
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
            joke = tell_joke()
            if joke is not None:
                print(joke)
                engine.say(joke)
                engine.runAndWait()
                
        elif 'list' or 'note' in query:
            print('Okay so what do you want to do? Create note? Read all notes? Read a single note? Delete a note?')
            engine.say('Okay so what do you want to do? Create note? Read all notes? Read a single note? Delete a note?')
            engine.runAndWait()
            task = recognize_speech()
            execute_tasks(task)
            
        elif "GPT" in query:
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

# Seperate method for determining todo list
def execute_tasks(task):
    """
    Method to execute todo list methods
    """
    if "create" in task:
        print("What's the title of the content?")
        engine.say("What's the title of the content?")
        engine.runAndWait()
        title = recognize_speech()
        print("What's the content?")
        engine.say("What's the content?")
        engine.runAndWait()
        content = recognize_speech()
        created_item = create_note(title, content)
        engine.say(f"You've successfully created {created_item[1]} containing {created_item[2]}")
        engine.runAndWait()
        
    elif "read" in task:
        print("Okay, fetching list from the database")
        engine.say("Okay, fetching list from the database")
        engine.runAndWait()
        notes = index_note()
        if notes:
            for index, (title, content) in enumerate(notes,  1):
                print(f"{index}. Title: {title}. Content: {content}")
                engine.say(f"{index}. Title: {title}. Content: {content}")
                engine.runAndWait()
        else:
            print("Sorry, there isn't any task.")
            engine.say("Sorry, there isn't any task.")
            engine.runAndWait()
            
    elif "update" in task:
        print("Which note id you want to edit?")
        engine.say("Which note id you want to edit?")
        engine.runAndWait()
        index = recognize_speech()
        single_note = show_note(index)
        print(f"This is the item i've found, ID: {single_note[0]}, title: {single_note[1]}, content: {single_note[2]}")
        engine.say(f"This is the item i've found, ID: {single_note[0]}, title: {single_note[1]}, content: {single_note[2]}")
        engine.runAndWait()
        
    elif "delete" in task:
        print("Okay so which note index do you want to delete?")
        engine.say("Okay so which note index do you want to delete?")
        engine.runAndWait()
        note_index = recognize_speech()
        delete_note(note_index)
    
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
