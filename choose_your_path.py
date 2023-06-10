print('This game has a pattern. You have to guess the answer and if the answer is right you are towards the goal else you will lost the game. ')

name_of_user = input("What's your name? ")
print('Hey '+name_of_user + " the game is on.. ")

press = input('Press y to start the game.. ').lower()

if press != 'y':
    quit()
else:
    print("Let's start the game!! ")

print('There is a road and you have to guess the direction.. ')
answer = input("Choose left or right ").lower()

if answer == "left":
    answer = input(
        'You can now swim across the river or walk around the road. Choose one. ').lower()
    if answer == 'swim':
        print("You'll be killed by alligator. And you loose the game. ")
        quit()

    elif answer == 'walk':
        print('You have to walk a long distance and you will be out of the water.. ')
        quit()
    else:
        print('Not a valid answer. You loose ')
        quit()

elif answer == 'right':
    answer = input(
        "You came to bridge. Now you have to cross the bride to reach the goal. chose one option back or cross")
    if answer == 'back':
        print("You are back on the road.")
        answer = input(
            'You can now swim across the river or walk around the road. Choose one')
        if answer == 'swim':
            print("You'll be killed by alligator. And you loose the game. ")
            quit()

        elif answer == 'walk':
            print('You have to walk a long distance and you will be out of the water.. ')
            quit()
    elif answer == 'cross':
        print('You can meet different strangers.')
        answer = input('Do you talk with stranger(yes/no)? ')
        if answer == 'yes':
            print('You can reach the goal by their help...')
            answer = input(
                'Do you have money to pay the help for stranger(yes/no)? ').lower()
            if answer == 'yes':
                print(
                    'Then you will be on your destination soon. Good Luck. You won the game. ')
            else:
                print(
                    'If your luck goes well then you can reach your destination. Work hard and earn money...')
        elif answer == 'no':
            print('This will be harder to reach your destination. ')
            print('You loose ! ')
            quit()
else:
    print('You loose! ')
    quit()
