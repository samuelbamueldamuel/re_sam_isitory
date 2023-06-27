import requests
i = 0 
url = "https://api.namefake.com/"
while(i < 5):
    response = requests.get(url).json()
    initName = response['name'].split()[0]
    if (initName == 'Mr.' or initName == 'Dr.' or initName == 'Mrs.' or initName == 'Ms.' or initName == 'Miss'):
        name = response['name'].split()[1]
    i += 1