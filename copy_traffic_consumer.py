from kafka import KafkaConsumer
import json


traffic_consumer = KafkaConsumer(auto_offset_reset='earliest', bootstrap_servers=['localhost:9092'])
traffic_consumer.subscribe("traffic")

print("zasubskrybowano do traffic")



message_count = 1
data_user_id = []
data_recipient_id = []
data_message = []
data_date = []


for traffic in traffic_consumer:

    print("for jednak dziala")

    value = traffic.value
    value = json.loads(traffic.value)

    print(value)

    user_id = int(value['user_id'])
    date = int(value['date'])
    ##print(date)
    data_user_id.append(user_id)
    data_date.append(date)
    message_count += 1


