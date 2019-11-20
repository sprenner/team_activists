import requests 

# Add your TEAMID here:
TEAMID = 'yourteamid'
URL = "http://172.31.99.115:8000/deletelater/json"

if TEAMID == 'yourteamid':
	print('You have to insert your TEAMID in backdoor.py for it to work.')
	exit(1)


while True:
    text = input("Enter a message: ")
    PARAMS = {'text':text, 'team': TEAMID} 
    r = requests.get(url = URL, params = PARAMS)
    data = r.json()
    if data['success']:
    	print(data['result'])
    else:
    	print(data['error'])
