"""
Illustration
In DNA A is the compliment of T and vice versa
& same is with C and G
Eg., if DNA is AAAA result will be TTTT
"""

def Complement(dna):
    dna_dict = {
        'A':'T',
        'T':'A',
        'C':'G',
        'G':'C'
    }
    return ''.join(dna_dict[c] for c in dna)

test = Complement('AAAA')
print(test)