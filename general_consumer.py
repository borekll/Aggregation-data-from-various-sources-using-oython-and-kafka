from kafka import KafkaConsumer

import json


traffic_consumer = KafkaConsumer(auto_offset_reset='earliest', bootstrap_servers=['localhost:9092'],
                                 api_version=(0, 10))
traffic_consumer.subscribe("traffic")
print("zasubskrybowano do traffic")


traffic_messages=0

for traffic in traffic_consumer:

    traffic_messages+=1
    print("traffic loop")

    value = traffic.value
    value = json.loads(traffic.value)

    print(value)

    if traffic_messages == 50:
        break

   #bledy w consumerze zmusily do usuniecia pobierania
   #do chwili naprawienia tylko wyswietlanie


#-- emaile


#message_count = 1
#data_user_id = []
#data_recipient_id = []
#data_message = []
#data_date = []

print("emails consumer")

email_consumer = KafkaConsumer(auto_offset_reset='earliest', bootstrap_servers=['localhost:9092'],
                               api_version=(0, 10))

email_consumer.subscribe('emails')
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

    user_id = int(value['user_id'])
    recipient_id = int(value['recipient_id'])
    message = str(value['message'])
    date = int(value['date'])



    #print(date)
    #data_user_id.append(user_id)
    #data_recipient_id.append(recipient_id)
    #data_message.append(message)
    #data_date.append(date)
    #message_count += 1


