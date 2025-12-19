import json
import os
from kafka import KafkaProducer
from vitals_generator import generate_vitals
import time


KAFKA_TOPIC = os.environ.get("KAFKA_TOPIC", "patient_vitals")

def create_producer():
    try:
        producer = KafkaProducer(
            bootstrap_servers=os.environ.get("KAFKA_BROKER_URL", "localhost:9092").split(","), #Get kafka broker url from environment variables
            value_serializer=lambda x: json.dumps(x).encode('utf-8')
        )
        print("Kafka Producer connected")
        return producer
    except Exception as e:
        print(f"Error connecting to Kafka: {e}")
        return None


def send_vitals_to_kafka(producer, topic, vitals):
    try:
        producer.send(topic, value=vitals)
        producer.flush()
        print(f"Sent vitals for patient {vitals['patient_id']} to Kafka topic {topic}")
    except Exception as e:
        print(f"Error sending data to Kafka: {e}")


if __name__ == '__main__':
    producer = create_producer()
    if producer:
        while True:
            vitals_data = generate_vitals()
            send_vitals_to_kafka(producer, KAFKA_TOPIC, vitals_data)
            time.sleep(1)
