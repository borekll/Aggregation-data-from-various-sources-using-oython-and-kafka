from kafka import KafkaConsumer
import json
import pandas as pd
from time import sleep
consumer = KafkaConsumer('emails', auto_offset_reset='earliest', bootstrap_servers=['localhost:9092']
                         , api_version=(0, 10))
message_count = 1
data_user_id = []
data_recipient_id = []
data_message = []
data_date = []
for emails in consumer:
    value = emails.value
    value = json.loads(emails.value)
    user_id = int(value['user_id'])
    recipient_id = int(value['recipient_id'])
    message = str(value['message'])
    date = int(value['date'])
    ##print(date)
    data_user_id.append(user_id)
    data_recipient_id.append(recipient_id)
    data_message.append(message)
    data_date.append(date)
    message_count += 1
    if message_count > 10:
        break
    else:
        pass
df = pd.DataFrame(data_user_id,columns=['user_id'])
df['recipient_id'] = data_recipient_id
df['message'] = data_message
df['date'] = data_date
print(df)
message_count1=1
consumer = KafkaConsumer('employees_traffic', auto_offset_reset='latest', bootstrap_servers=['localhost:9092']
                         , api_version=(0, 10))
for employees_traffic in consumer:
    value = employees_traffic.value
    value = json.loads(employees_traffic.value)
    ##user_id = int(value['user_id'])
    ##recipient_id = int(value['recipient_id'])
    ##message = str(value['message'])
    ##date = int(value['date'])
    print(value)
    ##data_user_id.append(user_id)
    ##data_recipient_id.append(recipient_id)
    ##data_message.append(message)
    ##data_date.append(date)
    message_count1 += 1
    if message_count1 > 10:
        break
    else:
        pass
