import random
import string
import json
import re

#store data mappings
URL_DATA_FILE = "url_data.json"

#load data from JSON file
def load_url_data():
    try:
        with open(URL_DATA_FILE, "r") as file: 
            return json.load(file)
    except (FileNotFoundError, json.JSONDecodeError):
        return {}
    

#Save url data
def save_url_data():
    with open(URL_DATA_FILE, "w") as file:
        json.dump(data, file)

#generate random ID
def generate_random_id():
    return ''.join(random.choices(string.ascii_letters + string.digits, k=6))

#Validate URL format
def validate_url(url):
    url_pattern = re.compile(
        r'^(?:http|ftp)s?://'  # http:// or https://
        r'(?:[\w-]+\.)+[a-z]{2,6}'  # domain
        r'(?:[/?#][^\s]*)?$', re.IGNORECASE)
    return re.match(url_pattern, url) is not None

#shorten the URL
def shorten_url(long_url):
    if not validate_url(long_url):
        return "Invalid URL. Please enter a valid URL."
    
    #load URL data
    url_data = load_url_data()

    #Check to see if the URL already exists
    for short_id, stored_url in url_data.items():
        if stored_url == long_url:
            return f"Shortened URL already exists: {short_id}"

    #generate new ID    
    short_id = generate_short_id()
    while short_id in url_data:
        short_id = generate_short_id()

    # Store the new URL
    url_data[short_id] = long_url
    save_url_data(url_data)
    return f"Shortened URL: {short_id}"

# Retrieve the original URL from the shortened version
def retrieve_url(short_id):
    url_data = load_url_data()
    return url_data.get(short_id, "Shortened URL not found.")

# Count the number of shortened URLs
def count_shortened_urls():
    url_data = load_url_data()
    return len(url_data)

#User interaction loop
def main():
    while True:
        print("\nURL Shortener Menu:")
        print("1. Shorten a URL")
        print("2. Retrieve a URL")
        print("3. Count shortened URLs")
        print("4. Exit")

        try:
            choice = input("Enter your choice (1-4): ").strip()
            
            if choice == '1':
                long_url = input("Enter the URL to shorten: ").strip()
                print(shorten_url(long_url))
            elif choice == '2':
                short_id = input("Enter the shortened URL ID: ").strip()
                print(retrieve_url(short_id))
            elif choice == '3':
                print(f"Total shortened URLs: {count_shortened_urls()}")
            elif choice == '4':
                print("Goodbye!")
                break
            else:
                print("Invalid choice. Please enter a number between 1 and 4.")
        except EOFError:
            print("\nUnexpected end of input. Exiting...")
            break
        except KeyboardInterrupt:
            print("\nKeyboard interruption detected. Exiting...")
            break

if __name__ == "__main__":
    main()
