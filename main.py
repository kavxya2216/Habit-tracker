from http.client import responses
from datetime import datetime
import requests
from dotenv import load_dotenv
import os

load_dotenv()  # take environment variables from .env


USERNAME = os.getenv("pixela_username")
TOKEN = os.getenv("pixela_token")


pixela_endpoint = "https://pixe.la/v1/users"

user_params = {
    "token": TOKEN,
    "username": USERNAME,
    "agreeTermsOfService": "yes",
    "notMinor": "yes",
}

# response = requests.post(url=pixela_endpoint, json=user_params)
# print(response.text)

#Creating the graph
graph_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs"

graph_config = {
    "id": "graph1",
    "name": "Reading Graph",
    "unit": "pages",
    "type": "int",
    "color": "ajisai",
    
}

headers = {
    "X-USER-TOKEN": TOKEN
}

# response = requests.post(url=graph_endpoint, json=graph_config, headers=headers)
# print(response.text)

#Adding a pixel on the graph
today = datetime.now()

post_a_pixel_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs/graph1"
pixel_config = {
    "date": today.strftime("%Y%m%d"),
    "quantity": input("How many pages did you read today?📕✨"),
}

response = requests.post(url=post_a_pixel_endpoint, json=pixel_config, headers=headers)
print(response.text)


#Updating a pixel
update_pixel_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs/graph1/20250518"
update_params = {
    "quantity": "44"
}

# response = requests.put(url=update_pixel_endpoint, json=update_params, headers=headers)
# print(response.text)


#Deleting a pixel
delete_pixel_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs/graph1/20250519"

# response = requests.delete(url=delete_pixel_endpoint, headers=headers)
# print(response.text)