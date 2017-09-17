f = open('WWF.txt', 'r')

newString = []
i = 0
for line in f:
	i += 1
	if i % 2 == 0:
		print line.strip()