"""
Illustration
return a without elements present in both a and b
"""

def array_diff(a, b):
    
    for i in b:
         if i in a:
            for j in range(a.count(i)):
                a.remove(i)
    return a

print(array_diff([1,2,2], [1]))