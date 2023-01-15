#-- przykladowe generowanie wartosci wiadomosci do wyslania na temat traffic
import time
import random
import string


#-- Przygotowanie listy ID pracowników
user_ids = list(range(1, 101))

#-- Funkcja z której będzie korzystał producer symulujący aktywność pracowników
def generate_traffic(actual_date) -> dict:

    #-- Wybieramy pracownika oraz typ akcji: wejście do budynku firmy lub jej opuszczenie
    random_user_id = random.choice(user_ids)
    entering = random.choice([True, False])

    #-- zależnie od wylosowanej operacji zwracana jest odpowiednia wartość
    if entering:

        return {
            'user_id': random_user_id,
            'entering': 1,
            'leaving' : 0,
            'date' : actual_date
        }
    else:
        return {
            'user_id': random_user_id,
            'entering': 0,
            'leaving': 1,
            'date': actual_date
        }



if __name__ == '__main__':
    print(generate_traffic())

