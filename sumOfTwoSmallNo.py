"""
Illustration
sum of the two smallest numbers in the list
Eg., [5,2,55,10] -> 5+2 = 7
"""
def sum_two_smallest_no(numbers):
    numbers.sort()
    return numbers[0]+numbers[1]

result = sum_two_smallest_no([5,2,55,10])
print(result)
