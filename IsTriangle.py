"""
Illustration
return True if the following conditions are matched:
a + b> c, b+c>a, a+c>b (where a,b,c are sides of the triangle)
else return False
"""
def is_trianlge(a,b,c):
    return True if a+b>c and b+c>a and a+c>b else False

result = is_trianlge(1,2,3)
print(result)