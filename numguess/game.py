
import random

user_name = input('Enter your name: ')
print(f'Welcome!{user_name}.')
answer = random.randint(1,100)

#for debugging
#print(answer)

for i in range (1,3+1):
	guess=int(input( 'Guess the ultimate number:'))
#for debugging
#print(i)

	if guess==answer:
		print("Correct!")
		break
	else:
		print("Guess once again!")
