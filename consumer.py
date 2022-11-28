from kafka import KafkaConsumer
consumer = KafkaConsumer('messages',auto_offset_reset='earliest', bootstrap_servers=['localhost:9092']
                         ,api_version=(0, 10))
for message in consumer:
    print(message)