from secret_number import seed_secret_numbers , generate_secret_number
from response import input_response

seed = int(input("Enter a seed number: "))
seed_secret_numbers(seed)

generate_value = generate_secret_number()

tries = 0
correcto = False

while not correcto:
    user_input = int(input("What is your guess: "))
    tries +=1


    mensaje, correcto = input_response(generate_value, user_input)
    print(mensaje)

print("It took you", tries, "tries!")