"""
Illustration
sorting the string on the basis of numbers present in string item
Eg., "is2 Thi1s T4est 3a"  -->  "Thi1s is2 3a T4est"
"""

import re
def order(sentence):
    final = ''
    sentence = sentence.strip().split()
    result = sorted(sentence, key=lambda str: re.findall("\d+", str)) #regular expression to get int in str
    return   ' '.join(result)

test = order("is2 Thi1s T4est 3a")
print(test)
      
   
    
     