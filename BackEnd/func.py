from kafka import KafkaProducer
from flask import jsonify
import requests
import json
import os

def buy_item(data):
    data_str = data.decode('utf-8')

    print(data)
    producer = KafkaProducer(bootstrap_servers='localhost:9093', value_serializer=lambda v: json.dumps(v).encode('utf-8'))
    
    topic = "purchased-items"

    message = data_str

    producer.send(topic, value=message)

def query_bought_items(credentials):
    api_url = f'http://{os.getenv("API_HOST")}/purchased_items'

    print(credentials)
    response = requests.post(api_url, data=credentials)

    data = response.json()
    print(type(data))
    return data