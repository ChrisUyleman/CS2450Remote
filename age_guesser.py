import random

UserAnswer = ""

print('Hello! I am going to try to guess your age.')
Username = input('What is your name?')

while UserAnswer != "y":
    RandomChoice = random.randint(15,30)
    UserAnswer = input(f'I think your age is: {RandomChoice} years old. Am I right? (y/n)').strip().lower()
    if UserAnswer == "y":
<<<<<<< HEAD
        break    
=======
        break
>>>>>>> 225a198 (initial commit + journal)
    print('Rats.')

print(f'Nice to meet you, {Username}!')

