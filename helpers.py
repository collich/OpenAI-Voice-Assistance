"""
Imported Libraries
"""
# pylint: disable=trailing-whitespace

import webbrowser
from googlesearch import search

def send_email():
    pass

def open_website(site):
    """
    Open website for user method
    """
    browser_list = webbrowser.get()
    if len(browser_list) > 0:
        return webbrowser.open(site, new=2)
    
    return webbrowser.open(site, new=1)

def search_internet(search_term):
    """
    Google Searching for results
    """
    search(search_term)

def tell_joke():
    pass