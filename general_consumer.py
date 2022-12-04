from kafka import KafkaConsumer
import json


traffic_consumer = KafkaConsumer(auto_offset_reset='earliest', bootstrap_servers=['localhost:9092'],
                                 api_version=(0, 10))
traffic_consumer.subscribe("traffic")
print("zasubskrybowano do traffic")

email_consumer = KafkaConsumer(auto_offset_reset='earliest', bootstrap_servers=['localhost:9092'],
                               api_version=(0, 10))

email_consumer.subscribe('emails')
print("zasubskrybowano do emails")


for traffic in traffic_consumer:

    print("traffic loop")

    value = traffic.value
    value = json.loads(traffic.value)

    print(value)

   #bledy w consumerze zmusily do usuniecia pobierania
   #do chwili naprawienia tylko wyswietlanie


#-- emaile


message_count = 1
data_user_id = []
data_recipient_id = []
data_message = []
data_date = []

for emails in email_consumer:

    print("emails loop")

    value = emails.value
    value = json.loads(emails.value)

    print(value)

    user_id = int(value['user_id'])
    recipient_id = int(value['recipient_id'])
    message = str(value['message'])
    date = int(value['date'])

    #print(date)
    data_user_id.append(user_id)
    data_recipient_id.append(recipient_id)
    data_message.append(message)
    data_date.append(date)
    message_count += 1

