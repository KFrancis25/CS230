import random
import string
import json
import re

#store data mappings
URL_DATA_FILE = "url_data.json"

#load data from JSON file
def load_url_data():
    try:
        with open(URL_DATA_FILE, 'r') as file: 
            return json.load(file)
    except FileNotFoundError:
        return {}
    except json.JSONDecodeError:
        return {}
    

#Save url data
def save_url_data():
    with open(URL_DATA_FILE, 'w') as file:
        json.dump(data, file)

#generate random ID
def generate_random_id():
    return ''.join(random.choices(string.ascii_uppercase + string.digits, k=8))

#Validate URL format
def validate_url(url):
    url_pattern = re.compile(
        r'^(?:http|ftp)s?://'  # http:// or https://
        r'(?:[\w-]+\.)+[a-z]{2,6}'  # domain
        r'(?:[/?#][^\s]*)?$', re.IGNORECASE)
    return url_pattern.match(url) is not None

#shorten the URL
def shorten_url(long_url):
    if not validate_url(long_url):
        return "Invalid URL. Please enter a valid URL."
    
    #load URL data
    url_data = load_url_data()

    #Check to see if the URL already exists
    for short_id, stored_url in url_data.items():
        if stored_url == long_url:
            return f"Shortened URL already exists{short_id}"

    #generate new ID    
    short_id = generate_short_id()
    while short_id in url_data:
        short_id = generate_short_id()

    # Store the new URL
    url_data[short_id] = long_url
    save_url_data(url_data)
    return f"Shortened URL: {short_id}"
