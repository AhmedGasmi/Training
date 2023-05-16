import requests
from getpass import getpass

API_URL = 'http://localhost:5000/protected'

def main():
    username = input('Username: ')
    password = getpass('Password: ')

    response = requests.get(API_URL, auth=(username, password))

    if response.status_code == 200:
        print('Access granted:', response.json()['message'])
    else:
        print('Access denied:', response.json()['error'])

if __name__ == '__main__':
    main()
