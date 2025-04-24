import json
from kafka import KafkaProducer
import time

producer = KafkaProducer(
    bootstrap_servers='localhost:9092',
    value_serializer=lambda v: json.dumps(v).encode('utf-8')
)

for i in range(100):
    record = {"id": i, "event": f"event-{i}"}
    producer.send('json-topic', record)
    print(f"Sent !!")
    time.sleep(1)

producer.flush()
producer.close()