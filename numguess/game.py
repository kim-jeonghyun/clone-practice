
import random

user_name = input('Enter your name: ')
answer = random.randint(1,100)

#for debugging
print(answer)

guess=int(input('Welcom,{}. Guess the ultimate number:'.format(user_name)))

#for debugging
print(guess, answer)

if guess==answer:
	print("Correct!")
else:
	print("Maybe next time!")
