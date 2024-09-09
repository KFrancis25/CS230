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

