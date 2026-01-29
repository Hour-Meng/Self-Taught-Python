# In this we will learn how to make API requests using Python
# First of all you need to install "requests" library if you don't have it already
# Type pip install requests in your terminal

import requests

base_url = "https://pokeapi.co/api/v2/pokemon/"

def get_pokemon(name):
    url = f"{base_url}{name.lower()}"
    response = requests.get(url)

    print(response)
    # what you will get in response is a status code

    if response.status_code == 200:
        the_data = response.json() # what you will get is a very larnge dictionary
        return the_data

    else:
        print(f"{response.status_code}: There was an error retrieving the data.")



name = "pikachu"

get_pokemon(name)

data = get_pokemon("charizard")


# put it in a if loop to avoid error if data is None
if data:
    print(data["name"])
    print(data["height"])
    print(data["weight"])