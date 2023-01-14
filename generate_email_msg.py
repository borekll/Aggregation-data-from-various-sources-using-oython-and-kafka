#-- przykladowe generowanie wartosci wiadomosci do wyslania kafce
import time
import random
import string


#-- Przygotowanie listy ID pracowników

user_ids = list(range(1, 101))
recipient_ids = list(range(1, 101))

#-- Funkcja z której będzie korzystał producer symulujący aktywność pracowników
def generate_message(actual_date) -> dict:

    #-- Wybieramy pracownika oraz upewniamy się, że nie będzie on w stanie wysyłać maili do samego siebie

    random_user_id = random.choice(user_ids)
    recipient_ids_copy = recipient_ids.copy()
    recipient_ids_copy.remove(random_user_id)
    random_recipient_id = random.choice(recipient_ids_copy)

    #-- generujemy string mający symulować potencjalnego maila

    message = ''.join(random.choice(string.ascii_letters) for i in range(32))

    #-- Tak przygotowaną wiadomość zwracamy do producera
    return {
        'user_id': random_user_id,
        'recipient_id': random_recipient_id,
        'message': message,
        'date' : actual_date
    }

if __name__ == '__main__':
    print(generate_message(1))


