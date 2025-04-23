from kafka import KafkaProducer
import time

# Kafka server connection
producer = KafkaProducer(bootstrap_servers='localhost:9092')

# Send messages to the demo-topic
for i in range(100):
    message = f"Message {i+1}"
    producer.send('demo-topic', value=message.encode('utf-8'))
    print(f"Sent: {message}")
    time.sleep(1)  # Adding a delay to mimic real-world data

producer.flush()
producer.close()
