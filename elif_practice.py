age = input('what is your age:')
age = int(age)
if age < 13:
	print('Elementary school')
elif age >= 13 and age < 18:
	print('Middle school')
elif age >= 18 and age < 22:
	print('University')
else:
	print('Working')