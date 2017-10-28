f = open('GATC.txt', 'r')
sampleText = f.read()
letters = {}
DNASequence = list(sampleText)
for nuc in DNASequence:
	if nuc not in letters:
		letters[nuc] = 1
	else:
		letters[nuc] += 1

#formatted string: percent s each time I have a string value I want
print '%d %d %d %d' % (letters['A'], letters['C'], letters['G'], letters['T'])