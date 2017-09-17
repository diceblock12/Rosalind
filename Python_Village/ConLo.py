a = 4186
b = 8833
if a % 2 == 0:
	a += 1


#while a <= b:
#	sum += a
#	a += 2



print sum(range(a, b+1, 2)) 
#range gives us a list of all the odd numbers between a and b
#sum will add up all the numbers in that range.