from confluent_kafka import Consumer, KafkaException, KafkaError
import threading

# Define a function to consume messages from Kafka
def consume_messages(consumer_id, topic, group_id):
    conf = {
        'bootstrap.servers': 'localhost:9092',  # Kafka broker
        'group.id': group_id,  # Consumer group
        'auto.offset.reset': 'earliest'  # Start consuming from the earliest message
    }

    # Create a consumer instance
    consumer = Consumer(conf)

    try:
        # Subscribe to the topic
        consumer.subscribe([topic])

        print(f"Consumer {consumer_id} started consuming from topic: {topic}")

        # Consume messages
        while True:
            msg = consumer.poll(timeout=1.0)  # 1 second timeout for polling
            if msg is None:
                continue  # No message available within timeout
            if msg.error():
                if msg.error().code() == KafkaError._PARTITION_EOF:
                    print(f"Consumer {consumer_id}: End of partition reached.")
                else:
                    raise KafkaException(msg.error())
            else:
                print(f"Consumer {consumer_id} received message: {msg.value().decode('utf-8')}")

    except KeyboardInterrupt:
        print(f"Consumer {consumer_id} interrupted.")
    finally:
        # Close the consumer
        consumer.close()

# Function to create multiple consumers
def create_consumers(num_consumers, topic, group_id):
    threads = []
    for i in range(num_consumers):
        consumer_thread = threading.Thread(target=consume_messages, args=(i + 1, topic, group_id))
        threads.append(consumer_thread)
        consumer_thread.start()

    # Wait for all threads (consumers) to finish
    for thread in threads:
        thread.join()

if __name__ == "__main__":
    topic_name = 'text-topic'  # Change this to your topic
    group_id = 'text-consumer-group'  # The consumer group name
    num_consumers = 3  # Number of consumers you want to create

    create_consumers(num_consumers, topic_name, group_id)
