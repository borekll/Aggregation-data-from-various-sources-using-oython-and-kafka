import time
import json
import random
from datetime import datetime

from generate_test_msg import generate_message
from generate_employee_traffic import generate_traffic

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
        email_event = generate_message(actual_date=actual_day)

        print(f'Sending email @ {datetime.now()} | Email = {str(email_event)}')
        producer.send('emails', email_event)


        traffic_event = generate_traffic(actual_date=actual_day)

        print(f'employees_traffic @ {datetime.now()} | Traffic = {str(traffic_event)}')
        producer.send('employees_traffic', email_event)


        time.sleep(2)

        limit_actions_per_day+=1

        if limit_actions_per_day == 10:
            limit_actions_per_day = 0
            actual_day +=1



