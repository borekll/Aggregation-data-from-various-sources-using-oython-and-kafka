import time
import random
import string


#-- przykladowe generowanie wartosci wiadomosci do wyslania kafce
user_ids = list(range(1, 101))
recipient_ids = list(range(1, 101))


def generate_message(actual_date) -> dict:
    random_user_id = random.choice(user_ids)

    # Copy the recipients array
    recipient_ids_copy = recipient_ids.copy()

    # User can't send message to himself
    recipient_ids_copy.remove(random_user_id)
    random_recipient_id = random.choice(recipient_ids_copy)

    # Generate a random message

    message = ''.join(random.choice(string.ascii_letters) for i in range(32))

    return {
        'user_id': random_user_id,
        'recipient_id': random_recipient_id,
        'message': message,
        'date' : actual_date #currently an integer for presentation; use data_stamp for real life implementaion
    }

if __name__ == '__main__':
    print(generate_message(1))


