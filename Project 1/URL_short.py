# CS 230 Project 1
# Shortening URLs
# Editors: Kai Francis, Ryan Yonek, Haylee Jackson
# Last Modified: 9/16/24

import random
import string
import json
import re
import pyshorteners

# Store data mappings
URL_DATA_FILE = "url_data.json"

# Load data from JSON file
def load_url_data():
    try:
        with open('url_data.json', 'r') as file:
            return json.load(file)
    except (FileNotFoundError, json.JSONDecodeError):
        return {}


# Initialize JSON data dictionary
data = {}

# Save url data
def save_url_data(data):
    with open('url_data.json', 'w') as file:
        json.dump(data, file, indent=4)

# Generate random ID
def generate_random_id():
    return ''.join(random.choices(string.ascii_letters + string.digits, k=6))

# Validate URL format
def validate_url(url):
    url_pattern = re.compile(
        r'^(?:http|ftp)s?://'  # http:// or https://
        r'(?:[\w-]+\.)+[a-z]{2,6}'  # domain
        r'(?:[/?#][^\s]*)?$', re.IGNORECASE)
    return re.match(url_pattern, url) is not None

# Shorten the URL
def shorten_url(long_url, data):
    if not validate_url(long_url):
        return "Invalid URL. Please enter a valid URL."
    
    # Load URL data
    data = load_url_data()

    # Generate new ID    
    short_id = generate_random_id()
    while short_id in data:
        short_id = generate_random_id()

    # Use pyshorteners module to make usable short URL
    s = pyshorteners.Shortener()
    short_url = s.tinyurl.short(long_url)

    # Check to see if the new short URL already exists
    for short_id, stored_url in data.items():
        if stored_url == short_url:
            return f"Shortened URL already exists: {short_id}"
    
    # Store the new URL
    data[short_id] = short_url
    print(data[short_id])
    save_url_data(data)
    return f"Shortened URL: {short_url} (ID: {short_id})"

# Retrieve the original URL from the shortened version
def retrieve_url(short_id, data):
    data = load_url_data()
    return data.get(short_id, "Shortened URL not found.")

# Count the number of shortened URLs
def count_shortened_urls(data):
    data = load_url_data()
    return len(data)

# Delete a specified short URL and ID
def delete_shortened_urls(data, short_id):
    data = load_url_data()
    del data[short_id]
    save_url_data(data)


# User interaction loop
def main():
    data = load_url_data()
    while True:
        print("\nURL Shortener Menu:")
        print("1. Shorten a URL")
        print("2. Retrieve a URL")
        print("3. Count shortened URLs")
        print("4. Delete a URL")
        print("5. Exit")
        
        
        try:
            choice = input("Enter your choice (1-5): ").strip()
            
            if choice == '1':
                long_url = input("Enter the URL to shorten: ").strip()
                print(shorten_url(long_url, data))
            elif choice == '2':
                short_id = input("Enter the shortened URL ID: ").strip()
                print(retrieve_url(short_id, data))
            elif choice == '3':
                print(f"Total shortened URLs: {count_shortened_urls(data)}")
            elif choice == '4':
                short_id = input("Enter the shortened URL ID to be deleted: ").strip()
                delete_shortened_urls(data, short_id)
                data = load_url_data()
                print("New data dictionary: ", data)
            elif choice == '5':
                print("Goodbye!")
                break
            else:
                print("Invalid choice. Please enter a number between 1 and 5.")
        except EOFError:
            print("\nUnexpected end of input. Exiting...")
            break
        except KeyboardInterrupt:
            print("\nKeyboard interruption detected. Exiting...")
            break



if __name__ == "__main__":
    main()
