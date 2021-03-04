
def print_(obj):
	print(obj, end='\t')
for i in range (1,100+1):
	if i%15  == 0:
		print_('피즈버즈')
	elif i% 3 ==0:
		print_('피즈')
	elif i% 5 ==0:
		print_('버즈')

	else:
		print_(i)
print('') 
