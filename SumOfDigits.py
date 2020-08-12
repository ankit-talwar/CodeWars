"""
Illustration
942  -->  9 + 4 + 2 = 15  -->  1 + 5 = 6
"""

def digital_root(n):
    sum = 0
    #making our int n iterable
    for no in str(n):
        sum += int(no) 
    while sum >=10:
        sum = digital_root(sum)
    return sum

test = digital_root(942)
print(test)