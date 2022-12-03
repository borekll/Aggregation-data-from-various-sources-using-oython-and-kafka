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

    actual_day=1
    limit_actions_per_day=0
    while True:
        dummy_message = generate_message(actual_date=actual_day)

        print(f'Producting message @ {datetime.now()} | Message = {str(dummy_message)}')
        producer.send('messages', dummy_message)

        time.sleep(2)

        limit_actions_per_day+=1

        if limit_actions_per_day == 10:
            limit_actions_per_day = 0
            actual_day +=1



