print('Welcome to my quiz game! ')
playing = input('Do you want to play? ').lower()

if playing != 'yes':
    quit()
print("Let's play the game! ")
score = 0

answer = input('What is the full form of CPU? ')
if answer.lower() == 'central processing unit':
    print('Your answer is correct')
    score += 1
else:
    print('Incorrect !')


answer = input('What is the full form of GPU? ')
if answer.lower() == 'graphics processing unit':
    print('Your answer is correct')
    score += 1
else:
    print('Incorrect !')


answer = input('What is the full form of RAM? ')
if answer.lower() == 'read only memory':
    print('Your answer is correct')
    score += 1
else:
    print('Incorrect !')

answer = input('What is the full form of ROM? ')
if answer.lower() == 'random access memory':
    print('Your answer is correct')
    score += 1
else:
    print('Incorrect !')

print('You got ' + str(score) + ' answer correct!')
print('You got ' + str((score/4)*100) + '%.')
