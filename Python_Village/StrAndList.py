f = open("data.txt", "r")
sample_text = f.readlines() #reads in the stuff from data and stores it in a strings called "sample_text"
stripped_strings = []  #initialize empty list
for x in sample_text:
	stripped = x.rstrip() #removes last character in string if it's the /n char
	stripped_strings.append(stripped) #adds the slightly edited list to a new one

numList = stripped_strings[1].split(' ') #add the numbers from stripped_strings (data.txt) to a new list (not string) and make sure to separate them by space
print stripped_strings[0][int(numList[0]):int(numList[1])+1]
print stripped_strings[0][int(numList[2]):int(numList[3])+1] #to convert something to an integer, do int(whatIwannaConvert)
f.close()