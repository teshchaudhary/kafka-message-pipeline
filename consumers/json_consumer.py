from kafka import KafkaConsumer

consumer = KafkaConsumer(
    'json-topic',
    bootstrap_servers='localhost:9092',
    auto_offset_reset='earliest',      # Start from the beginning of the topic
    enable_auto_commit=True,           # Automatically commit offsets
    group_id='json-group',             # Consumer group name
    value_deserializer=lambda x: x.decode('utf-8')
)

print("🚀 Listening to 'json-topic'...")

for message in consumer:
    print(f"🧾 Received: {message.value}")