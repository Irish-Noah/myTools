import datetime
import requests
import os
import json
import webbrowser
from dotenv import load_dotenv

load_dotenv()

CLIENT_ID = os.getenv('CLIENT_ID')
CLIENT_SECRET = os.getenv('CLIENT_SECRET')
REDIRECT_URI = os.getenv('REDIRECT_URL')
CODE_URL = os.getenv('CODE_URL')

output_path = os.path.join(os.path.dirname(__file__), 'output.json')

### Get an auth token to make the album request
def get_spotify_token(client_id, client_secret, code, redirect_uri):
    print('Authenticating...')
    url = "https://accounts.spotify.com/api/token"
    data = {
        "grant_type": "authorization_code",
        "code": code,
        "redirect_uri": redirect_uri,
        "client_id": client_id,
        "client_secret": client_secret
    }
    response = requests.post(url, data=data)
    print('Authentication complete!')
    return response.json()


### Gather all albums from my library
def get_albums_from_library(token): 

    all_albums = []
    url = "https://api.spotify.com/v1/me/albums"
    headers = {
        "Authorization": f"Bearer {token}"
    }
    params = {
         "limit": 50,
         "offset": 0
    }

    # keep getting albums until all have been gotten
    while True: 
        print('Sending a request for more albums...')
        response = requests.get(url, headers=headers, params=params).json()
        all_albums.extend(response.get('items', []))
        if response.get('next'):
            params['offset'] += params['limit'] # offset by 50 albums for each call until no more albums are left
        else: 
            break

    return all_albums

    # not needed but for checking structure of the response data. Save to output.json (untracked for privacy)
    with open(output_path, 'w') as outfile:
	    json.dump(response.json(), outfile, indent=2) 


### Get all albums that have been added since 2025-01-01
def count_new_albums(albums):
    print('Counting albums from this year...')
    total_2025 = 0
    for album in albums: 
        added_date = datetime.datetime.fromisoformat(album.get('added_at')).replace(tzinfo = None)
        compare_date = datetime.datetime(2025, 1, 1)
        if added_date >= compare_date: 
            total_2025 += 1
    return total_2025 - 1 # adjusting for the 1 LP and the album that I added from a previous year
    

def main(): 

    # Open the code retrieval url in my default browser and paste it into the terminal
    webbrowser.open(CODE_URL)
    code = input('Enter the code from the opened web browser: ') 

    token = get_spotify_token(CLIENT_ID, CLIENT_SECRET, code, REDIRECT_URI)
    albums = get_albums_from_library(token['access_token'])
    total = count_new_albums(albums)

    doy = int(datetime.datetime.now().strftime('%j'))
    if total < doy:
        print(f"It is day {doy} of {datetime.datetime.now().strftime('%Y')} and I have listened to {total} albums this year! Pick up the pace dude...")  
    elif total == doy:
        print(f"It is day {doy} of {datetime.datetime.now().strftime('%Y')} and I have listened to {total} albums this year! You are on track!")  
    else: 
        print(f"It is day {doy} of {datetime.datetime.now().strftime('%Y')} and I have listened to {total} albums this year! You're killing it!")  
    
    
if __name__ == '__main__': 
    main()