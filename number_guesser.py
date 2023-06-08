import random

input_number = input("Guess the number between 0-10 ")
random_number = random.randrange(0, 11)
if input_number.isdigit():
    input_number = int(input_number)
    if input_number <= 0:
        print('Enter a number greater than 0')
else:
    print('Type a number next time')
    quit()

if input_number == random_number:
    print('Your guess is correct')
else:
    print('Your guess is incorrect')
