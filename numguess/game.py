
import random

user_name = input('Enter your name: ')
answer = random.randint(1,100)

#for debugging
print(answer)

guess=input('Welcom,{}. Guess the ultimate number:'.format(user_name))

print(guess, answer)
