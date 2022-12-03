import time
import random
import string


#-- przykladowe generowanie wartosci wiadomosci do wyslania kafce
user_ids = list(range(1, 101))


def generate_traffic(actual_date) -> dict:
    random_user_id = random.choice(user_ids)



    entering= random.choice([True,False])

    if entering:

        return {
            'user_id': random_user_id,
            'entering': True,
            'leaving' : False,
            'date' : actual_date #currently an integer for presentation; use data_stamp for real life implementaion
    }
    else:
        return {
            'user_id': random_user_id,
            'entering': False,
            'leaving': True,
            'date': actual_date  # currently an integer for presentation; use data_stamp for real life implementaion
        }



if __name__ == '__main__':
    print(generate_traffic(1))

