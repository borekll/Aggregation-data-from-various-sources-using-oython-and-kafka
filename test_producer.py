import time
import json
import random
from datetime import datetime
from generate_test_msg import generate_message
from kafka import KafkaProducer

#-- Messages will be serialized as JSON
def serializer(message):
    return json.dumps(message).encode('utf-8')

#-- Kafka Producer
producer = KafkaProducer(
    bootstrap_servers=['localhost:9092'],
    value_serializer=serializer
)

if __name__ == '__main__':
    for x in range(100):
        dummy_message = generate_message()

        print(f'Producting message @ {datetime.now()} | Message = {str(dummy_message)}')
        producer.send('messages', dummy_message)

    time.sleep(100000)







