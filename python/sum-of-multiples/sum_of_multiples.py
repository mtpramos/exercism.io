from math import gcd
from itertools import combinations

def sum_of_multiples(limit, multiples):
    set_of_sums = list()
    for x in multiples:
        set_of_sums += list(range(x,limit,x))
    return sum(set(set_of_sums))
