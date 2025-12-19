FROM python:3.9-slim-buster

WORKDIR /app

COPY hospital_vitals_stream/vitals_generator.py ./vitals_generator.py
COPY hospital_vitals_stream/kafka_producer.py ./kafka_producer.py

RUN pip install --no-cache-dir kafka-python

ENV KAFKA_BROKER_URL=localhost:9092
ENV KAFKA_TOPIC=patient_vitals

CMD ["python", "kafka_producer.py"]