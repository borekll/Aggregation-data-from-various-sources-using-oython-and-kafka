#-- Skrypt działający jako prodocer wiadomości dla Kafka Broker
#-- Wykorzystuje stworzone wcześniej metody do symulowania aktywności w pewnej firmie opisanej w dokumentacji projektu

import time
import json
import random
from datetime import datetime

from generate_email_msg import generate_message
from generate_traffic_msg import generate_traffic

from kafka import KafkaProducer


#-- Wybieramy format JSON jako serializer dla wiadomości Kafki
def serializer(message):
    return json.dumps(message).encode('utf-8')


#-- Kafka Producer
producer1 = KafkaProducer(
    bootstrap_servers=['localhost:9092'], #localhost należy zmienić na IP urządzenia służącego jako kafka broker
    value_serializer=serializer
)

producer2 = KafkaProducer(
    bootstrap_servers=['localhost:9092'], #local host należy zmienić na IP urządzenia służącego jako kafka broker
    value_serializer=serializer
)

if __name__ == '__main__':

    #Testowy iterator ograniczający liczbe wysyłanych wiadomości podczas symulowania aktywności pracowników
    actual_day = 1
    limit_actions_per_day = 0

    while True:


        email_event = generate_message(actual_date=actual_day)

        print(f'Sending email @ {datetime.now()} | Email = {str(email_event)}')
        producer1.send('emails', email_event)
        producer1.flush()

        #-- Flush() zapewnia, że wszystkie wiadomości zostaną wysłane na temat do którego zasubskrybowany jest producer


        traffic_event = generate_traffic(actual_date=actual_day)

        print(traffic_event)

        print(f'traffic @ {datetime.now()} | Traffic = {str(traffic_event)}')
        producer2.send('traffic', traffic_event)
        producer2.flush()



        #-- warunek wyjścia z pętli
        time.sleep(0.1)

        limit_actions_per_day += 1

        if limit_actions_per_day == 10:
            limit_actions_per_day = 0
            actual_day += 1

        if actual_day == 10:
            break

