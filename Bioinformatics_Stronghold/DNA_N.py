f = open('GATC.txt', 'r')
sampleText = f.read()
letters = {}
DNASequence = sampleText.split()
for nuc in DNASequence:
	if nuc not in letters:
		letters[nuc] = 1
	else:
		letters[nuc] += 1

for letter in letters.values():
	print letter