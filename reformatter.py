import sys
import json
import requests

from tools import Loader

class Reformatter():
    def __init__(self):
        self.loader = Loader()
        self.content = self.get_file_contents()
        self.auth_token = self.request_auth_token()

    def get_file_contents(self):
        """Looks for a `contributors.json` file in the base directory"""

        with open('contributors.json', 'r') as f:
            content = json.load(f)

        return content

    def request_auth_token(self):
        """Requests the user to enter an access token"""
        # Show warning if over 60 or 250 items
        # anonymous users have a rate limit of 60 per hour
        auth_token = None
        if (len(self.content) > 60):
            print('An authentication token will be needed to request over 60 users')
            while auth_token is None:
                auth_token = input('Enter your access token ') or None

            if len(self.content) > 250:
                cont = input('The length of the input is over 250 users, do you want to continue? (y/n) ')
                if cont != 'y':
                    sys.exit(0)
        else:
            auth_token = input('Enter a personal access token (leave blank otherwise) ') or None

        return auth_token

    def reformat(self):
        """Gathers each user and writes to a JSON file"""
        output = []

        self.loader.start_loading()

        for account in self.content:
            account_url = account['url']

            user = self.fetch_user(account_url, self.auth_token)

            user_json = {
                'username': user['login'],
                'name': user['name'],
            }
            output.append(user_json)

        self.loader.stop_loading()

        with open ('reformatted.json', 'w') as f:
            json.dump(output, f, indent= 2)
    
    def fetch_user(self, account_url, PAT):
        """Fetch a user given the GitHub account URL"""
        headers = {
            'Accept': 'application/vnd.github+json',
            'Authorization': f'Bearer {PAT}'
            }
        response = requests.get(account_url, headers=headers) if PAT else requests.get(account_url)

        if not response.ok:
            self.loader.stop_loading()
            print(f'Request not successful\n{response.content}')
            sys.exit(1)

        return response.json()
    
Reformatter().reformat()