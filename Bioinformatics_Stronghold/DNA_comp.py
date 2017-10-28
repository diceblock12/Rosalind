f = open('DNA_comp.txt', 'r')
DNASequence = f.read()
DNAReverse = DNASequence[::-1]
DNAComplement = DNAReverse.replace('A', 'X')
DNAComplement = DNAComplement.replace('T','A')
DNAComplement = DNAComplement.replace('X', 'T')
DNAComplement = DNAComplement.replace('G', 'Y')
DNAComplement = DNAComplement.replace('C', 'G')
DNAComplement = DNAComplement.replace('Y', 'C')
print DNAComplement