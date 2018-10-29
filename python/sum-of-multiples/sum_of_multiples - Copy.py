from math import gcd
from itertools import combinations

def sum_of_multiples(limit, multiples):
    if(len(multiples) is 0):
        return 0
    set_of_sums = set()
    multiple_of_multiples = [find_lcm(pair) for pair in combinations(multiples, 2)]

    for x in multiples:
        set_of_sums.add(find_summation_of_x(limit,x))
    summations = 0;
    for x in multiple_of_multiples:
        summations += find_summation_of_x(limit,x)
    if(len(multiples) >1):
        if(len(multiples)>2):
            summations -= find_summation_of_x(limit,find_lcm(multiple_of_multiples))
        return sum(set_of_sums) - summations
    return sum(set_of_sums)


def find_lcm(numbers):
    lcm = int(numbers[0])
    for i in numbers[1:]:
      i = int(i)
      lcm = int(lcm)
      lcm = lcm*i/gcd(lcm, i)
    return int(lcm)

def find_summation_of_x(limit, x):
    highest = int(limit/x) *x
    if(highest == limit):
        highest-=x
    summands = int(highest/x)
    summation = int(summands*(x+highest)/2)
    return summation
