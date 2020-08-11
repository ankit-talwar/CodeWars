"""
Illustration
given a population p0 increasing at % percent and other additon i.e, aug
if it exceeds population p return in how many iterations
"""


def nb_year(p0, percent, aug, p):
    # your code
    count = 0
    while p0 < p:
        p0 += p0*(percent/100)+aug
        count += 1
    return count

test = nb_year(1500, 5, 100, 5000)
print(test)
        