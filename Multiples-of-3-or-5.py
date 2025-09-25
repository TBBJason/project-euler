# Find the sum of all multiples of 3 and 5 below 1000

"""Idea: sum all the multiples of 3 and 5 using:
1. Looking into the 3 case, 5 is similar,
    a) divide the number n by 3, assuming n is our input
    b) the output will be the # of times a number that's a multiple of 3 appears
    c) find the summation of i = 1, n = n. Multiply by 3 to find all the sums of 3

2. Handling the cases where 3 and 5 both divide:
    a) we'll have some overlap when we divide, we double count
    b) the same idea behind 5 and 3, find all the numbers that are divisible by 15,
    c) subtract this total:

3. Small change in bugs, the question wants BELOW n, not at n, so we do n - 1

"""

def multiple_of_3_or_5(n):
    n = n - 1 
    numof3 = n // 3
    numof5 = n // 5
    numof15 = n // 15

    total3 = (numof3 + 1)*(numof3) * 3 // 2
    total5 = (numof5 + 1)*(numof5) * 5 // 2
    total15 = (numof15 + 1)*(numof15) * 15 // 2

    total = total3 + total5 - total15

    return total


print(multiple_of_3_or_5(10))
print(multiple_of_3_or_5(1000))
