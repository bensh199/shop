import requests
import os

def get_bought_items(username, password):
    
    api_url = f'http://{os.getenv("BACKEND_HOST")}/get_bought_items'

    credentials = f'{username},{password}'

    print(credentials)
    response = requests.post(api_url, data=credentials)

    return response.json()

def buy_items(counter, item, username, password):

    data = f"{counter},{item},{username},{password}"
    print(data)

    api_url = f'http://{os.getenv("BACKEND_HOST")}/buy_item'

    response = requests.post(api_url, data=data)

    if response.status_code == 200:
        # Print the response content
        return(response.text)
    else:
        return(f"Error: {response.status_code}")