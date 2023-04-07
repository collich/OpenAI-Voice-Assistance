"""
Imported Libraries
"""
# pylint: disable=trailing-whitespace

import webbrowser
import platform
import pyjokes
from googlesearch import search

def send_email():
    pass

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
