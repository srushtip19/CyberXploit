import requests


def http_bruteforce(url, username, wordlist):

    try:

        with open(wordlist, 'r') as file:
            passwords = file.readlines()

        for password in passwords:

            password = password.strip()

            data = {
                'username': username,
                'password': password
            }

            response = requests.post(url, data=data)

            if 'Login Successful' in response.text:

                return {
                    'status': 'success',
                    'username': username,
                    'password': password
                }

        return {
            'status': 'failed'
        }

    except Exception as e:

        return {
            'error': str(e)
        }