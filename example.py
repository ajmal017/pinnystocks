from Robinhood import Robinhood
import sys

robinhood = None

def login():
    robinhood = Robinhood()
    username = input('Enter robinhood username: ')
    password = input('Enter robinhood password: ')
    try:
        robinhood.login(username=username, password=password)
    except:
        error = sys.exc_info()[0]
        print(f'[LOGIN] {error}')
        login()
    else: 
        print('[LOGIN] successful. Taking you to tags...sd:')

def tags():
    print('404')

if __name__ == '__main__':
    login()
