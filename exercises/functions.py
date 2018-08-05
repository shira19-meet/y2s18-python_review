# Write your solution for 1.4 here!

def is_prime(x):
	prime = True
	for i in range(2,x):
		if (x%i==0):
			prime=False
		# Code
	return prime


print(is_prime(2))