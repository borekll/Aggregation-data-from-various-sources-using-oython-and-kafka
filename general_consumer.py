from kafka import KafkaConsumer
import json

#-- localhost należy zmienić na IP urządzenia służącego jako kafka broker
traffic_consumer = KafkaConsumer(auto_offset_reset='earliest',
                                 bootstrap_servers=['localhost:9092'],
                                 api_version=(0, 10))


traffic_consumer.subscribe("traffic3")
print("zasubskrybowano do traffic")


traffic_messages=0

#-- pętla traffic pobiera wszystkie obecnie dostępne w temacie wiadomości
#-- obecnie ograniczone na potrzeby testowania 01-01-2023

for traffic in traffic_consumer:

    traffic_messages+=1
    print("traffic loop")

    value = traffic.value
    value = json.loads(traffic.value)

    print(value)

    if traffic_messages == 50:

        break


print("emails consumer")


email_consumer = KafkaConsumer(auto_offset_reset='earliest', bootstrap_servers=['localhost:9092'],
                               api_version=(0, 10))

email_consumer.subscribe('emails2')
print("zasubskrybowano do emails")

emails_messages = 0

for emails in email_consumer:

    print("emails loop")

    value = emails.value
    value = json.loads(emails.value)

    print(value)


    #print(value)

    if emails_messages == 50:
        break


