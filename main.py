import requests 
import json
import robin_stocks as r 

# Returns the access token as a string
def login():
    login = r.login('dragon-froot710@protonmail.com', '1185949Bobsaget1')
    return login['access_token']
    # print(login['access_token'])

# Gets a list of all the stocks you own and returns an array of url's to get other data 
def get_list_of_owned_stocks():
    data = r.account.get_current_positions(info=None)
    for i in data:
        url = i['url']
        head = {"Accept": "application/json"}
        payload = {'name': 'Technology', "Authorizaton": "Token " + login()}
        # res = requests.get(url, headers=head, auth=payload, authori)
        print(i)
        # print(res.text)

    
 
login()
get_list_of_owned_stocks()

# Make sure that the user logs in from the terminal
