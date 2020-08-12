"""
Illustration
given a list of direction n,s,e,w in a list walk
each item in the list takes 1 minute to cross a block
return True  if it takes exact 10 minutes and return to starting point
else False
Eg., ['n','s','n','s','n','s','n','s','n','s']), 'should return True'
['n','n','n','s','n','s','n','s','n','s']), 'should return False'
"""

def is_valid_walk(walk):
    x=0
    y=0
    if len(walk) == 10:
        for dir in walk:
            if dir == 'n':
                y += 1
            elif dir == 's':
                y -= 1
            elif dir == 'e':
                x += 1
            else:
                x -= 1
        if x == 0 and y == 0:
            return True
        else:
            return False
    else:
        return False

test = is_valid_walk(['n','s','n','s','n','s','n','s','n','s'])
print(test)
    