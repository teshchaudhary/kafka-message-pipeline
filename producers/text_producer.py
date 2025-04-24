from kafka import KafkaProducer
import time

producer = KafkaProducer(bootstrap_servers='localhost:9092')

for i in range(100):
    message = f"Message {i+1}"
    producer.send('text-topic', value=message.encode('utf-8'))
    print(f"Sent !!")
    time.sleep(1)

producer.flush()
producer.close()