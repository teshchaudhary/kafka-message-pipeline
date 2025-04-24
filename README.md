# Kafka Project with Confluent Using Docker Compose

---

## Step 1: Setup with Docker Compose

### 📦 Docker Compose File (`docker-compose.yml`)
Use Confluent's Kafka and Zookeeper images:

```yaml
version: '3.8'
services:
  zookeeper:
    image: confluentinc/cp-zookeeper:latest
    environment:
      ZOOKEEPER_CLIENT_PORT: 2181
      ZOOKEEPER_TICK_TIME: 2000
    ports:
      - '2181:2181'

  kafka:
    image: confluentinc/cp-kafka:latest
    depends_on:
      - zookeeper
    ports:
      - '9092:9092'
    environment:
      KAFKA_BROKER_ID: 1
      KAFKA_ZOOKEEPER_CONNECT: zookeeper:2181
      KAFKA_ADVERTISED_LISTENERS: PLAINTEXT://localhost:9092
      KAFKA_OFFSETS_TOPIC_REPLICATION_FACTOR: 1
```

### 🚀 Start the services
```bash
docker-compose up -d
```
> `-d` means detached mode (runs in the background)

---

## Step 2: Create Kafka Topics

### ✅ Create `text-topic`
```bash
docker exec -it <kafka_container_name> kafka-topics \
  --create \
  --topic text-topic \
  --bootstrap-server localhost:9092 \
  --partitions 1 \
  --replication-factor 1
```

### ✅ Create `json-topic`
```bash
docker exec -it <kafka_container_name> kafka-topics \
  --create \
  --topic json-topic \
  --bootstrap-server localhost:9092 \
  --partitions 1 \
  --replication-factor 1
```

### 🔍 List Topics
```bash
docker exec -it <kafka_container_name> kafka-topics \
  --list \
  --bootstrap-server localhost:9092
```

---

## Step 3: Change number of partitions for a topic

### Method 1: Alter Partitions (Increase)
To **increase** the number of partitions for an existing topic:

```bash
docker exec -it <kafka_container_name> kafka-topics \
  --alter \
  --topic <topic_name> \
  --bootstrap-server localhost:9092 \
  --partitions 3
```

> **Note:** You can only **increase** the number of partitions. **Decreasing** the partition count is **not supported** in Kafka.

### Method 2: Recreate `text-topic` with 3 partitions
Alternatively, if you prefer to **delete and recreate** the topic:

1. **Delete the `topic`:**
   ```bash
   docker exec -it <kafka_container_name> kafka-topics \
     --delete \
     --topic <topic_name> \
     --bootstrap-server localhost:9092
   ```

2. **Recreate `topic` with 3 partitions:**
   ```bash
   docker exec -it <kafka_container_name> kafka-topics \
     --create \
     --topic t<topic_name> \
     --bootstrap-server localhost:9092 \
     --partitions 3 \
     --replication-factor 1
   ```

---

## Step 4: Create Producer Scripts

##### ✅ `text_producer.py`


##### ✅ `json_producer.py`


### 🚀 Run the Producers
```bash
python producer.py
python json_producer.py
```

---

## Step 5: Consume Messages

```bash
docker exec -it <kafka_container_name> kafka-console-consumer \
  --bootstrap-server localhost:9092 \
  --topic <topic_name> \
  --from-beginning
```

---