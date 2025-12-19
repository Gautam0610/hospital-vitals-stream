# Hospital Vitals Stream

This project generates random human vitals data and sends it continuously to a Kafka topic.

## Prerequisites

*   Docker
*   Kafka cluster (e.g., running locally or in a cloud environment)

## Usage

1.  Clone the repository:

    ```bash
    git clone https://github.com/Gautam0610/hospital-vitals-stream.git
    cd hospital-vitals-stream
    ```

2.  Build the Docker image:

    ```bash
    docker build -t hospital-vitals-stream .
    ```

3.  Run the Docker container, setting the environment variables for the Kafka broker URL and topic:

    ```bash
    docker run -e KAFKA_BROKER_URL=<your_kafka_broker_url> -e KAFKA_TOPIC=patient_vitals hospital-vitals-stream
    ```

    Replace `<your_kafka_broker_url>` with the actual URL of your Kafka broker (e.g., `localhost:9092`).

## Configuration

The following environment variables can be configured:

*   `KAFKA_BROKER_URL`: The URL of the Kafka broker (default: `localhost:9092`).
*   `KAFKA_TOPIC`: The name of the Kafka topic to send data to (default: `patient_vitals`).
