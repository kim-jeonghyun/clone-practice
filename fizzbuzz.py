for i in range (1,100+1):
	if i%15  == 0:
		print('fizzbuzz', end='\t' )
	elif i% 3 ==0:
		print('fizz', end='\t')
	elif i% 5 ==0:
		print('buzz',  end='\t')

	else:
		print(i, end='\t')
print('') 
