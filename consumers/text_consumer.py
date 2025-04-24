from kafka import KafkaConsumer

consumer = KafkaConsumer(
    'text-topic',
    bootstrap_servers='localhost:9092',
    auto_offset_reset='earliest',      # Start from the beginning of the topic
    enable_auto_commit=True,           # Automatically commit offsets
    group_id='text-group',             # Consumer group name
    value_deserializer=lambda x: x.decode('utf-8')
)

print("🚀 Listening to 'text-topic'...")

for message in consumer:
    print(f"🧾 Received: {message.value}")