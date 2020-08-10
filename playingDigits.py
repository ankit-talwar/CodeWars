"""
Illustration 
dig_pow(46288, 3) should return 51 since 4³ + 6⁴+ 2⁵ + 8⁶ + 8⁷ = 2360688 = 46288 * 51
"""

def dig_pow(n, p):
    num = str(n)
    total = sum([int(num[i])**(p+i) for i in range(len(num))])
    return total/n if (total % n) ==0 else -1
    

result = dig_pow(46288, 3)
print(result)