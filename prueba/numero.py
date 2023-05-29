import random

def generate_card_number():
    # Generar un número de tarjeta de 16 dígitos
    card_number = ''.join(random.choice('0123456789') for i in range(16))
    return card_number
card_number = generate_card_number()
print(card_number)