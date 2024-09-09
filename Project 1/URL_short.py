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
