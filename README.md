# OpenAI-Voice-Assistance

For Windows:
1. python -m venv env
2. env\Scripts\activate.bat
3. pip install openai speechrecognition pyttsx3 python-dotenv googlesearch-python pyaudio pyjokes

Before Starting:
Create an env file on the main directory and an .sqlite file in data folder.
In the .env file, ensure that you have these variables OPENAI_API_KEY, SENDER_EMAIL and SENDER_PASS
OPENAI_API_KEY = your_api_key
SENDER_EMAIL = your_email
SENDER_PASS = your_email_password

Check your email. If it's outlook/hotmail, you don't have to change the code.
If it's Gmail or Yahoo, under helpers.py file, change line 39 from "smtp.outlook.com" to to either "smtp.gmail.com" or "smtp.yahoo.com" depending on your SENDER_EMAIL

Make sure to create a data file in the main directory then inside it, assistant.sqlite!