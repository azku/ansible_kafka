from kafka import KafkaProducer
import requests
import json
import time

# Set Kafka Producer
producer = KafkaProducer(bootstrap_servers='localhost:9092', value_serializer=lambda x: json.dumps(x).encode('utf-8'))

# OpenSky API endpoint (for real-time flights)
url = 'https://opensky-network.org/api/states/all'

def fetch_flight_data():
    response = requests.get(url)
    return response.json()

def send_flight_data():
    while True:
        data = fetch_flight_data()
        producer.send('flight_data_topic', value=data)
        time.sleep(100)  # Send data every 10 seconds

send_flight_data()
