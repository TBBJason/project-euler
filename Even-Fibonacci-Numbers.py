# By considering the terms in the Fibonacci sequence whose values do not exceed four million, find the sum of the even-valued terms.

"""
Intuition: from leetcode, I think the fastest way to compute fibonacci numbers without knowing is still O(n) using DP
Store the numbers in a vector, keep adding until we exceed 4 million, keep track of total if number is even.

1. Solution:   
    a) use dp to find our fibonacci array, doesn't necessarily need an array since we only store 2 numbers
    b) keep track of total
    c) check if number is even then add it to our running total

"""


def evenFibonacci(highest=4000000):
    num1 = 1
    num2 = 2
    res = 2
    curr = None
    while(True):
        curr = num1 + num2
        if (curr >= highest):
            return res
        
        if (curr % 2 == 0):
            res += curr

        num1 = num2
        num2 = curr
    

print(evenFibonacci(highest = 100))
print(evenFibonacci())