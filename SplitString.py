"""Illustration
split the string into pairs and if last one doesn't have one
add _ to it
"""

def solution(s):
    #checking if have to add _ or not
    if len(s)%2 == 0:
        result = [s[2*i:2+2*i] for i in range(len(s)//2)]
    else:
        result = [s[2*i:2+2*i] for i in range(len(s)//2)]
        last_pair = s[-1] + '_'
        result.append(last_pair)
    return result
    
#test 
print(solution("asdfads"))
print(solution("asdfadsf"))