import random

UserAnswer = ""

print('Hello! I am going to try to guess your age.')
Username = input('What is your name?')

while UserAnswer != y:
    RandomChoice = random.randint(15,30)
    UserAnswer = input('I think your age is: ', RandomChoice, ' years old.')
    if UserAnswer != y:
        print('Rats.')
    else:
        break

