f = open('dictionary.txt', 'r')
g = open('output.txt', 'w')
words = {}
sample_text = f.read()
wordlist = sample_text.split(' ')

for x in wordlist:
	if x in words:
		words[x]+=1
	else: 
		words[x]=1

for key, value in words.items():
	g.write(key + ' ' + str(value) + '\n') 
