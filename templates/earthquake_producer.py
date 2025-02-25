from kafka import KafkaProducer
import requests
import json
import time

# Set Kafka Producer
producer = KafkaProducer(bootstrap_servers='localhost:9092', value_serializer=lambda x: json.dumps(x).encode('utf-8'))

# USGS Earthquake API endpoint
url = 'https://earthquake.usgs.gov/earthquakes/feed/v1.0/summary/2.5_day.geojson'

def fetch_earthquake_data():
    response = requests.get(url)
    return response.json()

def send_earthquake_data():
    while True:
        data = fetch_earthquake_data()
        producer.send('earthquake_topic', value=data)
        time.sleep(60)  # Wait 1 minute before checking again

send_earthquake_data()



## probatzeko
##  /opt/kafka/bin/kafka-console-consumer.sh --bootstrap-server localhost:9092 --topic earthquake_topic --from-beginning
# producerra eta consumerra programatu ditzatela nik datuak eta brokerra emanda.
