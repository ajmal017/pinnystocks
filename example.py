import robin_stocks
import sys

def login():
    username = input('Enter robinhood username: ')
    password = input('Enter robinhood password: ')
    try:
        device_id = robin_stocks.get_new_device_token(username, password)
        robin_stocks.login(username, password, device_id)
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
