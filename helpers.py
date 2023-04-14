"""
Imported Libraries
"""
# pylint: disable=trailing-whitespace
import os
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
import webbrowser
import platform
import pyjokes
from googlesearch import search
from dotenv import load_dotenv

def send_email(to_recipient, subject, body, two_fac = False):
    """
    Email sending method
    Check if you have 2FA enable. If you do, change two_FA at the params to True
    """
    # First part is where the VA loads the env file, then retrieve both Sender email and pass then validate it
    # so as to ensure it's in the file
    load_dotenv()
    
    sender_email = os.getenv('SENDER_EMAIL')
    sender_password = os.getenv('SENDER_PASS')

    if not sender_email or not sender_password:
        raise ValueError("Sender email and/or password not found in environment variables")
    
    # Main email creation body
    recipient_email = to_recipient
    msg = MIMEMultipart()
    msg["From"] = send_email
    msg["To"] = recipient_email
    msg["Subject"] = subject
    msg.attach(MIMEText(body, "plain"))
    
    # For people who are using gmail, change outlook to gmail
    server = smtplib.SMTP('smtp.outlook.com', 587)
    server.starttls()
    
    # 2FA
    if two_fac:
        token = input("2-Factor Authentication Token: ")
        server.login(sender_email, f"{sender_password}{token}")
    else:
        server.login(sender_email, sender_password)
    
    # Server sending then close the server
    server.sendmail(sender_email, recipient_email, msg.as_string())
    server.quit()

def open_website(site):
    """
    Open website for user method
    """
    if platform.system() == "Windows":
        print(f'Opening Browser to {site}')
        return webbrowser.open(site)
    
    browser_list = webbrowser.get()
    if browser_list:
        print('Opening Browser to {site}')
        return webbrowser.open(site, new=2)
    
    print('Opening Browser to {site}')
    return webbrowser.open(site, new=1)

def search_internet(search_term):
    """
    Google Searching for results
    """
    print(f'Searching for {search_internet}')
    search(search_term)

def tell_joke():
    """
    Jokes methods
    """
    joke = pyjokes.get_joke()
    return joke
